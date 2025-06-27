from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("hello_dag", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    t1 = BashOperator(
        task_id="say_hello",
        bash_command="echo 'Hello, Airflow!'"
    )
