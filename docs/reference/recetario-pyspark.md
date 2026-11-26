# Recetario rápido PySpark

```python
from pyspark.sql import functions as F, Window

# Columnas
selected = df.select("order_id", "amount_eur")
valid = df.filter(F.col("amount_eur") >= 0)
casted = df.withColumn("amount_eur", F.col("amount_eur").cast("decimal(12,2)"))

# Nulos
clean = df.filter(F.col("customer_id").isNotNull())

# Agregaciones
agg = df.groupBy("customer_id").agg(F.sum("amount_eur").alias("revenue_eur"))

# Último registro por clave
w = Window.partitionBy("order_id").orderBy(F.col("updated_at").desc())
latest = df.withColumn("_rn", F.row_number().over(w)).filter("_rn = 1").drop("_rn")

# Left anti: registros sin coincidencia
orphans = fact_df.join(dim_df, on="customer_id", how="left_anti")

# Inspección
latest.printSchema()
latest.explain()
```

Evita `collect()` sobre datos grandes; verifica cardinalidad al realizar joins y prefiere funciones integradas frente a Python UDF cuando sea posible.
