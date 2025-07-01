from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="notify_specific_task",
    start_date=datetime(2025, 6, 27),
    schedule_interval=None,
    catchup=False,
) as dag:

    ok_task = BashOperator(
        task_id="ok_task",
        bash_command="echo OK"  # このタスクには通知しない
    )

    alert_task = BashOperator(
        task_id="alert_task",
        bash_command="exit 1",   # 故意に失敗させる
        email=["XXXXX@gmail.com"],        # ←宛先
        email_on_failure=True,               # ←失敗時のみ送信
        email_on_retry=False                 # リトライ時は不要なら False
    )

    ok_task >> alert_task