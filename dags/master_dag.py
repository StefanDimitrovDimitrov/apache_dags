import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "start_date": airflow.utils.dates.days_ago(1)
}

with DAG(
        dag_id="master_dag",
        default_args=default_args,
        schedule_interval="*/ 5 * * * *",
        catchup=False
)as dag:
    sensor = ExternalTaskSensor(
        task_id='sensor',
        external_dag_id='sensor_dag',
        external_task_id='t1'
    )

    last_task = DummyOperator(task_id='last_task')

    sensor >> last_task
