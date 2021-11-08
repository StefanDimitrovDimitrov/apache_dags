import datetime

from airflow import models
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time()
)

default_dag_args = {
    'start_date': yesterday,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=2)
}

with models.DAG(
        'dag_dummy_operator',
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:
    def greeting():
        print('Greetings form SpikeySales! Happy shopping.')
        return 'Greeting successfully printed.'


    python_greeting = PythonOperator(
        task_id='hello_python',
        python_callable=greeting
    )

    bash_greeting = BashOperator(
        task_id='bye_bash',
        bash_command='echo Goodbye! Hope to see you soon.',
    )

    end = DummyOperator(
        task_id='dummy'
    )

    python_greeting >> bash_greeting >> end
