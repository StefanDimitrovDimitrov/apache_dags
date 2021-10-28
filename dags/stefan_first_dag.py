from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 26, 10),
    'email': ['airflow@example'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'spotify_dog',
    default_args=default_args,
    description='Our first DAG with ETL process',
    schedule_interval=timedelta(days=1),
)


def just_a_function():
    print("This is your first running DAG")


run_etl = PythonOperator(
    task_id='whole_spotify_etl',
    python_callable=just_a_function,
    dag=dag,
)

run_etl
