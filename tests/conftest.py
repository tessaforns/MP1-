"""Fixtures compartidas: las salidas del pipeline en data/processed/ (contrato de AGENTS.md §3)."""
from pathlib import Path

import pandas as pd
import pytest

PROCESADOS = Path(__file__).resolve().parent.parent / "data" / "processed"


def _leer(nombre: str) -> pd.DataFrame:
    ruta = PROCESADOS / f"{nombre}.parquet"
    if not ruta.exists():
        pytest.fail(f"No existe {ruta.relative_to(PROCESADOS.parent.parent)}. "
                    "Ejecuta antes `uv run python -m src.pipeline`.", pytrace=False)
    return pd.read_parquet(ruta)


@pytest.fixture(scope="session")
def estaciones() -> pd.DataFrame:
    return _leer("estaciones")


@pytest.fixture(scope="session")
def viajes() -> pd.DataFrame:
    return _leer("viajes")


@pytest.fixture(scope="session")
def estado() -> pd.DataFrame:
    return _leer("estado")


# Si vuestros tests necesitan otras tablas de data/processed/, añadid aquí su fixture:
#
# @pytest.fixture(scope="session")
# def abonados() -> pd.DataFrame:
#     return _leer("abonados")
