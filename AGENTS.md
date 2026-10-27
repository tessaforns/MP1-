# AGENTS.md

Instrucciones para cualquier asistente o agente de IA que trabaje en este repositorio. **Léelas al empezar cada conversación y síguelas siempre.**

El proyecto es un cuadro de mando de operaciones para BiciBCN, un servicio de bicicleta compartida de Barcelona. Las estaciones son reales; los viajes y el resto de datos son simulados.

## 1. Antes de hacer nada

Lee, en este orden:

1. `SPECS.md`: **qué** construimos (objetivo, entradas, salidas, requisitos y criterios de aceptación).
2. `DESIGN.md`: **cómo se ve y se comporta** (nombres, formatos, gráficos, pantallas).
3. `ARCHITECTURE.md`: **cómo está construido** (carpetas, módulos, flujo de datos).
4. `TASKS.md`: **qué toca ahora**. Trabajas en la primera tarea sin marcar, salvo que una persona te indique otra.

Si alguno de esos ficheros está vacío o le falta lo necesario para la tarea, **no lo supongas**: dilo y pregunta.

## 2. Comandos

| Para | Comando |
| --- | --- |
| Instalar el entorno | `uv sync` |
| Descargar los datos a `data/raw/` | `uv run python scripts/descargar_datos.py` |
| Generar los datos limpios en `data/processed/` | `uv run python -m src.pipeline` |
| Ejecutar los tests | `uv run pytest` |
| Comprobar que cada criterio tiene su test | `uv run python scripts/trazabilidad.py` |
| Arrancar el cuadro de mando | `uv run streamlit run src/app.py` |
| Añadir una librería | `uv add <libreria>` (y explica por qué hace falta) |

## 3. Contrato fijado por el profesorado

Esto no se negocia. Todo lo demás lo decide el equipo en `SPECS.md`, `DESIGN.md` y `ARCHITECTURE.md`.

1. `uv run python -m src.pipeline` lee `data/raw/` y escribe, como mínimo, estos ficheros con estas columnas:

   | Fichero | Columnas mínimas |
   | --- | --- |
   | `data/processed/estaciones.parquet` | `estacion_id`, `nombre`, `latitud`, `longitud`, `altitud_m`, `capacidad`, `districte`, `en_servicio` |
   | `data/processed/viajes.parquet` | `viaje_id`, `abonado_id`, `tipo_bici`, `estacion_origen`, `estacion_destino`, `fecha_hora_inicio`, `fecha_hora_fin`, `duracion_min` |
   | `data/processed/estado.parquet` | `estacion_id`, `fecha_hora`, `bicis_mecanicas`, `bicis_electricas`, `anclajes_libres` |

2. `uv run streamlit run src/app.py` arranca el cuadro de mando.
3. Cuando el pipeline ya genere las tablas finales limpias, deben pasar los tests de `tests/acceptance/test_contrato_datos.py` (criterios **CD1 a CD5**):

   | Criterio | Qué comprueba |
   | --- | --- |
   | CD1 | `viaje_id` es único en `viajes.parquet` |
   | CD2 | `tipo_bici` solo toma los valores `electrica` y `mecanica` |
   | CD3 | Las fechas son fechas, ningún viaje termina sin fecha y todos duran al menos 1 minuto |
   | CD4 | Las estaciones de origen y destino de los viajes existen en `estaciones.parquet` |
   | CD5 | En `estado.parquet`, bicis + anclajes libres nunca supera la capacidad de la estación |

## 4. Cómo trabajas

1. **Una tarea cada vez.** Antes de escribir código, resume la tarea, di qué requisitos (`R…`) y criterios (`CA…`) cubre y qué ficheros vas a tocar. Espera confirmación si la tarea es grande o ambigua.
2. **Implementa lo mínimo** que pide la tarea, respetando `ARCHITECTURE.md` y `DESIGN.md`.
3. **Verifica según el alcance de la tarea:**
   - Ejecuta las pruebas unitarias y de aceptación que correspondan a la tarea actual.
   - Ejecuta `uv run python -m src.pipeline` si has tocado el pipeline o la limpieza de datos.
   - Ejecuta `uv run pytest` y `uv run python scripts/trazabilidad.py` al completar todas las tareas, o antes si todas las dependencias de esas pruebas ya están implementadas.
   - Si una prueba todavía no aplica porque depende de una tarea posterior, no la cambies ni la marques como fallo de la tarea actual; explica esa limitación y deja la verificación global para cuando se cumpla su prerrequisito.
4. **Actualiza `TASKS.md`:** marca la tarea con `[x]` solo si pasan todas las pruebas aplicables a esa tarea, y añade debajo una línea `Agente:` con qué hiciste y cómo lo comprobaste. Deja la línea `Verificado por:` para que la complete una persona.
5. **Para.** No empieces la siguiente tarea hasta que te lo pidan.

## 5. Lo que nunca haces

- **Nunca modificas** `tests/acceptance/`, `SPECS.md` ni `DESIGN.md`. Si crees que están mal o que se contradicen, explícalo y para: lo decide el equipo.
- **Nunca cambias un test para que pase.** Si un test falla, el problema está en el código, salvo que el equipo diga otra cosa.
- **Nunca inventas columnas, valores ni datos.** El esquema de entrada está en `SPECS.md` y en los propios CSV de `data/raw/`.
- **Nunca modificas `data/raw/`.** Es de solo lectura.
- **Nunca escribes resultados a mano** en el código (cifras fijas para que cuadre un KPI o un test).
- **Nunca añades dependencias** sin decirlo y sin usar `uv add`.
- **Nunca te sales de la tarea:** si ves otro problema, apúntalo en tu respuesta, pero no lo arregles por tu cuenta.

## 6. Estilo de código

- Python con pandas. Funciones pequeñas, con *type hints* y sin efectos secundarios ocultos.
- Nombres de variables, funciones y columnas en castellano y en `snake_case`.
- El *docstring* de cada función cita el requisito que implementa, por ejemplo `"""Excluye viajes sin devolver (R3)."""`.
- Los tests unitarios que escribas van en `tests/unit/`. Si un test verifica un criterio de aceptación, márcalo con `@pytest.mark.criterio("CA…")`.

## 7. Datos: lo que debes saber

- `data/raw/viajes.csv` es una **muestra aleatoria del 5 %** de los viajes. Los totales de viajes se multiplican por 20; las medias y los porcentajes, no.
- Los ficheros de `data/raw/` tienen errores. Encontrarlos y decidir qué hacer con ellos es trabajo del equipo y queda escrito en `SPECS.md`. Si al implementar ves datos raros que `SPECS.md` no trata, avisa.
- `estado_estaciones.csv` solo cubre de abril a junio de 2026.

## 8. Notas técnicas

- Streamlit ejecuta `src/app.py` como script. Para que `app.py` pueda importar otros módulos de `src/`, añade la raíz del proyecto a `sys.path` al principio de `app.py`.
- Lee y escribe tablas intermedias en Parquet, no en CSV: son casi dos millones de filas.

## 9. Terminado significa

- La tarea está implementada y respeta `SPECS.md`, `DESIGN.md` y `ARCHITECTURE.md`.
- Pasan las pruebas aplicables a la tarea y `uv run python scripts/trazabilidad.py` cuando sus criterios ya estén cubiertos.
- Al completar todas las tareas, pasan `uv run pytest` y `uv run python scripts/trazabilidad.py`.
- `TASKS.md` está actualizado con la línea `Agente:`.
- No se ha tocado nada fuera del alcance de la tarea.
