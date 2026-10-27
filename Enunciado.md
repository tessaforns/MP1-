# Miniproyecto 1 · De CSV a dashboard (BiciBCN)

Oct 1, 2026 · @santi, @Eloi Puertas, @MireiaUB

## Contexto y encargo

En este miniproyecto, cada equipo construye en dos sesiones un panel en Streamlit que la dirección de operaciones de BiciBCN pueda usar en su reunión semanal.

**El servicio.** BiciBCN es el servicio de bicicleta compartida de Barcelona en este caso de estudio. Tiene 543 estaciones repartidas por los 10 distritos, unas 7.000 bicis en la calle (el 60 % eléctricas) y unos 168.000 abonados con tarifa anual.

**Qué es real y qué es simulado.** Las estaciones (ubicación, altitud, capacidad y barrio) son reales y proceden del feed público de Bicing. Todo lo demás, desde los viajes hasta los abonados, el estado de las estaciones y la meteorología, es simulado. Las cifras que obtengáis **no describen el servicio real de Bicing**.

**El encargo.** Este es el mensaje que la directora de operaciones, Aina Puig, ha enviado al equipo de datos:

> Cada lunes repasamos el servicio con informes sueltos que nadie mira. Necesito un panel que me diga, de un vistazo, cuánto se usa la bici, dónde y cuándo falla el servicio (estaciones sin bicis o sin sitio para dejarla), si las eléctricas están resolviendo el problema de las cuestas y si estamos llegando igual a todos los barrios. Tengo que poder filtrar por periodo y por distrito, y quiero ver un mapa. Y al final, decidme qué cambiaríais.

Los datos cubren de julio de 2025 a junio de 2026 y están exportados tal cual de varios sistemas. No están limpios: parte del trabajo es encontrar sus problemas y decidir cómo tratarlos.

## Preguntas de negocio

El panel tiene que responder, como mínimo, a las cuatro preguntas de la directora. Las subpreguntas son orientativas: podéis elegir otras si las justificáis.

1. **¿Cómo se usa el servicio?** Viajes por día y por hora, laborables frente a fines de semana, estacionalidad y efecto de la lluvia. ¿Crece el uso?
2. **¿Dónde y cuándo falla?** Estaciones que se quedan sin bicis o sin anclajes libres: cuáles, a qué horas y por qué. ¿Qué hacen los camiones de redistribución?
3. **¿Eléctrica o mecánica?** Qué parte de los viajes se hace en cada tipo, para qué recorridos y con qué tarifa.
4. **¿Llega a toda la ciudad?** Oferta y uso por distrito en relación con su población, y quién usa el servicio.

Y una quinta que no es un gráfico: **¿qué cambiaríais?** Vuestra presentación termina con una recomendación concreta.

## Cómo se trabaja y qué se entrega

En este miniproyecto **el código lo genera un agente de IA**. Vuestro trabajo es especificar, verificar y decidir. Cada equipo de 3 o 4 personas trabaja en un repositorio creado desde la plantilla `mp1-plantilla`, que gira en torno a seis ficheros:

| Fichero | Qué es | Quién lo escribe |
| --- | --- | --- |
| `AGENTS.md` | Reglas y comandos para el agente; lo lee al empezar cada conversación | Viene completo; podéis añadir reglas |
| `SPECS.md` | **Qué** construimos: objetivo, entradas, salidas, requisitos y criterios de aceptación | Equipo |
| `DESIGN.md` | **Cómo se ve y se comporta**: nombres, formatos, gráficos, pantallas, casos límite | Equipo |
| `ARCHITECTURE.md` | **Cómo está construido**: carpetas, módulos, flujo de datos | Equipo (el agente puede proponer) |
| `TASKS.md` | La lista de tareas, en pasos pequeños, con la verificación de cada una | El agente propone, el equipo aprueba y verifica |
| `README.md` | Para personas: cómo ejecutarlo, uso de IA y resumen para la dirección | Equipo |

**El ciclo de cada iteración**

