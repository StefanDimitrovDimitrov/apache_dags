import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "start_date": airflow.utils.dates.days_ago(1)
}

with DAG(
        dag_id="slave_dag",
        default_args=default_args,
        schedule_interval="*/ 5 * * * *",
        catchup=False
)as dag:
    t1 = BashOperator(task_id="t1", bash_command="ehcho 'test'")

    t1
