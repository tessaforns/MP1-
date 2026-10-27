# Cuadro de mando BiciBCN

**Equipo:** <!-- nombres y usuarios de GitHub -->

Miniproyecto 1 del posgrado. Cuadro de mando de operaciones para BiciBCN, el servicio de bicicleta compartida de Barcelona de este caso de estudio.

> **Datos simulados.** Las estaciones (ubicación, altitud, capacidad y barrio) son reales y proceden del feed público de Bicing. Los viajes, el estado de las estaciones, los abonados, la redistribución y la meteorología son simulados y no reflejan el funcionamiento real de Bicing.

## Cómo se trabaja en este proyecto

El código lo genera un agente de IA a partir de lo que escribe el equipo. Vuestro trabajo es **especificar, verificar y decidir**.

| Fichero | Qué es | Quién lo escribe |
| --- | --- | --- |
| `AGENTS.md` | Reglas y comandos para el agente | Profesorado (podéis añadir reglas) |
| `SPECS.md` | Qué construimos: objetivo, entradas, salidas, requisitos y criterios de aceptación | Equipo |
| `DESIGN.md` | Cómo se ve y se comporta | Equipo |
| `ARCHITECTURE.md` | Cómo está construido: carpetas, módulos, flujo de datos | Equipo (el agente puede proponer) |
| `TASKS.md` | Lista de tareas en pasos pequeños | El agente propone, el equipo aprueba |
| `README.md` | Este fichero, para personas | Equipo |


## Puesta en marcha

```bash
uv sync
uv run python scripts/descargar_datos.py    # datos a data/raw/
```


### El ciclo de cada iteración:

1. Escribid o ampliad `SPECS.md` y `DESIGN.md`.
2. Pedid al agente que **revise** la spec y señale ambigüedades. Corregid.
3. Pedid al agente que genere los tests de aceptación en `tests/acceptance/`, marcados con `@pytest.mark.criterio("CA…")`.
4. Pedid al agente que proponga las tareas en `TASKS.md`. Aprobadlas.
5. El agente implementa **una** tarea. Vosotros verificáis y completáis `Verificado por:`.
6. Si algo cambia, se cambia primero `SPECS.md` (sección "Decisiones") y después el código.

### Una vez que el pipeline y `SPECS.md` existan, podéis ejecutar todo el proyecto con: 

```bash 
uv run python -m src.pipeline               # cuando exista: datos limpios a data/processed/
uv run pytest                               # tests
uv run python scripts/trazabilidad.py       # ¿cada criterio tiene su test?
uv run streamlit run src/app.py             # cuadro de mando
```

Al empezar, `src/` está vacío: los tests del contrato (CD1–CD5) y la trazabilidad fallan hasta que el pipeline y `SPECS.md` existan. Es lo esperado.

Cada *push* ejecuta todo lo anterior en GitHub (pestaña **Actions**).

## Uso de IA

<!-- Qué agente habéis usado, cómo lo habéis guiado y qué habéis tenido que corregir. -->

## Resumen para la dirección de operaciones

<!--
Una página, para Aina Puig. Sin jerga técnica y con cifras.

**La situación.** Una o dos frases con lo esencial.

**Hallazgos**
1. …
2. …
3. …

**Recomendación.** Qué cambiaríais, concreta, y con qué indicador se mediría.

**Qué no dicen estos datos.** Las limitaciones que debe conocer antes de decidir.
-->