1. Escribís o ampliáis `SPECS.md` y `DESIGN.md`.
2. Pedís al agente que **revise** la especificación y señale ambigüedades. Corregís.
3. Pedís al agente que genere los tests de aceptación en `tests/acceptance/`, uno o más por criterio, marcados con `@pytest.mark.criterio("CA…")`.
4. El agente propone las tareas en `TASKS.md` y vosotros las aprobáis.
5. El agente implementa **una** tarea. Verificáis (tests, lectura del *diff*, una cifra a mano) y completáis `Verificado por:`.
6. Si algo cambia, se cambia primero `SPECS.md` (sección "Decisiones") y después el código.



**Calendario**

| Sesión | Tramo | Min | Qué hacéis |
| --- | --- | --- | --- |
| 4 | Encargo | 15 | Presentación del caso y de la metodología . Equipos y repositorio desde la plantilla. |
| 4 | Concepto | 20 | Cómo escribir especificaciones. Demostración del ciclo con el agente sobre una tarea pequeña. |
| 4 | Trabajo en equipo | 70 | Explorar los datos, escribir las entradas, requisitos y criterios de datos de `SPECS.md`, sus tests y las primeras tareas con el agente. |
| 4-5 | Revisión cruzada | 15 | Otro equipo usa vuestro panel y lee vuestro `SPECS.md`. |
| 5 | Iteración | 70 | Incorporar los comentarios y pasar la checklist de calidad. Formalización de SPECS.md. y criterios de aceptación. |
| 5 | Presentaciones | 30  |
| 5 | Cierre | 10 |  |

**Hito de control al final de la sesión 4:** `SPECS.md` documenta al menos seis problemas de calidad con sus requisitos y criterios, el pipeline genera los ficheros Parquet y los tests CD1–CD5 pasan.

## Normas de trabajo

El agente escribe el código, pero sois responsables de todo lo que contiene vustro proyecto.

- **Cualquier agente vale**, siempre que siga `AGENTS.md`. Si vuestro agente no lo lee solo, pedidle al empezar que lo lea.
- **Una tarea cada vez.** Nada se marca como hecho en `TASKS.md` sin la línea `Verificado por:` de una persona que diga cómo lo comprobó.
- **El agente no toca `SPECS.md`, `DESIGN.md` ni `tests/acceptance/`.** Los cambios en esos ficheros pasan por una *pull request* aprobada por otra persona del equipo.
- **Nunca se cambia un test para que pase.** Si un test falla, primero se decide si el error está en el código o en la especificación.
- **Los datos originales no se tocan:** `data/raw/` es de solo lectura.
- **Ojo con la muestra.** `viajes.csv` contiene el 5 % de los viajes: los totales se escalan (× 20) y se indica que son una estimación.
- **Las cifras deben cuadrar** entre equipos. Si no coinciden, averiguad por qué y dejadlo en "Decisiones".

## Materiales

Todo lo que necesitáis está en este repositorio. 

**Repositorio plantilla** (`mp1-plantilla`): `AGENTS.md` completo; `SPECS.md`, `DESIGN.md`, `ARCHITECTURE.md` y `TASKS.md` con sus secciones vacías e indicaciones; los tests del contrato mínimo (CD1–CD5); el script de trazabilidad; la integración continua de GitHub y un notebook de exploración con pandas. Los datos se descargan con `uv run python scripts/descargar_datos.py`.

Más adelante podéis basaros en los skills de https://github.com/MireiaUB/Infovis2627/tree/main/skills como inspiración para reglas de diseño.
Si quieres usar mapas puedes pedir una API Key de CARTO en https://carto.com/basemaps/apikey/  La respuesta es immediata

**Fuentes de los datos reales:** ubicación, altitud y capacidad de las estaciones del feed GBFS de Bicing (consultado el 1 de octubre de 2026); barrios y distritos de CartoBCN (Ajuntament de Barcelona, CC-BY); población por distrito de 2021 ([Wikipedia](https://en.wikipedia.org/wiki/Districts_of_Barcelona)).
