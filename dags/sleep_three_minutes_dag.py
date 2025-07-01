from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time



# --- Python callable ---------------------------------------------------------
def sleep_three_minutes() -> None:
    """Pause for 180 seconds."""
    print("sleep start") 
    time.sleep(180)
    print("sleep end") 


# --- DAG definition ----------------------------------------------------------
default_args = {
    "owner": "airflow",
    "retries": 0,          # no automatic retries
}

with DAG(
    dag_id="sleep_three_minutes_dag",
    description="Simple DAG: one task that sleeps for 3 minutes",
    default_args=default_args,
    start_date=datetime(2025, 7, 1),  # first run anchor (any past date OK)
    schedule_interval=None,            # run manually
    catchup=False,                     # don’t backfill
    tags=["example"],
) as dag:

    sleep_task = PythonOperator(
        task_id="sleep_180_seconds",
        python_callable=sleep_three_minutes,
    )

# If you want to chain multiple tasks, use sleep_task >> next_task …etc.
