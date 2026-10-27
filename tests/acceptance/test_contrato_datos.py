"""Contrato de datos fijado por el profesorado (criterios CD1-CD5 de AGENTS.md).

NO SE MODIFICA. Comprueba las salidas del pipeline, sea cual sea la arquitectura del equipo.
"""
import pandas as pd
import pytest

COLUMNAS = {
    "estaciones": {"estacion_id", "nombre", "latitud", "longitud", "altitud_m", "capacidad", "districte", "en_servicio"},
    "viajes": {"viaje_id", "abonado_id", "tipo_bici", "estacion_origen", "estacion_destino",
               "fecha_hora_inicio", "fecha_hora_fin", "duracion_min"},
    "estado": {"estacion_id", "fecha_hora", "bicis_mecanicas", "bicis_electricas", "anclajes_libres"},
}


def test_columnas_minimas(estaciones, viajes, estado):
    for nombre, df in (("estaciones", estaciones), ("viajes", viajes), ("estado", estado)):
        faltan = COLUMNAS[nombre] - set(df.columns)
        assert not faltan, f"{nombre}.parquet no tiene las columnas {sorted(faltan)}"


@pytest.mark.criterio("CD1")
def test_viaje_id_unico(viajes):
    assert viajes["viaje_id"].is_unique, "Hay viajes repetidos"


@pytest.mark.criterio("CD2")
def test_tipo_bici(viajes):
    tipos = set(viajes["tipo_bici"].unique())
    assert tipos <= {"electrica", "mecanica"}, f"Valores inesperados en tipo_bici: {tipos}"


@pytest.mark.criterio("CD3")
def test_fechas_y_duracion(viajes):
    assert pd.api.types.is_datetime64_any_dtype(viajes["fecha_hora_inicio"])
    assert pd.api.types.is_datetime64_any_dtype(viajes["fecha_hora_fin"])
    assert viajes["fecha_hora_fin"].notna().all(), "Hay viajes sin hora de fin"
    assert (viajes["duracion_min"] >= 1).all(), "Hay viajes de menos de 1 minuto o con duración negativa"


@pytest.mark.criterio("CD4")
def test_estaciones_existen(viajes, estaciones):
    catalogo = set(estaciones["estacion_id"])
    assert viajes["estacion_origen"].isin(catalogo).all(), "Hay estaciones de origen fuera del catálogo"
    assert viajes["estacion_destino"].isin(catalogo).all(), "Hay estaciones de destino fuera del catálogo"


@pytest.mark.criterio("CD5")
def test_ocupacion_posible(estado, estaciones):
    e = estado.drop(columns="capacidad", errors="ignore").merge(
        estaciones[["estacion_id", "capacidad"]], on="estacion_id", how="left")
    total = e["bicis_mecanicas"] + e["bicis_electricas"] + e["anclajes_libres"]
    assert (total <= e["capacidad"]).all(), "Hay lecturas con más bicis y anclajes que capacidad"
