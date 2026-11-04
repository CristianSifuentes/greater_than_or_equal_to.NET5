#!/usr/bin/env python3
"""Genera el catálogo A–Z y las ilustraciones SVG de .NET Atlas.

Fuentes:  data/caracteristicas.csv · data/versiones.csv · data/cve-por-anio.csv · data/laboratorio.csv
Salidas:  docs/23-catalogo-a-z.md
          assets/net-atlas-banner.svg
          assets/net-atlas-tabla-periodica.svg
          assets/net-atlas-soporte.svg
          assets/net-atlas-cve.svg
          assets/net-atlas-laboratorio.svg  (si existe data/laboratorio.csv)

Uso:  python3 tools/generar_atlas.py   (solo biblioteca estándar, Python 3.9+)
"""
from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "data"
ASSETS = RAIZ / "assets"
CATALOGO = RAIZ / "docs" / "23-catalogo-a-z.md"

CORTE = date(2026, 11, 4)
EDICION = "4 de noviembre de 2026"
FUENTE = "Segoe UI, Inter, Helvetica Neue, Arial, sans-serif"

# Superficie y tinta. La paleta categórica pasa validate_palette.js sobre SUPERFICIE
# (ΔE CVD adyacente ≥ 8, ΔE normal ≥ 15, contraste ≥ 3:1).
SUPERFICIE = "#0F0D22"
TINTA = "#F4F2FF"
TINTA_2 = "#C4BFE0"
TINTA_3 = "#8D87AD"
REJILLA = "#2C2850"

# Ocho grupos: nunca más que los tonos validados. (clave, nombre, color, áreas del CSV)
GRUPOS = [
    ("lenguaje", "Lenguaje", "#3987e5", {"lenguaje"}),
    ("runtime", "Runtime", "#d95926", {"runtime"}),
    ("despliegue", "AOT y despliegue", "#199e70", {"despliegue"}),
    ("bcl", "Bibliotecas base", "#c98500", {"bcl"}),
    ("web", "Web y clientes", "#d55181", {"web", "clientes"}),
    ("datos", "Datos", "#008300", {"datos"}),
    ("nube", "Nube e IA", "#9085e9", {"cloud", "ia"}),
    ("sdk", "SDK y seguridad", "#e66767", {"sdk", "seguridad"}),
]
GRUPO_DE_AREA = {a: g for g in GRUPOS for a in g[3]}
NOMBRE_AREA = {
    "lenguaje": "Lenguaje", "runtime": "Runtime", "despliegue": "AOT y despliegue",
    "bcl": "Bibliotecas base", "web": "Web", "clientes": "Clientes", "datos": "Datos",
    "cloud": "Nube", "ia": "IA", "sdk": "SDK", "seguridad": "Seguridad",
}
CAPITULOS = {
    "10": "10-lenguajes-csharp-fsharp-vb.md", "11": "11-runtime-jit-y-gc.md",
    "12": "12-aot-despliegue-y-contenedores.md", "13": "13-bibliotecas-base.md",
    "14": "14-aspnet-core-y-blazor.md", "15": "15-datos-y-ef-core.md",
    "16": "16-clientes-maui-wpf-winforms.md", "17": "17-cloud-native-aspire-y-observabilidad.md",
    "18": "18-ia-en-net.md", "19": "19-sdk-herramientas-y-pruebas.md",
    "20": "20-seguridad-y-cadena-de-suministro.md",
}
TEMAS = {
    "5": "La unificación", "6": "La consolidación", "7": "La velocidad", "8": "La nube nativa",
    "9": "La adaptación", "10": "La madurez", "11": "La reescritura silenciosa",
}
ESTADOS = {"GA": "🟢 GA", "RC": "🟡 RC", "Preview": "🟡 Preview", "Experimental": "🧪 Experimental"}


def leer(nombre: str) -> list[dict]:
    with open(DATOS / nombre, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def orden(texto: str) -> str:
    plano = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in plano if not unicodedata.combining(c)).lstrip(".#").casefold()


def fecha_de(iso: str) -> date:
    a, m, d = (int(x) for x in iso.split("-"))
    return date(a, m, d)


