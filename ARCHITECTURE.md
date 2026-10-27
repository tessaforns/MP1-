# ARCHITECTURE · Cuadro de mando BiciBCN

> **Cómo está construido.** Lo escribe el equipo. El agente puede proponer cambios, pero no aplicarlos sin aprobación.
> Las indicaciones entre `<!-- -->` son de la plantilla: borradlas cuando escribáis cada sección.

## 1. Flujo de datos

<!--
Un esquema de cómo pasan los datos de data/raw/*.csv a data/processed/*.parquet y de ahí al
cuadro de mando. Indicad qué módulo hace cada paso y qué requisitos de SPECS cubre.

Lo fijo (AGENTS.md §3): `uv run python -m src.pipeline` escribe los Parquet y
`uv run streamlit run src/app.py` arranca la app.
-->

## 2. Carpetas

| Carpeta | Qué contiene |
| --- | --- |
| `src/` | Todo el código del proyecto |
| `tests/acceptance/` | Tests de los criterios de SPECS (los escribe el equipo) y del contrato del profesorado |
| `tests/unit/` | Tests unitarios (los puede escribir el agente) |
| `data/raw/` | CSV descargados. Solo lectura |
| `data/processed/` | Parquet generados por el pipeline. No van a Git |
| `notebooks/` | Exploración. Importan de `src/`; nunca al revés |
| `scripts/` | Descarga de datos y comprobación de trazabilidad |

## 3. Módulos y responsabilidades

<!--
Qué módulos tendrá src/ y qué hace (y qué NO hace) cada uno. Separar responsabilidades
facilita testear y explicar el código en la defensa individual.
Preguntas útiles: ¿dónde se limpia? ¿dónde se calculan los KPIs? ¿la app calcula o solo muestra?
-->

| Módulo | Hace | No hace |
| --- | --- | --- |
| `pipeline.py` | | |
| `app.py` | | |

## 4. Dependencias

<!--
Instaladas en pyproject.toml: pandas, pyarrow, polars, duckdb, plotly, streamlit y pytest.
Decid cuáles usa src/ y para qué. Las nuevas se añaden con `uv add` y se justifican aquí.
-->

| Librería | Para qué |
| --- | --- |
| | |

## 5. Rendimiento

<!-- Casi dos millones de filas: ¿qué se calcula una vez y qué en cada clic? ¿Qué se cachea? -->

## 6. Qué está protegido

El agente no modifica: `SPECS.md`, `DESIGN.md`, `tests/acceptance/`, `data/raw/` ni este fichero sin aprobación (CODEOWNERS exige la revisión de otro miembro del equipo).
