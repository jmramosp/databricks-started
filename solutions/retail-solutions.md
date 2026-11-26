# Soluciones razonadas — Retail

1. Bronze contiene **8 filas**: retener fuente original permite auditoría.
2. Validar `customer_id IS NOT NULL`; hay una fila sin cliente.
3. Ordenar usando importe convertido, no string: `orderBy(F.col("amount_eur").desc())` después del cast.
4. `F.expr("try_cast(amount_eur as decimal(12,2))")` convierte INVALID en null.
5. Tres órdenes inválidas: 1004 (negativo), 1005 (importe inválido), 1006 (cliente nulo).
6. `Window.partitionBy("order_id").orderBy(F.col("updated_at").desc())` y `row_number=1`.
7. Silver contiene cuatro órdenes únicas (1001, 1002, 1003, 1007); 1002 queda con 99.99 EUR; total Silver 515.49 EUR.
8. Añade secuencia de origen o ingestion_id y define prioridad determinista.
9. En producción, considera claves, ordering, duplicaciones y borrados; no trates el overwrite docente como incremental.
10. Testea tipos, claves, sumas, filas rechazadas y consistencia antes/después de joins.

Ver `notebooks/01_retail_pipeline.py` y `tests/test_retail_transformations.py`.
