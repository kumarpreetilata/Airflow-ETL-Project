from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

with DAG(
    "etl_sales_dag",
    default_args={
        "owner": "preeti",
        "depends_on_past": False,
        "email_on_failure": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=2),
    },
    description="Simple ETL pipeline with Airflow",
    schedule_interval="@daily",
    start_date=datetime(2025, 9, 19),
    catchup=False,
    tags=["etl", "sales"],
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command=f"python3 {BASE_DIR}/scripts/extract.py {BASE_DIR}/data/raw_sales.csv {BASE_DIR}/output/extracted.csv",
    )

    transform = BashOperator(
        task_id="transform",
        bash_command=f"python3 {BASE_DIR}/scripts/transform.py {BASE_DIR}/output/extracted.csv {BASE_DIR}/output/processed_sales.csv",
    )

    load = BashOperator(
        task_id="load",
        bash_command=f"python3 {BASE_DIR}/scripts/load.py {BASE_DIR}/output/processed_sales.csv {BASE_DIR}/output/sales.db",
    )

    extract >> transform >> load
