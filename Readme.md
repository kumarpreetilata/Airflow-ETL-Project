# Automated ETL Pipeline for Customer Sales Data 📊

**Extract, Transform & Load with Airflow**

Process customer sales data daily—compute key metrics, aggregate spend, and load into a **SQLite database**—fully automated with **Airflow** DAGs, logging, and retry mechanisms. ⚡️

---

## Features
- **Extract:** Reads raw sales CSV files and standardizes them for processing.
- **Transform:** Computes order-level **total value** and aggregates customer spend.
- **Load:** Inserts transformed data into a **SQLite database** for analytics.
- **Airflow Orchestration:** DAGs with task dependencies, daily scheduling, retries, and monitoring.
- **Modular & Maintainable:** Separate scripts for **extract**, **transform**, and **load**.
- **Logging & Observability:** Tracks task execution, success/failure, and retries.

---

## Tech Stack
- **Python** (ETL scripts, data manipulation)
- **Pandas**
- **SQLite**
- **Apache Airflow**
- **BashOperator** (task execution)
- **Logging**

---

## Quick Start 🚀
1️⃣ **Place raw CSV**
```bash
data/raw_sales.csv

Setup Instruction

git clone https://github.com/<your-username>/airflow-etl-project.git
cd airflow-etl-project



py -3.11 -m venv venv
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install "apache-airflow==2.7.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.11.txt"
pip install pandas
airflow db init
airflow users create --username admin --firstname Preeti --lastname Kumar --role Admin --email admin@example.com --password YourPassword123
airflow webserver --port 8080
airflow scheduler (separate terminal)
#irflow standalone
