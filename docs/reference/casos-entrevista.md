# Casos de entrevista técnica

## Caso 1: pedidos duplicados
**Situación:** un `order_id` aparece varias veces con distinto `updated_at`.
**Solución esperada:** define clave y desempate, usa `row_number`, prueba valor final y justifica la política.

## Caso 2: join que multiplica filas
**Situación:** una tabla de clientes tiene duplicados por clave.
**Solución esperada:** comprueba granularidad, unicidad y cardinalidad antes de unir.

## Caso 3: pipeline lento
**Situación:** cientos de GB y join de gran tamaño.
**Solución esperada:** inspecciona `explain`, shuffle, skew, particiones, tamaño de dimensiones y AQE.

## Caso 4: CDC
**Situación:** fuente emite insert/update/delete.
**Solución esperada:** compara marca de tiempo, orden de eventos, claves y semántica de `MERGE`.

## Caso 5: acceso a métricas
**Situación:** BI debe leer Gold sin modificar Silver.
**Solución esperada:** mínimo privilegio y grants de Unity Catalog por catálogo/esquema/tabla.

## Criterios de respuesta
Explica supuestos, alternativas, fallos típicos, observabilidad, estrategia de tests y costes.
