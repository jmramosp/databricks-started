# Ejercicios del proyecto Retail

## Principiante
1. Cuenta filas de Bronze y describe por qué `amount_eur` llega como string.
2. Obtén valores únicos de customer_id y registra nulos.
3. Muestra los importes ordenados de mayor a menor.

## Intermedio
4. Convierte el importe a DECIMAL sin romper ante INVALID.
5. Rechaza negativos y campos clave nulos. Cuenta rechazados y conserva evidencias.
6. Deduplica por order_id manteniendo la actualización más reciente.
7. Construye ventas por mes y cliente; comprueba el importe de la orden 1002.

## Avanzado
8. Define una política de desempate cuando updated_at es idéntico.
9. Diseña cambios incrementales con MERGE y considera un evento DELETE.
10. Añade pruebas de contrato y un diagrama de orquestación/observabilidad.

**Entrega:** notebook, explicación, tests y resultados esperados.
