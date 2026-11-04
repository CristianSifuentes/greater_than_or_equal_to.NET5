#!/usr/bin/env python3
"""Descarga los metadatos oficiales de .NET y regenera data/versiones.csv y data/parches.csv.

Fuente: https://github.com/dotnet/core/tree/main/release-notes  (releases.json por canal)
Uso:    python3 tools/actualizar_datos.py   (solo biblioteca estándar, Python 3.9+)

Notas sobre los datos:
  * La entrada 9.0.0 de releases.json trae la fecha de su republicación (2024-12-03, SDK 9.0.101).
    La GA real fue el 2024-11-12, según la página de soporte: ver GA_CORREGIDA.
  * El campo vs-version del SDK de 10.0.0 trae un error ("10.0.0"); se usa el del runtime.
  * Los CVE se cuentan una sola vez por canal, en el primer parche que los corrige.
"""
from __future__ import annotations

import csv
import json
import subprocess
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BASE = "https://raw.githubusercontent.com/dotnet/core/main/release-notes"
CANALES = ["5.0", "6.0", "7.0", "8.0", "9.0", "10.0", "11.0"]
GA_CORREGIDA = {"9.0": "2024-11-12"}


def descargar(canal: str) -> dict:
    url = f"{BASE}/{canal}/releases.json"
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return json.load(r)
    except urllib.error.URLError:
        # El Python de python.org en macOS no trae certificados raíz: curl sí verifica TLS
        # con los del sistema, así que se usa como respaldo sin desactivar la verificación.
        salida = subprocess.run(["curl", "-fsSL", url], check=True, capture_output=True)
        return json.loads(salida.stdout)


def main() -> None:
    versiones, parches = [], []
    primera_vez: dict[str, str] = {}  # CVE -> fecha del primer parche que lo corrige, en cualquier canal
    for canal in CANALES:
        datos = descargar(canal)
        lanzamientos = list(reversed(datos["releases"]))  # del más antiguo al más nuevo
        ga = next((r for r in lanzamientos if r["release-version"] == f"{canal}.0"), None)
        estables = [r for r in lanzamientos if "-" not in r["release-version"]]
        previas = [r for r in lanzamientos if "-" in r["release-version"]]
        vistos: set[str] = set()
        for r in lanzamientos:
            cves = [c["cve-id"] for c in (r.get("cve-list") or [])]
            nuevos = [c for c in cves if c not in vistos]
            vistos.update(cves)
            for c in cves:
                if c not in primera_vez or r["release-date"] < primera_vez[c]:
                    primera_vez[c] = r["release-date"]
            parches.append({
                "canal": canal,
                "version": r["release-version"],
                "fecha": r["release-date"],
                "seguridad": int(bool(r.get("security"))),
                "cve_nuevos": len(nuevos),
                "sdk": (r.get("sdk") or {}).get("version", ""),
            })
        sdk = (ga or {}).get("sdk", {})
        versiones.append({
            "canal": canal,
            "tipo": datos["release-type"].upper(),
            "fase": datos["support-phase"],
            "ga": GA_CORREGIDA.get(canal, ga["release-date"] if ga else ""),
            "fin_soporte": datos.get("eol-date") or "",
            "ultima": datos["latest-release"],
            "ultima_fecha": datos["latest-release-date"],
            "ultimo_sdk": datos["latest-sdk"],
            "csharp": sdk.get("csharp-version", ""),
            "fsharp": sdk.get("fsharp-version", ""),
            "vb": sdk.get("vb-version", ""),
            "vs": (ga or {}).get("runtime", {}).get("vs-version", ""),
            "parches": max(len(estables) - 1, 0),
            "parches_seguridad": sum(1 for r in estables if r.get("security")),
            "previas": len(previas),
            "cve": len(vistos),
        })
    destino = RAIZ / "data"
    destino.mkdir(exist_ok=True)
    for nombre, filas in (("versiones.csv", versiones), ("parches.csv", parches)):
        with open(destino / nombre, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(filas[0]))
            w.writeheader()
            w.writerows(filas)
    anios: dict[str, int] = {}
    for fecha in primera_vez.values():
        anios[fecha[:4]] = anios.get(fecha[:4], 0) + 1
    with open(destino / "cve-por-anio.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["anio", "cve_unicos"])
        w.writerows(sorted(anios.items()))
    print(f"{len(versiones)} canales y {len(parches)} lanzamientos escritos en data/")


if __name__ == "__main__":
    main()
