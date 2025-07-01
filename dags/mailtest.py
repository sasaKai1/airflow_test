from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time
import os, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Python callable ---------------------------------------------------------
def mailtest() -> None:
    SMTP_HOST = "email-smtp.ap-northeast-1.amazonaws.com"  # 利用リージョンで変える
    SMTP_PORT = 587
    SMTP_USER = "XXXXXX"
    SMTP_PASS = "XXXXXXXXX"
    msg            = MIMEMultipart()
    msg["Subject"] = "テスト: SES → Gmail"
    msg["From"]    = "XXXXXXX@gmail.com"
    msg["To"]      = "XXXXXXX@gmail.com"
    msg.attach(MIMEText("こんにちは。SES からのテストメールです。", "plain", "utf-8"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

# --- DAG definition ----------------------------------------------------------
default_args = {
    "owner": "airflow",
    "retries": 0,          # no automatic retries
}

with DAG(
    dag_id="mailtest_dag",
    description="Simple DAG: one task that sleeps for 3 minutes",
    default_args=default_args,
    start_date=datetime(2025, 7, 1),  # first run anchor (any past date OK)
    schedule_interval=None,            # run manually
    catchup=False,                     # don’t backfill
    tags=["example"],
) as dag:

    mailtest = PythonOperator(
        task_id="mailtest",
        python_callable=mailtest,
    )

# If you want to chain multiple tasks, use sleep_task >> next_task …etc.
