# 🚀 Radar Comercial IA B2B  
### Sistema inteligente de priorización de prospectos mediante Data Analytics e IA Generativa

## 📌 Descripción del proyecto

Las empresas suelen perder oportunidades comerciales debido a la falta de seguimiento, ausencia de criterios de priorización y procesos manuales en la gestión de prospectos.

Este proyecto propone una solución basada en análisis de datos e Inteligencia Artificial Generativa para ordenar el pipeline comercial, asignar prioridades y recomendar acciones comerciales.

El sistema integra un proceso ETL con Python, análisis de datos con Pandas, visualización ejecutiva mediante Power BI y un agente de IA desarrollado con Gemini Gems.

---

# 🎯 Objetivo

Diseñar un agente comercial de IA capaz de analizar prospectos B2B mediante reglas de negocio previamente definidas.

El agente es capaz de:

- Evaluar información del prospecto.
- Detectar datos faltantes.
- Calcular un scoring comercial de 0 a 100.
- Clasificar oportunidades en categorías A, B, C y D.
- Identificar riesgos de enfriamiento.
- Detectar objeciones comerciales.
- Recomendar la siguiente acción comercial.
- Generar mensajes profesionales de seguimiento.
- Crear un resumen ejecutivo para Dirección.

> **Nota:** El agente no toma decisiones comerciales finales. Todas sus recomendaciones requieren validación humana.

---

# 🛠️ Tecnologías utilizadas

<p align="left">
  <img src="https://skillicons.dev/icons?i=python" />
</p>

- Python
- Pandas
- Excel / CSV
- Power BI
- Gemini Gems
- Prompt Engineering
- ETL (Extract, Transform, Load)

---

# 🏗️ Arquitectura de la solución

<p align="center">
  <img src="arquitectura/radar_comercial_arquitectura.png" width="900"/>
</p>

La arquitectura sigue el siguiente flujo:

```
Base de prospectos (Excel/CSV)
              ↓
      ETL con Python y Pandas
              ↓
        Dataset procesado
              ↓
      ┌─────────────────┐
      ↓                 ↓
 Radar Comercial IA   Dashboard Power BI
      ↓
Validación humana
      ↓
Acción comercial
```

---

# 📂 Estructura del proyecto

```
Radar-Comercial-IA-B2B/
│
├── base_datos/
│   └── prospectos.csv
│
├── scripts/
│   └── scoring_prospectos.py
│
├── procesados_dash/
│   ├── prospectos_scoring.csv
│   ├── dashboard.pbix
│   └── dashboard.png
│
├── agente_IA/
│   └── prompt_maestro.md
│
├── documentacion/
│   ├── documento_ejecutivo.pdf
│   └── desarrollo_completo.pdf
│
├── presentacion/
│   ├── Radar_Comercial_IA_B2B.pptx
│   └── Radar_Comercial_IA_B2B.pdf
│
└── README.md
```

---

# 📊 Dashboard ejecutivo

El dashboard permite visualizar indicadores clave para Dirección Comercial:

- Número de prospectos por categoría A, B, C y D.
- Monto potencial por prioridad.
- Prospectos con riesgo de enfriamiento.
- Oportunidades sin seguimiento reciente.
- Distribución de oportunidades por responsable.
- Alertas comerciales.

<p align="center">
  <img src="procesados_dash/dashboard.png" width="900"/>
</p>

---

# ⚙️ Flujo de trabajo

1. El usuario carga la base de prospectos en formato Excel/CSV.
2. Python realiza el proceso ETL:
   - Limpieza de datos.
   - Estandarización de variables.
   - Aplicación de reglas comerciales.
   - Cálculo del scoring.
3. Se genera una nueva base de datos con clasificación A/B/C/D.
4. Power BI consume los datos procesados y genera indicadores ejecutivos.
5. El usuario envía un prospecto al agente Radar Comercial IA.
6. Gemini Gems analiza el caso y propone recomendaciones comerciales.
7. Un responsable humano valida la recomendación antes de actuar.

---

# 🧪 Pruebas realizadas

El agente fue evaluado utilizando cinco escenarios comerciales:

- Prospecto categoría A (alta prioridad).
- Prospecto categoría B (seguimiento activo).
- Prospecto categoría C (nutrición comercial).
- Prospecto categoría D (posible descarte).
- Prospecto con información incompleta.

Los resultados demostraron que el agente puede aplicar las reglas comerciales definidas, detectar información faltante y proponer acciones concretas.

---

# 📈 Resultados obtenidos

- Automatización del scoring comercial mediante Python.
- Clasificación automática de prospectos utilizando criterios de negocio.
- Creación de un dashboard ejecutivo para toma de decisiones.
- Desarrollo de un prototipo funcional de agente comercial utilizando Gemini Gems.
- Generación automática de mensajes comerciales adaptados a cada escenario.
- Incorporación de validación humana como mecanismo de control.

---

# 🧠 Aprendizajes del proyecto

Durante este desarrollo se aplicaron conocimientos relacionados con:

- Procesos ETL utilizando Python y Pandas.
- Limpieza y transformación de datos comerciales.
- Diseño de dashboards ejecutivos con Power BI.
- Construcción de agentes de IA mediante Prompt Engineering.
- Integración entre datos, reglas de negocio e Inteligencia Artificial Generativa.
- Diseño de soluciones de análisis de datos orientadas al negocio.

---

# 🚀 Futuras mejoras

Las siguientes etapas permitirían evolucionar el sistema hacia una solución empresarial más robusta:

- Integración con CRM (HubSpot, Salesforce, Zoho, etc.).
- Automatización de procesos mediante n8n o Zapier.
- Conexión con APIs de modelos de IA.
- Orquestación del pipeline mediante Apache Airflow.
- Almacenamiento de información en bases de datos relacionales como PostgreSQL.
- Incorporación de métricas históricas de conversión y desempeño comercial.

---

# 👤 Autor

Proyecto desarrollado por **[Tu nombre]** como caso de estudio de Data Analytics, Business Intelligence e Inteligencia Artificial aplicada a procesos comerciales B2B.
