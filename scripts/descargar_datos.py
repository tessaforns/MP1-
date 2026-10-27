"""Descarga los datos del miniproyecto a data/raw/.

    uv run python scripts/descargar_datos.py
"""
import urllib.request
import zipfile
from pathlib import Path

URL = "https://github.com/DataScienceUB/mp1-plantilla/releases/download/Datos2026_0.1/bicibcn.zip"
DESTINO = Path(__file__).resolve().parent.parent / "data" / "raw"

if any(DESTINO.glob("*.csv")):
    print("Los datos ya están en data/raw/")
else:
    zip_local = DESTINO / "bicibcn.zip"
    print(f"Descargando {URL} …")
    urllib.request.urlretrieve(URL, zip_local)
    with zipfile.ZipFile(zip_local) as z:
        z.extractall(DESTINO)
    zip_local.unlink()
    print("Listo:", ", ".join(sorted(p.name for p in DESTINO.glob("*.csv"))))