def lienzo(ancho: int, alto: int, titulo: str, cuerpo: str, defs: str = "") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" '
        f'height="{alto}" font-family="{FUENTE}" role="img" aria-label="{escape(titulo)}">\n'
        f"<title>{escape(titulo)}</title>\n<defs>{defs}</defs>\n"
        f'<rect width="{ancho}" height="{alto}" rx="14" fill="{SUPERFICIE}"/>\n{cuerpo}\n</svg>\n'
    )


def texto(x, y, t, tam=14, color=TINTA, peso=400, ancla="start", extra="") -> str:
    return (f'<text x="{x}" y="{y}" font-size="{tam}" fill="{color}" font-weight="{peso}" '
            f'text-anchor="{ancla}" {extra}>{escape(str(t))}</text>')


def recortar(t: str, n: int) -> list[str]:
    """Parte un nombre en un máximo de dos líneas de n caracteres."""
    if len(t) <= n:
        return [t]
    # Una palabra larga con puntos o barras se puede partir en esos separadores
    palabras = [q for p in t.split() for q in (re.split(r"(?<=[./])", p) if len(p) > n else [p]) if q]
    lineas, actual = [], ""
    for p in palabras:
        if len(actual) + len(p) + 1 > n and actual:
            lineas.append(actual)
            actual = p
        else:
            actual = f"{actual}{p}" if actual.endswith((".", "/")) else f"{actual} {p}".strip()
    lineas.append(actual)
    if len(lineas) > 2:
        lineas = [lineas[0], " ".join(lineas[1:])]
    return [l if len(l) <= n + 1 else l[: n].rstrip() + "…" for l in lineas]


def generar_catalogo(items: list[dict], versiones: list[dict]) -> None:
    por_letra: dict[str, list[dict]] = defaultdict(list)
    for it in sorted(items, key=lambda i: orden(i["nombre"])):
        inicial = orden(it["nombre"])[0].upper()
        por_letra[inicial if inicial.isalpha() else "#"].append(it)

    conteo_v = Counter(i["version"] for i in items)
    conteo_a = Counter(i["area"] for i in items)
    o = [
        '<div align="center">\n',
        "# 23 · Catálogo A–Z\n",
        f"**{len(items)} capacidades de la plataforma, de .NET 5 a .NET 11, con su versión de origen y estado**\n",
        "[⬅ 22 · Guías de decisión](22-guias-de-decision.md) · [🏠 Índice](../README.md) · "
        "[24 · Laboratorio ➡](24-laboratorio.md)\n",
        "</div>\n",
        "> [!NOTE]\n> Este capítulo se **genera** desde `data/caracteristicas.csv` con "
        "`python3 tools/generar_atlas.py`. No lo edites a mano.\n"
        f"> Estado verificado al **{EDICION}**. La columna *Desde* indica la primera versión de .NET "
        "con la capacidad, no la última que la mejoró.\n",
        "---\n",
        "## Resumen\n",
        "| .NET | Tema | Capacidades catalogadas |",
        "|---|---|---:|",
    ]
    for v in ("5", "6", "7", "8", "9", "10", "11"):
        o.append(f"| **{v}** | {TEMAS[v]} | {conteo_v[v]} |")
    o += ["", "| Área | Capacidades |", "|---|---:|"]
    for a, n in conteo_a.most_common():
        o.append(f"| {NOMBRE_AREA[a]} | {n} |")
    o += ["", "**Saltar a:** " + " · ".join(f"[{l}](#{l.lower()})" for l in sorted(por_letra) if l != "#"), "", "---", ""]
    for letra in sorted(por_letra):
        if letra == "#":
            continue
        o += [f"## {letra}\n", "| Capacidad | Área | Desde | Estado | Descripción |", "|---|---|:---:|---|---|"]
        for it in por_letra[letra]:
            enlace = f"[{it['nombre']}]({CAPITULOS[it['capitulo']]})".replace("|", "\\|")
            desc = it["descripcion"].replace("|", "\\|")
            o.append(f"| {enlace} | {NOMBRE_AREA[it['area']]} | .NET {it['version']} | {ESTADOS[it['estado']]} | {desc} |")
        o.append("")
    o += ["---\n", '<div align="center">\n',
          "[⬅ 22 · Guías de decisión](22-guias-de-decision.md) · [🏠 Índice](../README.md) · "
          "[24 · Laboratorio ➡](24-laboratorio.md)\n", "</div>\n"]
    CATALOGO.write_text("\n".join(o), encoding="utf-8")


