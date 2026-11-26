"""Transformaciones PySpark reutilizables para el caso Retail."""
from pyspark.sql import DataFrame, Window, functions as F


def to_typed_orders(df: DataFrame) -> DataFrame:
    """Convertir tipos antes de evaluar reglas de calidad."""
    return (df
        .withColumn("amount_eur", F.expr("try_cast(amount_eur as decimal(12,2))"))
        .withColumn("order_date", F.to_date("order_date"))
        .withColumn("updated_at", F.to_timestamp("updated_at")))


def to_valid_orders(df: DataFrame) -> DataFrame:
    """Excluir pedidos sin clave, fecha, actualización o importe válido."""
    return df.filter(
        F.col("order_id").isNotNull()
        & F.col("customer_id").isNotNull()
        & F.col("order_date").isNotNull()
        & F.col("updated_at").isNotNull()
        & F.col("amount_eur").isNotNull()
        & (F.col("amount_eur") >= 0)
    )


def latest_per_order(df: DataFrame) -> DataFrame:
    """Conservar la versión con updated_at más reciente de cada pedido."""
    w = Window.partitionBy("order_id").orderBy(F.col("updated_at").desc())
    return df.withColumn("_rn", F.row_number().over(w)).filter(F.col("_rn") == 1).drop("_rn")


def monthly_sales(df: DataFrame) -> DataFrame:
    """Producir ventas mensuales por cliente."""
    return (df.withColumn("order_month", F.date_trunc("month", "order_date").cast("date"))
        .groupBy("order_month", "customer_id")
        .agg(F.count("order_id").alias("order_count"),
             F.sum("amount_eur").alias("revenue_eur")))
