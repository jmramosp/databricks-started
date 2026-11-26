# PYSP-05 — Agregaciones y joins

**Nivel:** Intermedio · **Modalidad:** teoría, demostración, práctica y evaluación.

## Objetivos observables
Al terminar, podrás explicar los conceptos, aplicar al menos una transformación y verificar el resultado con una prueba reproducible.

## Contexto
PySpark es la API de Python de Apache Spark. Las transformaciones de DataFrames describen un plan distribuido que Spark optimiza y ejecuta cuando corresponde.

## Vocabulario y conceptos
1. **groupBy** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
2. **agg** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
3. **countDistinct** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
4. **inner** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
5. **left** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
6. **anti** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
7. **cardinalidad** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
8. **duplicación** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.

## Ejemplo guiado
```python
from pyspark.sql import functions as F

orders = spark.createDataFrame(
    [("1001", "C001", 120.5), ("1002", "C002", 89.99)],
    ["order_id", "customer_id", "amount_eur"]
)
result = (orders.filter(F.col("amount_eur") >= 0)
    .groupBy("customer_id")
    .agg(F.sum("amount_eur").alias("revenue_eur")))
result.show()
```
_Resultado esperado: C001=120.5; C002=89.99._

## Caso de estudio: ventas minoristas
Haz un left join de órdenes con clientes y valida recuentos antes/después.

Trabaja con `order_id`, `customer_id`, `order_date`, `amount_eur` y `updated_at`. Define la granularidad, comprueba los tipos, detecta duplicados y explica por qué las reglas de negocio importan antes de agregar ventas.

## Práctica graduada
1. Describe cinco términos de la sección con tus propias palabras y un ejemplo real.
2. Ejecuta el ejemplo y registra esquema, recuento y una muestra del resultado.
3. Modifica un dato para provocar un error y crea una validación para detectarlo.
4. Explica cómo cambiaría la solución con cien millones de registros.
5. Documenta una decisión técnica con riesgo, alternativa y criterio de aceptación.

## Preguntas de entrevista
- ¿Qué garantías ofrece esta transformación y cuáles no?
- ¿Cómo distinguirías un fallo de datos de un fallo de infraestructura?
- ¿Qué medirías para demostrar corrección y rendimiento?

## Evidencia para aprobar
Entrega código o SQL, captura o tabla de resultados, dos verificaciones automatizables y una explicación breve de diseño.

**Referencias oficiales:** [Databricks](https://docs.databricks.com/aws/en/getting-started) · [PySpark](https://spark.apache.org/docs/latest/api/python/).
