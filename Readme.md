🏗 Airflow ETL Project – Sales Data Pipeline

This is a fully local ETL pipeline using Apache Airflow that extracts, transforms, and loads sales data into a SQLite database.

##################################################################
Project Overview

This project demonstrates a classic ETL workflow:

Extract – Read raw CSV file from data/.

Transform – Clean, enrich, and aggregate sales data with Pandas.

Load – Persist results into a SQLite database for analytics.

###########################################################################################

Project Structure

airflow_etl_project/
│
├── dags/
│   └── etl_sales_dag.py        # Airflow DAG definition
│
├── data/
│   └── raw_sales.csv           # Sample raw sales data
│
├── scripts/
│   ├── extract.py              # Extract task
│   ├── transform.py            # Transform task
│   └── load.py                 # Load task
│
├── output/                     # Pipeline outputs (created at runtime)
│   ├── extracted.csv
│   ├── processed_sales.csv
│   └── sales.db
│
└── requirements.txt
###########################################################################################

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
