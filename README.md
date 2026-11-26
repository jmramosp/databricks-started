# Databricks Started — Curso integral en español

> Ruta autodidacta: **Databricks (14 módulos)** + **PySpark (12 módulos)**, desde cero hasta diseño de pipelines de producción. Creado para aprendizaje y portafolio; no es un curso oficial de Databricks.

## Objetivo
Aprender Databricks como plataforma Lakehouse y PySpark como motor de transformación distribuida. Trabajaremos con un caso consistente de ventas minoristas e implementaremos **Bronze → Silver → Gold** con calidad, modelado, pruebas y recomendaciones de despliegue.

## Cómo estudiar
1. Lee `docs/00-guia-de-estudio.md` y `docs/reference/nomenclatura.md`.
2. Completa los módulos `docs/databricks/` y `docs/pyspark/` por orden.
3. Ejecuta `notebooks/01_retail_pipeline.py` en Databricks tras elegir catálogo y esquema autorizados.
4. Resuelve `exercises/retail-challenges.md` sin mirar `solutions/retail-solutions.md`.
5. Revisa `docs/reference/arquitectura.md` y `docs/reference/glosario.md` para entrevistas.

## Contenidos Databricks
- [01. Fundamentos de Databricks](docs/databricks/01-fundamentos-de-databricks.md) — Principiante
- [02. Primeros pasos y entorno](docs/databricks/02-primeros-pasos-y-entorno.md) — Principiante
- [03. Arquitectura y gobierno de datos](docs/databricks/03-arquitectura-y-gobierno-de-datos.md) — Principiante
- [04. Databricks SQL](docs/databricks/04-databricks-sql.md) — Principiante
- [05. Ingesta de datos](docs/databricks/05-ingesta-de-datos.md) — Intermedio
- [06. Delta Lake](docs/databricks/06-delta-lake.md) — Intermedio
- [07. Medallion y calidad](docs/databricks/07-medallion-y-calidad.md) — Intermedio
- [08. Modelado analítico](docs/databricks/08-modelado-analitico.md) — Intermedio
- [09. Orquestación y Lakeflow](docs/databricks/09-orquestacion-y-lakeflow.md) — Intermedio
- [10. Structured Streaming](docs/databricks/10-structured-streaming.md) — Avanzado
- [11. Optimización de Spark](docs/databricks/11-optimizacion-de-spark.md) — Avanzado
- [12. Ingeniería de software y CI/CD](docs/databricks/12-ingenieria-de-software-y-ci/cd.md) — Avanzado
- [13. Seguridad y operación](docs/databricks/13-seguridad-y-operacion.md) — Avanzado
- [14. Casos avanzados de plataforma](docs/databricks/14-casos-avanzados-de-plataforma.md) — Avanzado

## Contenidos PySpark
- 01. Python esencial
- 02. Fundamentos de Spark
- 03. DataFrame API
- 04. Funciones integradas y nulls
- 05. Agregaciones y joins
- 06. Window functions
- 07. Schemas y datos anidados
- 08. Lectura y escritura
- 09. Testing y calidad
- 10. Rendimiento PySpark
- 11. Streaming con PySpark
- 12. Patrones avanzados — consulta `docs/pyspark/`.

## Estructura
- `docs/`: teoría, ejemplos, casos, preguntas y referencias.
- `notebooks/`: notebook de práctica compatible con el formato source de Databricks.
- `data/`: datos simulados, sin PII real.
- `src/`: transformaciones reutilizables.
- `tests/`: pruebas unitarias opcionales para entorno con PySpark instalado.
- `exercises/` y `solutions/`: ejercicios y soluciones.

## Restricciones y versiones
Free Edition proporciona serverless con cuotas y limitaciones. Algunas funciones de administración, infraestructura, conectores o costes pueden variar por nube, edición y permisos. No pegues tokens ni contraseñas en el repositorio. La documentación de nombres de producto cambia; revisa `docs/reference/nomenclatura.md`.

## Recursos oficiales
- [Introducción a Databricks](https://docs.databricks.com/aws/en/getting-started)
- [Conceptos de Databricks](https://docs.databricks.com/aws/en/getting-started/concepts)
- [Documentación PySpark](https://spark.apache.org/docs/latest/api/python/)
- [Guía de Spark SQL](https://spark.apache.org/docs/latest/sql-programming-guide)
- [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html)
- [Terminología actualizada](https://docs.databricks.com/aws/en/resources/product-name-changes)

## Progreso
Usa `docs/00-guia-de-estudio.md` como checklist. La ruta completa tiene teoría, ejemplos guiados y actividades; los ejercicios avanzados de operación requieren acceso a las funciones correspondientes del workspace.