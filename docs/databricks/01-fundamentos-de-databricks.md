# DBX-01 — Fundamentos de Databricks

**Nivel:** Principiante · **Modalidad:** teoría, demostración, práctica y evaluación.

## Objetivos observables
Al terminar, podrás explicar los conceptos, aplicar al menos una transformación y verificar el resultado con una prueba reproducible.

## Contexto
Databricks combina procesamiento distribuido, almacenamiento tabular confiable y controles de acceso para entregar pipelines y productos analíticos.

## Vocabulario y conceptos
1. **Lakehouse** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
2. **Workspace** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
3. **Apache Spark** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
4. **separación cómputo y almacenamiento** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
5. **serverless** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.
6. **CSV, Parquet y Delta** — describe su propósito, cómo se aplica a un conjunto de órdenes y qué problema operativo o de rendimiento hay que prevenir.

## Ejemplo guiado
```sql
SELECT customer_id, COUNT(*) AS order_count,
       SUM(amount_eur) AS revenue_eur
FROM retail_orders_silver
WHERE amount_eur >= 0
GROUP BY customer_id
ORDER BY revenue_eur DESC;
```
_Nota: primero ejecuta el notebook para crear la tabla opcionalmente._

## Caso de estudio: ventas minoristas
Diferencia entre Apache Spark (motor de procesamiento) y Databricks (plataforma administrada).

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
