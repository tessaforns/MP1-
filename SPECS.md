# SPECS · Cuadro de mando BiciBCN

> **Qué construimos.** Lo escribe el equipo; el agente lo lee pero no lo edita.
> Las indicaciones entre `<!-- -->` son de la plantilla: borradlas cuando escribáis cada sección.

## 1. Objetivo

<!--
Una o dos frases: para quién es el cuadro de mando y qué decisiones le ayuda a tomar.
Pista: no es "ver datos", es decidir algo concreto. ¿Qué decidirá Aina Puig cada lunes?
-->

## 2. Usuarios y preguntas

<!--
- Usuario: quién lo usa, cuándo y qué sabe (¿es técnico? ¿cuánto tiempo tiene?).
- Preguntas: las del encargo, numeradas (P1, P2…) y concretadas. Cada pantalla del cuadro
  de mando responderá a una de ellas.
-->

## 3. Entradas

<!--
Los ficheros de data/raw/ y los problemas de calidad que encontréis con notebooks/exploracion.ipynb.
Sed concretos: cuántas filas, qué columna, qué valor raro y cuántas veces aparece.
Hito de la sesión 4: al menos seis problemas documentados.

Ejemplo de fila:
| `viajes.csv` (N filas) | Un viaje de la muestra del 5 % | N `viaje_id` repetidos; … |
-->

| Fichero | Una fila es | Problemas encontrados |
| --- | --- | --- |
| | | |

## 4. Salidas

<!--
Qué genera el pipeline en data/processed/ y qué muestra la app.
Como mínimo, las tres tablas del contrato de AGENTS.md §3. Añadid las columnas derivadas
o tablas extra que necesitéis para las métricas (p. ej. fecha, hora, laborable…).
-->
- `data/processed/estaciones.parquet`, `viajes.parquet` y `estado.parquet` con el contrato de `AGENTS.md`

## 5. Requisitos

<!--
Reglas numeradas (R1, R2…), cada una verificable y sin ambigüedad. Separadlas en bloques.
Cada problema de la sección 3 debería tener un requisito que diga qué se hace con él.

Ejemplos de forma:
- R1. Un viaje aparece una sola vez: si un viaje_id se repite, se conserva una fila.
- R7. Viajes por día laborable = viajes estimados en días laborables / número de días laborables. Laborable = …
-->

**Datos**

- R1. Un viaje es válido si sus estaciones de origen y destino existen en el catálogo, la bici se devolvió, aparece una sola vez y dura entre 1 y 180 minutos.
- R2. `tipo_bici` solo toma los valores `electrica` y `mecanica`.
- R3. Los viajes afectados por los cambios de hora se corrigen (+60 min el 26-oct-2025, −60 min el 29-mar-2026), no se eliminan.
- R4. Las estaciones con latitud y longitud intercambiadas se corrigen.
- R5. Una altitud de −999 significa "desconocida" y se guarda como nula.
- R6. El distrito de cada estación se toma de su barrio, no del código de distrito del feed.
- R7. Una estación con capacidad 0 o 1 está fuera de servicio.
- R8. Las lecturas de estado de estaciones cerradas no se usan.
- R9. Las lecturas con más bicis y anclajes que capacidad no se usan.
- R10. Una estación que repite exactamente la misma lectura más de 24 horas seguidas tiene el sensor bloqueado; esas lecturas no se usan.
- R11. En abonados, el año 1900 significa "desconocido" (nulo) y un género vacío es `no_indicado`.

**Métricas**

**Cuadro de mando**

## 6. Criterios de aceptación

<!--
Cada criterio (CA1, CA2…) dice qué requisito verifica y cómo se comprueba con una cifra o un hecho
concreto. Cada uno tendrá al menos un test en tests/acceptance/ marcado con
@pytest.mark.criterio("CA…"). scripts/trazabilidad.py lee los CA de esta sección.

Dos tipos útiles:
- Con los datos reales: "CA1 (R1). Tras limpiar, ningún viaje_id se repite."
- Con un ejemplo pequeño calculado a mano: "CA5 (R7). Con 3 viajes laborables en 2 días laborables,
  los viajes por día laborable son 30."

Lo que no se pueda testear (p. ej. si un gráfico se entiende) indicad cómo se verifica.
-->

**Datos** (`tests/acceptance/test_datos.py`, además de CD1–CD5)

- CA1 (R1). Ningún viaje dura más de 180 minutos.
- CA2 (R1). Tras limpiar quedan entre 750.000 y 760.000 viajes.
- CA3 (R3). La noche del 26-oct-2025 (de 1:00 a 3:00) se conservan al menos 30 viajes y todos duran entre 1 y 60 minutos.
- CA4 (R4). Todas las estaciones tienen latitud entre 41,30 y 41,50 y longitud entre 2,05 y 2,25.
- CA5 (R5). Ninguna altitud es negativa y exactamente 3 son nulas.
- CA6 (R6). La estación 13 está en Sant Martí y la 395 en Ciutat Vella.
- CA7 (R7). Las estaciones 245, 366 y 458 están fuera de servicio.
- CA8 (R8). No hay lecturas de la estación 509 entre el 20 de abril y el 31 de mayo de 2026 (cerrada por obras).
- CA9 (R10). No hay lecturas de la estación 120 del 3 al 9 de mayo de 2026.
- CA10 (R11). Ningún abonado tiene año 1900 ni género vacío.


## 7. Fuera de alcance

<!-- Lo que no vais a hacer, para que nadie (ni el agente) lo haga. -->

## 8. Preguntas abiertas

<!-- Dudas pendientes de decidir. Cuando se decidan, pasan a "Decisiones". -->

## 9. Decisiones

<!--
Una línea por decisión: fecha · qué se decide · requisitos afectados · por qué (con cifras si las hay).
Ejemplo:
- 2026-10-20 · Se conserva la primera aparición de cada viaje duplicado · R1 · Son copias exactas (N filas).
-->
