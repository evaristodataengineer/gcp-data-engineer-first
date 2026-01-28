<div align="center">

# 🚀 Google Cloud Platform - Portfolio de Data Engineering

[![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?style=for-the-badge&logo=google-bigquery&logoColor=white)](https://cloud.google.com/bigquery)
[![Dataflow](https://img.shields.io/badge/Dataflow-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/dataflow)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Apache Beam](https://img.shields.io/badge/Apache_Beam-FF6600?style=for-the-badge&logo=apache&logoColor=white)](https://beam.apache.org/)

### 📊 Portafolio completo de proyectos con Google Cloud Platform para demostrar competencias como Data Engineer

*Una colección integral de proyectos prácticos que demuestran dominio en el ecosistema de GCP, desde ingesta y transformación de datos hasta arquitecturas avanzadas de Data Mesh y ML*

[Ver Proyectos](#-proyectos) • [Tecnologías](#-stack-tecnológico) • [Contacto](#-contacto)

---

</div>

## 🎯 Sobre este Repositorio

Este repositorio contiene una **suite completa de proyectos** desarrollados con **Google Cloud Platform**, diseñados para demostrar habilidades profesionales en **Ingeniería de Datos**. Cada carpeta representa un área específica del ecosistema GCP, con implementaciones reales y casos de uso empresariales.

### 💡 ¿Por qué este repositorio?

- ✅ **Experiencia práctica** con servicios clave de GCP
- ✅ **Casos de uso reales** aplicables a entornos de producción
- ✅ **Mejores prácticas** en arquitectura de datos en la nube
- ✅ **Código documentado** y reutilizable
- ✅ **Enfoque en empleabilidad** como Data Engineer

---

## 🛠 Stack Tecnológico

<table>
<tr>
<td align="center" width="25%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" width="60" height="60" />
<br><b>Google Cloud</b>
</td>
<td align="center" width="25%">
<img src="https://www.vectorlogo.zone/logos/apache_beam/apache_beam-icon.svg" width="60" height="60" />
<br><b>Apache Beam</b>
</td>
<td align="center" width="25%">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" height="60" />
<br><b>Python</b>
</td>
<td align="center" width="25%">
<img src="https://www.vectorlogo.zone/logos/apache_airflow/apache_airflow-icon.svg" width="60" height="60" />
<br><b>Apache Airflow</b>
</td>
</tr>
</table>

### Servicios de GCP Utilizados:
- **BigQuery** - Almacenamiento y análisis de datos a escala masiva
- **Cloud Storage** - Almacenamiento de objetos y Data Lake
- **Dataflow** - Procesamiento de datos en streaming y batch con Apache Beam
- **Cloud Composer** - Orquestación de flujos de trabajo con Apache Airflow
- **Dataplex** - Gestión unificada de datos y Data Mesh
- **Cloud SQL** - Bases de datos relacionales gestionadas
- **Dataproc** - Clusters de Spark/Hadoop gestionados
- **Cloud Monitoring** - Observabilidad y troubleshooting

---

## 📂 Proyectos

### 1️⃣ **BigQuery - Analytics & Data Warehousing** 
📁 [`Big-Query/`](./Big-Query) | [`Bigquery-model/`](./Bigquery-model)

Implementación de un Data Warehouse moderno con BigQuery, desde consultas básicas hasta modelos de datos complejos.

**Características:**
- 🔍 Consultas sobre datasets públicos de BigQuery
- 📊 Diseño de esquemas de datos (users, orders)
- 🎯 Vistas desnormalizadas para analytics
- 💾 Inserción y gestión de datos
- 🔗 Joins y agregaciones optimizadas

**Tecnologías:** BigQuery, SQL, Python SDK

**Casos de uso:**
- Análisis de e-commerce
- Reporting de ventas
- KPIs de negocio

```sql
-- Ejemplo: Vista desnormalizada para análisis
CREATE OR REPLACE VIEW ecommerce_dataset.denormalized_view AS
SELECT
    o.user_id, o.order_id, o.product, o.price,
    u.name, u.email
FROM ecommerce_dataset.orders o
JOIN ecommerce_dataset.users u
ON o.user_id = u.user_id;
```

---

### 2️⃣ **Cloud Storage - Object Storage & Data Lake**
📁 [`Cloud-storage/`](./Cloud-storage) | [`Changes/`](./Changes)

Gestión programática de Cloud Storage para la creación de Data Lakes y almacenamiento escalable.

**Características:**
- 🪣 Creación automática de buckets
- 📤 Upload/Download de archivos
- 🔧 Configuración de permisos y lifecycle policies
- 📊 Integración con BigQuery para datos externos
- 🔄 Procesamiento de archivos CSV

**Tecnologías:** Cloud Storage, Python SDK

**Casos de uso:**
- Almacenamiento de datos raw
- Archivado de logs
- Data Lakes multi-zona

```python
# Ejemplo: Creación de bucket con configuración
def create_bucket(bucket_name, location="US"):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    client.create_bucket(bucket, location=location)
    print(f"🟩 Bucket creado: {bucket.name}")
```

---

### 3️⃣ **Dataflow - Stream & Batch Processing**
📁 [`dataflow/`](./dataflow)

Pipelines de procesamiento de datos usando Apache Beam en Google Dataflow para transformaciones ETL a escala.

**Características:**
- 🌊 Procesamiento batch con Apache Beam
- 📝 Pipeline WordCount clásico
- ☁️ Ejecución en Dataflow Runner
- 🎯 Transformaciones PTransform
- 💾 Escritura a Cloud Storage

**Tecnologías:** Apache Beam, Dataflow, Python

**Casos de uso:**
- ETL de archivos de texto
- Procesamiento de logs
- Análisis de datos no estructurados

```python
# Pipeline de procesamiento con Apache Beam
with beam.Pipeline(options=options) as p:
    (
        p
        | "Leer archivo" >> beam.io.ReadFromText("gs://input/data.txt")
        | "Separar palabras" >> beam.FlatMap(lambda line: line.split())
        | "Contar palabras" >> beam.combiners.Count.PerElement()
        | "Guardar resultados" >> beam.io.WriteToText("gs://output/wordcount")
    )
```

---

### 4️⃣ **Cloud Composer - Workflow Orchestration**
📁 [`Composer/`](./Composer) | [`composer_dags/`](./composer_dags)

Orquestación de flujos de trabajo complejos usando Cloud Composer (Apache Airflow managed).

**Características:**
- 🔄 DAGs de Airflow para orquestación
- 🚀 Integración con Dataflow Templates
- ⏰ Scheduling y retries
- 📊 Monitoreo de ejecuciones
- 🔗 Operadores de GCP

**Tecnologías:** Cloud Composer, Apache Airflow, Dataflow

**Casos de uso:**
- ETL programados
- Pipelines de ML
- Orquestación multi-servicio

```python
# DAG de Airflow para ejecutar Dataflow
dataflow_task = DataflowTemplatedJobStartOperator(
    task_id='ejecutar_wordcount',
    template='gs://bucket/templates/wordcount_template',
    location='us-central1',
    project_id='mi-proyecto',
    dag=dag,
)
```

---

### 5️⃣ **Datalake - External Tables & Lakehouse**
📁 [`Datalake/`](./Datalake)

Implementación de un Data Lake moderno con tablas externas en BigQuery apuntando a Cloud Storage.

**Características:**
- 🏗️ Arquitectura Lakehouse (Storage + BigQuery)
- 📁 Tablas externas sobre CSV en GCS
- 🔍 Consultas SQL sobre archivos raw
- 🚀 Separación de storage y compute
- 💰 Optimización de costos

**Tecnologías:** BigQuery, Cloud Storage, Bash

**Casos de uso:**
- Query directo sobre archivos
- Data Lake analytics
- Reducción de costos de almacenamiento

---

### 6️⃣ **Data Mesh - Decentralized Architecture**
📁 [`datamesh/`](./datamesh)

Implementación de una arquitectura Data Mesh usando Dataplex para dominios de datos descentralizados.

**Características:**
- 🏛️ Creación de Data Lakes con Dataplex
- 🌐 Zonas de datos por dominio (ventas, marketing, logística)
- 🔗 Assets vinculados a Cloud Storage
- 📦 Automatización con Python SDK
- 🎯 Domain-driven data ownership

**Tecnologías:** Dataplex, Cloud Storage, Python

**Casos de uso:**
- Arquitecturas Data Mesh empresariales
- Gestión federada de datos
- Data governance distribuido

```python
# Crear zona de datos en Dataplex
def create_zone(project_id, region, lake_name, domain, bucket_name):
    client = dataplex_v1.DataplexServiceClient()
    zone = dataplex_v1.Zone()
    zone.display_name = f"{domain.capitalize()} Zone"
    zone.type_ = dataplex_v1.Zone.Type.RAW
    # ... configuración y creación
```

---

### 7️⃣ **Analysis Preparation - Materialized Views**
📁 [`analysis_preparation/`](./analysis_preparation)

Preparación de datos para análisis con vistas materializadas y agregaciones pre-computadas.

**Características:**
- 📊 Materialized Views en BigQuery
- ⚡ Agregaciones diarias y semanales
- 🔄 Refresh automático
- 💹 KPIs pre-calculados
- 🎯 Optimización de queries analíticas

**Tecnologías:** BigQuery, SQL

**Casos de uso:**
- Dashboards de BI
- Reportes ejecutivos
- Analytics en tiempo real

```sql
-- Vista materializada para agregaciones diarias
CREATE MATERIALIZED VIEW ecommerce_analysis.orders_daily_mv AS
SELECT
  DATE(order_date) AS order_day,
  COUNT(order_id) AS total_orders,
  SUM(price) AS total_revenue
FROM ecommerce_analysis.orders_raw
GROUP BY order_day;
```

---

### 8️⃣ **ML Preparation - Feature Engineering**
📁 [`ml_prep/`](./ml_prep)

Preparación de datos para Machine Learning con transformaciones de features y exploración de datos.

**Características:**
- 🤖 Feature engineering en BigQuery
- 🔍 Queries de exploración de datos
- 📈 Creación de variables derivadas
- 🎯 Preparación para BigQuery ML
- 📊 Análisis estadístico

**Tecnologías:** BigQuery, SQL

**Casos de uso:**
- Preparación de datasets para ML
- Feature stores
- Análisis exploratorio de datos

---

### 9️⃣ **Optimization - Performance & Cost**
📁 [`optimization/`](./optimization)

Técnicas de optimización para mejorar el rendimiento y reducir costos en GCP.

**Características:**
- 🔧 Particionamiento de tablas en BigQuery
- 💰 Clusters bajo demanda con Dataproc
- ⚡ Query optimization
- 📊 Análisis de costos
- 🎯 Reservations y slots

**Tecnologías:** BigQuery, Dataproc, Bash

**Casos de uso:**
- Reducción de costos de queries
- Optimización de pipelines
- Mejora de tiempos de respuesta

---

### 🔟 **Fault Tolerance - High Availability**
📁 [`fault_tolerance/`](./fault_tolerance)

Implementación de estrategias de tolerancia a fallos y alta disponibilidad.

**Características:**
- 🌍 Multi-region en BigQuery
- 🔄 Replicación de Cloud SQL
- 💪 Dataflow resiliente
- 🛡️ Backup y disaster recovery
- 📊 Monitoreo de failover

**Tecnologías:** BigQuery, Cloud SQL, Dataflow, Bash

**Casos de uso:**
- Continuidad de negocio
- Sistemas críticos 24/7
- Disaster recovery

---

### 1️⃣1️⃣ **Monitoring & Troubleshooting**
📁 [`monitoring_troubleshooting/`](./monitoring_troubleshooting)

Observabilidad y diagnóstico de sistemas de datos en GCP.

**Características:**
- 📊 Dashboards de Cloud Monitoring
- 🔍 Logs y métricas
- 🚨 Alertas automatizadas
- 📈 Visualización de KPIs
- 🛠️ Troubleshooting proactivo

**Tecnologías:** Cloud Monitoring, Cloud Logging

**Casos de uso:**
- Monitoreo de pipelines
- Alertas de SLA
- Performance monitoring

---

### 1️⃣2️⃣ **Workload Organization - Resource Management**
📁 [`workload_organizate/`](./workload_organizate)

Organización y gestión de cargas de trabajo con reservations y slot management.

**Características:**
- 📅 BigQuery reservations
- 🎯 Slot assignment
- 💼 Gestión de recursos
- 📊 Optimización de workloads
- 💰 Control de costos por equipo

**Tecnologías:** BigQuery, Bash

**Casos de uso:**
- Multi-tenancy
- Control presupuestario
- Aislamiento de workloads

---

### 1️⃣3️⃣ **Data Sharing - Cross-Organization**
📁 [`sharing_data/`](./sharing_data)

Compartir datos de forma segura entre proyectos y organizaciones.

**Características:**
- 🔐 Authorized views
- 🌐 Cross-project queries
- 👥 IAM y permisos granulares
- 📊 Analytics Hub
- 🔗 Data sharing controlado

**Tecnologías:** BigQuery, IAM

**Casos de uso:**
- Data marketplace
- Colaboración entre equipos
- Data monetization

---

## 🎓 Competencias Demostradas

Este portafolio demuestra competencia profesional en:

### 🏗️ **Arquitectura de Datos**
- Diseño de Data Lakes y Data Warehouses
- Implementación de arquitecturas Data Mesh
- Lakehouse híbridos (Storage + Compute)

### ⚙️ **Ingeniería de Datos**
- Pipelines ETL/ELT escalables
- Stream y batch processing
- Orquestación de workflows

### 📊 **Analytics Engineering**
- Modelado de datos dimensional
- Vistas materializadas y agregaciones
- Optimización de queries

### 🔧 **DevOps & Infraestructura**
- Infrastructure as Code
- Automatización con Python
- CI/CD de pipelines de datos

### 💰 **Optimización & Costos**
- Performance tuning
- Cost optimization strategies
- Resource management

### 🛡️ **Reliability & Security**
- Fault tolerance
- High availability
- Data governance

---

## 🚀 Cómo Ejecutar los Proyectos

### Prerrequisitos

1. **Cuenta de Google Cloud Platform** con proyecto activo
2. **gcloud CLI** instalado y configurado
3. **Python 3.8+** instalado
4. **Permisos** adecuados en GCP (BigQuery Admin, Storage Admin, etc.)

### Configuración Inicial

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/gcp-data-engineer-first.git
cd gcp-data-engineer-first

# 2. Autenticarse en GCP
gcloud auth login
gcloud config set project TU-PROJECT-ID

# 3. Instalar dependencias de Python
pip install google-cloud-bigquery google-cloud-storage apache-beam[gcp]

# 4. Configurar variables de entorno
export PROJECT_ID="tu-project-id"
export REGION="us-central1"
```

### Ejecutar Proyectos Específicos

Cada carpeta contiene scripts ejecutables. Ejemplos:

```bash
# BigQuery - Consultar dataset público
python Big-Query/public_dataset_demo.py

# Cloud Storage - Crear bucket
python Cloud-storage/create_bucket_script.py

# Dataflow - Ejecutar pipeline
python dataflow/pipeline_wordcount.py

# Datamesh - Crear arquitectura
python datamesh/create_zones_new.py \
  --project_id mi-proyecto \
  --region us-central1 \
  --lake retail-lake \
  --domains ventas marketing
```

---

## 📈 Próximos Pasos

Este repositorio está en **evolución continua**. Futuras adiciones incluirán:

- [ ] **BigQuery ML** - Modelos de ML directamente en BigQuery
- [ ] **Pub/Sub + Dataflow** - Streaming en tiempo real
- [ ] **dbt (data build tool)** - Transformaciones declarativas
- [ ] **Terraform** - Infrastructure as Code
- [ ] **CI/CD con Cloud Build** - Automatización completa

---

## 📞 Contacto

**Evaristo - Data Engineer**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/evaristo-sandoval-gil-86a6a0291/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/evaristodataengineer)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:evaristodataengineer@gmail.com)

> 💼 **En búsqueda activa de oportunidades como Data Engineer**


<div align="center">

### ⭐ Si este repositorio te resulta útil, considera darle una estrella

**Hecho con ❤️ para la comunidad de Data Engineering**

</div>



