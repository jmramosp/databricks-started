# Databricks notebook source
# MAGIC %md
# MAGIC # Retail: Bronze → Silver → Gold
# MAGIC Notebook de aprendizaje. Los datos se construyen en memoria y la escritura de tablas Delta es opcional.

# COMMAND ----------
from pyspark.sql import Window, functions as F
from pyspark.sql.types import StructType, StructField, StringType

# COMMAND ----------
# MAGIC %md
# MAGIC ## Bronze: datos fuente

# COMMAND ----------
rows = [
    ("1001", "C001", "2026-01-02", "120.50", "2026-01-02T10:00:00"),
    ("1002", "C002", "2026-01-02", "89.99", "2026-01-02T11:00:00"),
    ("1003", "C001", "2026-01-05", "45.00", "2026-01-05T10:00:00"),
    ("1002", "C002", "2026-01-02", "99.99", "2026-01-03T11:00:00"),
    ("1004", "C003", "2026-02-03", "-15.00", "2026-02-03T10:00:00"),
    ("1005", "C003", "2026-02-04", "INVALID", "2026-02-04T11:00:00"),
    ("1006", None, "2026-02-05", "40.00", "2026-02-05T11:00:00"),
    ("1007", "C004", "2026-02-06", "250.00", "2026-02-06T14:00:00")
]
schema = StructType([StructField(c, StringType(), True) for c in
    ["order_id", "customer_id", "order_date", "amount_eur", "updated_at"]])
bronze_df = spark.createDataFrame(rows, schema)
assert bronze_df.count() == 8

# COMMAND ----------
# MAGIC %md
# MAGIC ## Silver: tipos, reglas y versión más reciente

# COMMAND ----------
typed = (bronze_df
    .withColumn("order_date", F.to_date("order_date"))
    .withColumn("updated_at", F.to_timestamp("updated_at"))
    .withColumn("amount_eur", F.expr("try_cast(amount_eur as decimal(12,2))")))
valid = typed.filter(
    F.col("order_id").isNotNull() & F.col("customer_id").isNotNull()
    & F.col("order_date").isNotNull() & F.col("updated_at").isNotNull()
    & F.col("amount_eur").isNotNull() & (F.col("amount_eur") >= 0))
w = Window.partitionBy("order_id").orderBy(F.col("updated_at").desc())
silver_df = valid.withColumn("_rn", F.row_number().over(w)).filter("_rn = 1").drop("_rn")
assert silver_df.count() == 4

# COMMAND ----------
# MAGIC %md
# MAGIC ## Gold: KPIs agregados

# COMMAND ----------
gold_df = (silver_df
    .withColumn("order_month", F.date_trunc("month", "order_date").cast("date"))
    .groupBy("order_month", "customer_id")
    .agg(F.count("order_id").alias("order_count"),
         F.sum("amount_eur").alias("revenue_eur")))
gold_df.orderBy("order_month", "customer_id").show(truncate=False)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Escritura Delta (opcional)
# MAGIC Revisa el catálogo y esquema disponibles antes de descomentar. Overwrite solo en este demo.

# COMMAND ----------
# bronze_df.write.format("delta").mode("overwrite").saveAsTable("retail_orders_bronze")
# silver_df.write.format("delta").mode("overwrite").saveAsTable("retail_orders_silver")
# gold_df.write.format("delta").mode("overwrite").saveAsTable("retail_sales_gold")
