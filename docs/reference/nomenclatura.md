# Estándares de nomenclatura

- Variables y funciones Python: `snake_case`; clases: `PascalCase`; constantes: `UPPER_SNAKE_CASE`.
- Tablas: `<dominio>_<entidad>_<capa>`, por ejemplo `retail_orders_silver`.
- Columnas: `order_id`, `order_date`, `amount_eur`, `updated_at`; incluye moneda/unidad cuando corresponda.
- Catálogos y esquemas: separar ambientes (`dev`, `test`, `prod`) según política del equipo.
- Archivos: prefijo numerado y nombre descriptivo; notebooks con propósito y capa.
- Usar `from pyspark.sql import functions as F`; evitar imports wildcard.
- Documentar claves, zona horaria, granularidad, nullabilidad, fuente y frecuencia.
- Nunca poner contraseñas o tokens en notebooks o GitHub.

## Terminología actual
Databricks Jobs se presenta bajo Lakeflow Jobs; la documentación también usa Lakeflow Declarative Pipelines y Declarative Automation Bundles. Revisar cambios de nombres en https://docs.databricks.com/aws/en/resources/product-name-changes.