def generar_tabla_periodica(items: list[dict]) -> None:
    visibles = [i for i in items if i["poster"] == "1"]
    por_version = defaultdict(list)
    for i in visibles:
        por_version[i["version"]].append(i)
    orden_grupo = {g[0]: n for n, g in enumerate(GRUPOS)}

    col, tile_w, tile_h, gap = 12, 118, 92, 8
    izq, sup = 214, 150
    ancho = izq + col * (tile_w + gap) + 24
    y = sup
    cuerpo = [
        texto(40, 60, "Tabla periódica de .NET", 34, TINTA, 700),
        texto(40, 92, f"{len(visibles)} elementos de 5 a 11 · cada fila es un periodo, cada color un grupo · edición {EDICION}", 16, TINTA_2),
    ]
    numero = 0
    for v in ("5", "6", "7", "8", "9", "10", "11"):
        lista = sorted(por_version[v], key=lambda i: (orden_grupo[GRUPO_DE_AREA[i["area"]][0]], orden(i["nombre"])))
        filas = -(-len(lista) // col)
        alto_banda = filas * (tile_h + gap)
        cuerpo.append(texto(40, y + 40, f".NET {v}", 28, TINTA, 700))
        cuerpo.append(texto(40, y + 62, TEMAS[v], 13, TINTA_2))
        for n, it in enumerate(lista):
            numero += 1
            x = izq + (n % col) * (tile_w + gap)
            yy = y + (n // col) * (tile_h + gap)
            c = GRUPO_DE_AREA[it["area"]][2]
            guion = ' stroke-dasharray="5 4"' if it["estado"] in ("Preview", "Experimental") else ""
            cuerpo.append(f'<rect x="{x}" y="{yy}" width="{tile_w}" height="{tile_h}" rx="7" fill="{c}" fill-opacity="0.16" stroke="{c}" stroke-width="1.5"{guion}/>')
            cuerpo.append(texto(x + tile_w - 8, yy + 16, numero, 10, TINTA_3, 400, "end"))
            cuerpo.append(texto(x + 9, yy + 35, it["simbolo"], 25, TINTA, 700))
            for k, l in enumerate(recortar(it["nombre"], 18)):
                cuerpo.append(texto(x + 9, yy + 58 + k * 14, l, 11, TINTA_2))
        y += alto_banda + 18
    # Leyenda: siempre presente, en una sola fila
    lx, ly = 40, y + 16
    for _, nombre, c, _a in GRUPOS:
        cuerpo.append(f'<rect x="{lx}" y="{ly}" width="16" height="16" rx="4" fill="{c}"/>')
        cuerpo.append(texto(lx + 23, ly + 13, nombre, 14, TINTA_2))
        lx += 44 + int(len(nombre) * 7.4)
    cuerpo.append(f'<rect x="{lx}" y="{ly}" width="16" height="16" rx="4" fill="none" stroke="{TINTA_2}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    cuerpo.append(texto(lx + 23, ly + 13, "Preview o experimental", 14, TINTA_2))
    alto = ly + 44
    (ASSETS / "net-atlas-tabla-periodica.svg").write_text(
        lienzo(ancho, alto, "Tabla periódica de .NET, de .NET 5 a .NET 11", "\n".join(cuerpo)), encoding="utf-8")


def generar_soporte(versiones: list[dict]) -> None:
    w, izq, der, sup = 1400, 130, 40, 112
    h_fila, gap = 44, 10
    a0, a1 = date(2020, 1, 1), date(2029, 1, 1)
    def x(d: date) -> float:
        return izq + (d - a0).days / (a1 - a0).days * (w - izq - der)
    filas = []
    for v in versiones:
        ga = fecha_de(v["ga"]) if v["ga"] else date(2026, 11, 10)
        fin = fecha_de(v["fin_soporte"]) if v["fin_soporte"] else date(2028, 11, 9)
        filas.append((v, ga, fin, not v["ga"]))
    alto = sup + len(filas) * (h_fila + gap) + 76
    c = [
        texto(40, 50, "Ventanas de soporte de .NET", 28, TINTA, 700),
        texto(40, 78, f"Desde la GA hasta el fin de soporte oficial · corte al {EDICION}", 15, TINTA_2),
    ]
    for anio in range(2020, 2030):
        xx = x(date(anio, 1, 1))
        c.append(f'<line x1="{xx:.1f}" y1="{sup - 8}" x2="{xx:.1f}" y2="{alto - 58}" stroke="{REJILLA}" stroke-width="1"/>')
        if anio < 2029:
            c.append(texto(xx + 6, sup - 14, anio, 13, TINTA_3))
    color = {"LTS": "#3987e5", "STS": "#d95926"}
    y = sup
    for v, ga, fin, previsto in filas:
        tipo = v["tipo"]
        x0, x1 = x(ga), x(fin)
        c.append(texto(40, y + 28, f".NET {v['canal'].split('.')[0]}", 18, TINTA, 700))
        guion = f' stroke="{color[tipo]}" stroke-width="2" stroke-dasharray="6 4" fill-opacity="0.2"' if previsto else ""
        c.append(f'<rect x="{x0:.1f}" y="{y + 7}" width="{x1 - x0:.1f}" height="{h_fila - 14}" rx="4" fill="{color[tipo]}"{guion}/>')
        etiqueta = f"{tipo} · hasta {fin.strftime('%m/%Y')}"
        if previsto:
            etiqueta = "STS · GA prevista · hasta 11/2028"
        c.append(texto(x0 + 10, y + 27, etiqueta, 13, TINTA, 600))
        y += h_fila + gap
    xh = x(CORTE)
    c.append(f'<line x1="{xh:.1f}" y1="{sup - 8}" x2="{xh:.1f}" y2="{alto - 58}" stroke="{TINTA}" stroke-width="2"/>')
    c.append(texto(xh - 8, alto - 40, "hoy", 14, TINTA, 700, "end"))
    ly = alto - 34
    for n, (nombre, col) in enumerate((("LTS · 3 años", "#3987e5"), ("STS · 18 meses hasta .NET 8, 24 desde .NET 9", "#d95926"))):
        lx = 40 + n * 170
        c.append(f'<rect x="{lx}" y="{ly - 13}" width="16" height="16" rx="4" fill="{col}"/>')
        c.append(texto(lx + 23, ly, nombre, 14, TINTA_2))
    (ASSETS / "net-atlas-soporte.svg").write_text(
        lienzo(w, alto, "Ventanas de soporte de .NET 5 a .NET 11", "\n".join(c)), encoding="utf-8")


def generar_barras(nombre: str, titulo: str, sub: str, filas: list[tuple[str, float]], nota: str, formato=str) -> None:
    w, h = 1200, 480
    izq, der, sup, inf = 70, 40, 112, 74
    maximo = max(v for _, v in filas)
    tope = -(-maximo // 20) * 20
    c = [texto(40, 50, titulo, 28, TINTA, 700), texto(40, 78, sub, 15, TINTA_2)]
    alto_p = h - sup - inf
    for t in range(0, int(tope) + 1, 20):
        y = sup + alto_p - t / tope * alto_p
        c.append(f'<line x1="{izq}" y1="{y:.1f}" x2="{w - der}" y2="{y:.1f}" stroke="{REJILLA}"/>')
        c.append(texto(izq - 10, y + 4, t, 12, TINTA_3, 400, "end"))
    paso = (w - izq - der) / len(filas)
    ancho_b = min(64, paso * 0.5)
    for n, (et, v) in enumerate(filas):
        xc = izq + paso * (n + 0.5)
        alto_b = v / tope * alto_p
        y = sup + alto_p - alto_b
        c.append(f'<path d="M{xc - ancho_b / 2:.1f} {sup + alto_p} V{y + 4:.1f} q0 -4 4 -4 H{xc + ancho_b / 2 - 4:.1f} q4 0 4 4 V{sup + alto_p} Z" fill="#3987e5"/>')
        c.append(texto(xc, y - 9, formato(v), 15, TINTA, 700, "middle"))
        c.append(texto(xc, sup + alto_p + 24, et, 14, TINTA_2, 400, "middle"))
    c.append(texto(40, h - 22, nota, 13, TINTA_3))
    (ASSETS / nombre).write_text(lienzo(w, h, titulo, "\n".join(c)), encoding="utf-8")


def generar_laboratorio() -> None:
    ruta = DATOS / "laboratorio.csv"
    if not ruta.exists():
        return
    filas = list(csv.DictReader(open(ruta, encoding="utf-8")))
    filas = [f for f in filas if f["tipo"] == "micro"]
    pruebas = list(dict.fromkeys(f["prueba"] for f in filas))
    versiones = ["net8.0", "net9.0", "net10.0", "net11.0"]
    # Secuencial de un solo tono: .NET 8 claro, .NET 11 oscuro sobre fondo oscuro se invierte.
    tonos = {"net8.0": "#2F5F9E", "net9.0": "#3F7AC4", "net10.0": "#6BA3EA", "net11.0": "#BBD6F8"}
    w, izq, der, sup = 1200, 240, 90, 120
    h_prueba = 64
    alto = sup + len(pruebas) * h_prueba + 60
    c = [
        texto(40, 50, "Laboratorio: tiempo relativo a .NET 8", 28, TINTA, 700),
        texto(40, 78, "Misma prueba en cada runtime · 100 % = .NET 8 · menos es mejor · Apple M4, una máquina", 15, TINTA_2),
    ]
    tope = 1.2
    x = lambda r: izq + r / tope * (w - izq - der)
    xb = x(1.0)
    y = sup
    por = {(f["prueba"], f["runtime"]): float(f["media_ns"]) for f in filas}
    for p in pruebas:
        c.append(texto(izq - 14, y + 30, p, 14, TINTA, 500, "end"))
        base = por[(p, "net8.0")]
        for n, v in enumerate(versiones):
            r = por[(p, v)] / base
            yy = y + 4 + n * 13
            c.append(f'<rect x="{izq}" y="{yy}" width="{max(x(min(r, tope)) - izq, 2):.1f}" height="11" rx="3" fill="{tonos[v]}"/>')
            if v == "net11.0":
                # Si la etiqueta caería sobre la línea de referencia, se coloca a su derecha
                xe = xb + 8 if 0.9 <= r <= 1.02 else x(min(r, tope)) + 7
                c.append(texto(xe, yy + 10, f"{r * 100:.0f} %", 12, TINTA, 600))
        y += h_prueba
    c.append(f'<line x1="{xb:.1f}" y1="{sup - 6}" x2="{xb:.1f}" y2="{y}" stroke="{TINTA_2}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    lx = 40
    for v in versiones:
        c.append(f'<rect x="{lx}" y="{alto - 40}" width="16" height="16" rx="4" fill="{tonos[v]}"/>')
        c.append(texto(lx + 23, alto - 27, ".NET " + v[3:-2], 14, TINTA_2))
        lx += 110
    (ASSETS / "net-atlas-laboratorio.svg").write_text(
        lienzo(w, alto, "Tiempo relativo a .NET 8 en microbenchmarks", "\n".join(c)), encoding="utf-8")


def generar_banner(items: list[dict], versiones: list[dict]) -> None:
    w, h = 1600, 440
    defs = (
        '<linearGradient id="fondo" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B0920"/>'
        '<stop offset="0.6" stop-color="#1A1145"/><stop offset="1" stop-color="#34188A"/></linearGradient>'
        '<radialGradient id="halo" cx="0.82" cy="0.42" r="0.5"><stop offset="0" stop-color="#7C5CFC" stop-opacity="0.5"/>'
        '<stop offset="1" stop-color="#7C5CFC" stop-opacity="0"/></radialGradient>'
        '<pattern id="puntos" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.1" fill="#fff" fill-opacity="0.05"/></pattern>'
        '<linearGradient id="trazo" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6B4FE0"/><stop offset="1" stop-color="#C9B8FF"/></linearGradient>'
        '<filter id="brillo" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="6" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    )
    c = [
        f'<rect width="{w}" height="{h}" fill="url(#fondo)"/>',
        f'<rect width="{w}" height="{h}" fill="url(#halo)"/>',
        f'<rect width="{w}" height="{h}" fill="url(#puntos)"/>',
        texto(72, 158, ".NET ATLAS", 76, "#F8F7FF", 800, extra='letter-spacing="9"'),
        texto(76, 206, "De .NET 5 a .NET 11: runtime, lenguaje, nube e IA", 27, "#D9D2FF"),
        texto(76, 242, f"25 capítulos · {len(items)} capacidades catalogadas · datos oficiales y laboratorio propio", 17, "#A9A0D6"),
        texto(76, 270, f"Edición del {EDICION}", 17, "#A9A0D6"),
    ]
    # Órbita: siete versiones sobre una curva ascendente
    puntos = []
    n = len(versiones)
    for i, v in enumerate(versiones):
        px = 820 + i * 112
        py = 340 - (i ** 1.35) * 27
        puntos.append((px, py, v))
    ruta = "M" + " L".join(f"{p[0]} {p[1]:.1f}" for p in puntos)
    c.append(f'<path d="{ruta}" fill="none" stroke="url(#trazo)" stroke-width="3" stroke-linecap="round"/>')
    relleno = {"eol": "#3A3560", "maintenance": "#d95926", "active": "#199e70", "go-live": "#c98500"}
    for px, py, v in puntos:
        r = 27 if v["tipo"] == "LTS" else 21
        c.append(f'<circle cx="{px}" cy="{py:.1f}" r="{r}" fill="{relleno[v["fase"]]}" stroke="#E9E4FF" stroke-width="2" filter="url(#brillo)"/>')
        c.append(texto(px, py + 6, v["canal"].split(".")[0], 19, "#FFFFFF", 700, "middle"))
        c.append(texto(px, py + r + 22, v["tipo"], 12, "#C9C2EE", 600, "middle"))
    lx = 76
    for nombre, col in (("Sin soporte", "#3A3560"), ("Fin 10-nov-2026", "#d95926"), ("Soporte activo", "#199e70"), ("Release candidate", "#c98500")):
        c.append(f'<circle cx="{lx + 7}" cy="326" r="7" fill="{col}" stroke="#E9E4FF"/>')
        c.append(texto(lx + 22, 331, nombre, 14, "#D9D2FF"))
        lx += 34 + int(len(nombre) * 7.6)
    (ASSETS / "net-atlas-banner.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="{FUENTE}" '
        f'role="img" aria-label=".NET Atlas"><title>.NET Atlas · De .NET 5 a .NET 11</title><defs>{defs}</defs>\n'
        + "\n".join(c) + "\n</svg>\n", encoding="utf-8")


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    CATALOGO.parent.mkdir(exist_ok=True)
    items = leer("caracteristicas.csv")
    versiones = leer("versiones.csv")
    generar_catalogo(items, versiones)
    generar_tabla_periodica(items)
    generar_soporte(versiones)
    cves = [(f["anio"], float(f["cve_unicos"])) for f in leer("cve-por-anio.csv")]
    generar_barras(
        "net-atlas-cve.svg", "CVE corregidos en .NET por año",
        "CVE únicos, contados en el primer parche que los corrige, en cualquier versión de .NET 5 a 11",
        cves, "Fuente: releases.json oficial. 2026 llega hasta el parche fuera de ciclo del 25 de octubre.",
        lambda v: f"{v:.0f}",
    )
    generar_laboratorio()
    generar_banner(items, versiones)
    print(f"Catálogo: {len(items)} capacidades · SVG regenerados en assets/")


if __name__ == "__main__":
    main()
