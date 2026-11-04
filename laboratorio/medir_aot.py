#!/usr/bin/env python3
"""Mide tamaño, tiempo y memoria de apps con JIT y Native AOT en .NET 8, 9, 10 y 11.

Uso:  python3 laboratorio/medir_aot.py [rid]     (por defecto osx-arm64)
Requiere el SDK de .NET 11 con los runtimes 8, 9 y 10, y el compilador C del sistema.
Modifica temporalmente el TargetFramework de los proyectos de laboratorio/aot y lo restaura al final.
"""
import json
import re
import shutil
import statistics as st
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent / "aot"
RID = sys.argv[1] if len(sys.argv) > 1 else "osx-arm64"
VERSIONES = ["net8.0", "net9.0", "net10.0", "net11.0"]


def medir_consola(exe: str) -> float:
    tiempos = []
    for _ in range(40):
        inicio = time.perf_counter()
        subprocess.run([exe], capture_output=True)
        tiempos.append((time.perf_counter() - inicio) * 1000)
    return st.median(tiempos[5:])


def medir_web(exe: str) -> tuple[float, float]:
    tiempos, memoria = [], []
    for i in range(14):
        puerto = 5900 + i
        entorno = {"ASPNETCORE_URLS": f"http://127.0.0.1:{puerto}"}
        inicio = time.perf_counter()
        proceso = subprocess.Popen([exe], env=entorno, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        while time.perf_counter() - inicio < 20:
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=1).read()
                break
            except OSError:
                time.sleep(0.002)
        tiempos.append((time.perf_counter() - inicio) * 1000)
        rss = subprocess.run(["ps", "-o", "rss=", "-p", str(proceso.pid)], capture_output=True, text=True)
        memoria.append(int(rss.stdout.strip() or 0))
        proceso.kill()
        proceso.wait()
    return st.median(tiempos[2:]), st.median(memoria[2:]) / 1024


def main() -> None:
    resultados = {}
    salida = Path(tempfile.mkdtemp(prefix="net-atlas-"))
    for app in ("hello", "web"):
        proyecto = RAIZ / app / f"{app}.csproj"
        original = proyecto.read_text()
        try:
            for tfm in VERSIONES:
                proyecto.write_text(re.sub(r"<TargetFramework>[^<]+", f"<TargetFramework>{tfm}", original))
                fila = {}
                for modo, extra in (("aot", ["-p:PublishAot=true"]), ("jit", ["--self-contained", "false"])):
                    for d in ("bin", "obj"):
                        shutil.rmtree(proyecto.parent / d, ignore_errors=True)
                    destino = salida / f"{app}-{tfm}-{modo}"
                    subprocess.run(["dotnet", "publish", "-c", "Release", "-r", RID, *extra, "-o", str(destino)],
                                   cwd=proyecto.parent, check=True, capture_output=True)
                    exe = str(destino / app)
                    fila[f"{modo}_mb"] = round(Path(exe).stat().st_size / 1e6, 2)
                    if app == "hello":
                        fila[f"{modo}_ms"] = round(medir_consola(exe), 1)
                    else:
                        primera, rss = medir_web(exe)
                        fila[f"{modo}_primera_ms"] = round(primera, 1)
                        fila[f"{modo}_rss_mb"] = round(rss, 1)
                resultados[f"{app}-{tfm}"] = fila
                print(app, tfm, fila, flush=True)
        finally:
            proyecto.write_text(original)
            for d in ("bin", "obj"):
                shutil.rmtree(proyecto.parent / d, ignore_errors=True)
    print(json.dumps(resultados, indent=1))


if __name__ == "__main__":
    main()
