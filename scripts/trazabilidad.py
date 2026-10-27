"""Comprueba que cada criterio de aceptación de SPECS.md tiene al menos un test.

    uv run python scripts/trazabilidad.py

Un criterio se declara en SPECS.md como "CA<número>" en la sección "Criterios de aceptación".
Un test lo verifica si lleva @pytest.mark.criterio("CA<número>").
Sale con código 1 si falta algún test o si un test cita un criterio que no existe.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PROFESORADO = {f"CD{i}" for i in range(1, 6)}


def criterios_en_specs() -> set[str]:
    texto = (RAIZ / "SPECS.md").read_text(encoding="utf-8")
    texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)        # ignorar las indicaciones de la plantilla
    m = re.search(r"^##\s*\d*\.?\s*Criterios de aceptación\s*$(.*?)(?=^##\s|\Z)", texto, flags=re.M | re.S | re.I)
    seccion = m.group(1) if m else ""
    return set(re.findall(r"\bCA\d+\b", seccion))


def criterios_en_tests() -> dict[str, list[str]]:
    usados: dict[str, list[str]] = {}
    for f in (RAIZ / "tests").rglob("test_*.py"):
        for cid in re.findall(r"criterio\(\s*[\"']((?:CA|CD)\d+)[\"']\s*\)", f.read_text(encoding="utf-8")):
            usados.setdefault(cid, []).append(str(f.relative_to(RAIZ)))
    return usados


def main() -> int:
    definidos = criterios_en_specs()
    usados = criterios_en_tests()
    orden = lambda c: (c[:2], int(c[2:]))
    if not definidos:
        print("✘ SPECS.md no tiene criterios de aceptación (CA1, CA2…) en la sección 'Criterios de aceptación'.")
        return 1
    sin_test = sorted(definidos - set(usados), key=orden)
    desconocidos = sorted(set(usados) - definidos - PROFESORADO, key=orden)
    for c in sorted(definidos, key=orden):
        print(f"{'✔' if c in usados else '✘'} {c}: {', '.join(sorted(set(usados.get(c, [])))) or 'SIN TEST'}")
    for c in desconocidos:
        print(f"✘ {c}: lo cita {', '.join(sorted(set(usados[c])))} pero no existe en SPECS.md")
    if sin_test or desconocidos:
        print(f"\n{len(sin_test)} criterio(s) sin test y {len(desconocidos)} referencia(s) desconocida(s).")
        return 1
    print(f"\nTodos los criterios ({len(definidos)}) tienen al menos un test.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
