# Tests de aceptación

- `test_contrato_datos.py` es del profesorado (criterios CD1–CD5 de `AGENTS.md`). **No se modifica.**
- El resto de ficheros los escribe el equipo: uno o más tests por cada criterio `CA…` de `SPECS.md` §6.
  Podéis organizarlos como queráis, por ejemplo `test_datos.py`, `test_metricas.py` y `test_cuadro_mando.py`.

Cada test se marca con el criterio que verifica, para que `scripts/trazabilidad.py` lo encuentre:

```python
import pytest


@pytest.mark.criterio("CA1")
def test_viaje_id_sin_repetir(viajes):
    assert viajes["viaje_id"].is_unique
```

Las *fixtures* `estaciones`, `viajes` y `estado` (en `tests/conftest.py`) leen los Parquet de `data/processed/`.
Si necesitáis otras tablas, añadid su *fixture* en `conftest.py`.

Para probar una métrica, mejor un ejemplo pequeño calculado a mano que los datos reales: así sabéis el resultado exacto.
Para probar la app sin navegador, `streamlit.testing.v1.AppTest`.
