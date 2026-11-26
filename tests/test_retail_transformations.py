"""Ejecutar con pytest -q desde la raíz del proyecto."""
from decimal import Decimal
import pytest
from pyspark.sql import SparkSession
from src.retail_transformations import to_typed_orders, to_valid_orders, latest_per_order, monthly_sales

@pytest.fixture(scope="session")
def spark():
    session = SparkSession.builder.master("local[1]").appName("databricks-started").getOrCreate()
    yield session
    session.stop()

def test_cleaning_and_aggregation(spark):
    rows = [("1", "C1", "2026-01-02", "10.00", "2026-01-02T10:00:00"),
            ("1", "C1", "2026-01-02", "15.00", "2026-01-03T10:00:00"),
            ("2", "C2", "2026-01-02", "-1.00", "2026-01-02T10:00:00")]
    df = spark.createDataFrame(rows, ["order_id","customer_id","order_date","amount_eur","updated_at"])
    cleaned = latest_per_order(to_valid_orders(to_typed_orders(df)))
    assert cleaned.count() == 1
    assert monthly_sales(cleaned).first()["revenue_eur"] == Decimal("15.00")
