from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("flow1", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    t1 = BashOperator(task_id="start", bash_command="echo start")
    t2 = BashOperator(task_id="middle", bash_command="echo middle")
    t3 = BashOperator(task_id="end", bash_command="echo end")
    t1 >> t2 >> t3
