import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook

def debug_smtp():
    c = BaseHook.get_connection("smtp_default")
    print("★ host =", repr(c.host))
    print("★ port =", c.port, type(c.port))
    print("★ login =", c.login)
    print("★ disable_tls =", c.extra_dejson.get("disable_tls"))
    print("★ disable_ssl =", c.extra_dejson.get("disable_ssl"))

args = {
    "owner": "airflow",
    "start_date": airflow.utils.dates.days_ago(2),
    "provide_context": True,
}

with DAG(dag_id="test_ses_sendmail", default_args=args, schedule_interval=None) as dag:

    start = DummyOperator(task_id="start")

    debug = PythonOperator(task_id="debug", python_callable=debug_smtp)

    sendmail = EmailOperator(
        task_id="sendmail",
        to="XXXX@gmail.com",
        subject="SESTest",
        html_content="test",
        mime_charset="utf-8",
    )

    end = DummyOperator(task_id="end")

    start >> sendmail >> end