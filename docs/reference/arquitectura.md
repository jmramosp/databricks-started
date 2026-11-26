# Arquitectura de referencia — Retail

```text
Fuentes CSV / eventos / APIs
            ↓
Ingesta con trazabilidad
            ↓
Delta Bronze (datos originales)
            ↓
Silver (tipos, calidad, deduplicación)
            ↓
Gold (métricas / modelos dimensionales)
            ↓
Databricks SQL / Power BI
```

## Contrato de datos
`order_id` identifica una orden; `customer_id` cliente; `order_date` fecha de negocio; `amount_eur` importe; `updated_at` hora de actualización. Definir UTC vs hora local en sistemas reales.

## Controles
Validar esquema, duplicados, importes negativos, nulos, calidad y métricas. Separar datos rechazados para su auditoría.

## Producción
Reemplazar overwrite del demo por ingestión incremental, gestión de cambios, monitoreo, reintentos, permisos mínimos y CI/CD.
