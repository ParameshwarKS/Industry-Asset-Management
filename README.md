# ML-Based Predictive Asset Management – Asset Health Scoring

This project leverages Machine Learning to score the health of industrial assets using data collected from various sources. The health score helps optimize maintenance strategies and supports data-driven decision-making.

## 🛠️ Problem Statement

Industrial machinery downtime and inefficient maintenance can lead to significant losses. To mitigate this, we aim to develop a predictive system that:

- Aggregates data from multiple sources (e.g., sensors, logs, historical maintenance data).
- Computes a comprehensive **Asset Health Score** for each machine.
- Uses the score to **prioritize maintenance activities**.
- Enables **informed decisions** about asset utilization and lifecycle management.

## 🔍 Key Features

- 📥 **Data Ingestion**: Supports structured and unstructured sensor and operational data.
- 🧠 **ML Modeling**: Applies predictive models to assess asset health.
- 📊 **Scoring System**: Outputs intuitive health scores that quantify machinery condition.
- 📅 **Maintenance Planning**: Helps schedule preventive maintenance using insights from the score.

## 🧾 Use Cases

- Predictive maintenance scheduling
- Failure risk assessment
- Budget and resource optimization
- Lifecycle asset management
---
## 📦 Data Source & Description

📌 **Source**: [Microsoft Azure Predictive Maintenance Dataset](https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance)

This dataset is an example data source suitable for building a **Predictive Maintenance Model**. It includes information on:

### 🔍 Details

- ⚙️ **Machine Conditions & Usage**  
  Operational data collected from machine sensors.

- ❌ **Failure History**  
  Past failure events at the component or system level.

- 🧰 **Maintenance History**  
  Logs of maintenance events, component replacements, and error codes.

- 🏷️ **Machine Features**  
  Static metadata like model number, engine type, location, and size.

---

## 🧬 Data Schema

Below is the schema representing how the tables relate to each other:

![Data Schema](https://github.com/user-attachments/assets/7aafa0de-1340-47ea-99e9-653631e3ce9c)

🧠 This schema shows how sensor data, maintenance logs, machine specifications, and failure events are interconnected for use in a predictive maintenance pipeline.

---

✅ Use this schema to:
- Build an ETL pipeline
- Feed data into ML models (SageMaker, Forecast, etc.)
- Visualize data lineage and design system monitoring
---

## 🏗️ Solution & Architecture

This project is built on AWS services for scalable, predictive asset health scoring. The system follows a 6-step architecture using AWS's data and ML tools to forecast the condition of industrial assets and trigger alerts when necessary.

<img width="1355" height="846" alt="image" src="https://github.com/user-attachments/assets/520fd126-6018-4825-9d63-60286e645332" />

---

### 🔢 1. Data Integration and Storage
**Services Used:** `AWS RDS`

- Ingests data from various sources: sensors, equipment logs, maintenance records, inspection reports, environmental data.
- Stores structured data in **AWS RDS**.

---

### 🔄 2. ETL Process
**Service Used:** `AWS Glue`

- Performs ETL (Extract, Transform, Load) operations on raw data.
- Cleans, normalizes, and transforms the data for model consumption.
- Reloads transformed data into **AWS S3**.

---

### 🧠 3. Data Processing and Model Training
**Service Used:** `AWS SageMaker`

- Preprocesses the data and performs feature engineering.
- Builds the **Health Scoring Model** using ML algorithms.
- Using Random Forest Classifier the probability of machine failure is predicted and 100*(1-P(machine failure)) would be the health score of that machine.
- Validates and tunes the model iteratively.

---

### 📈 4. Time Series Forecasting of Health Score
**Services Used:** `AWS SageMaker`

- Predicts future health scores based on historical data trends.
- Uses time series models like **SARIMAX**
- This feature is not yet build but would be added in the future
- Enables proactive maintenance and failure prevention.

---

### 📊 5. Visualization and Reporting
**Service Used:** `AWS QuickSight`

- Builds dashboards to show asset health trends, current scores, and alerts.
- Provides **real-time insights** and **historical analysis**.
- Allows users to monitor performance visually and intuitively.

---

### 🚨 6. Monitoring and Notifications
**Services Used:** `AWS CloudWatch`, `AWS SNS`

- Uses **CloudWatch** to define custom alarms based on asset health thresholds.
- Sends real-time alerts via **email/SMS/notifications** using **SNS**.
- Supports fast responses to degrading equipment conditions.

---

## 🧰 Tools Used

- **AWS Aurora**: Data warehouse for structured asset data.
- **AWS Lambda**: Trigger data loads.
- **AWS Glue**: Serverless ETL pipeline.
- **AWS SageMaker**: ML model training and deployment, Time series prediction.
- **AWS QuickSight**: BI and visualization.
- **AWS CloudWatch & SNS**: Monitoring and alerting.

  <img width="1559" height="860" alt="image" src="https://github.com/user-attachments/assets/75082a4f-701b-49d8-be3c-6f625498d17c" />


---

## 📌 Outcome

This pipeline allows industrial teams to:
- Monitor asset health in near real-time.
- Forecast equipment degradation.
- Reduce unplanned downtime.
- Make smarter maintenance and investment decisions.


