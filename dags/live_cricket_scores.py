from datetime import timedelta

# The dags object; we'll need this to instantiate a dags
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['stefan.dimitrov.dimitrov@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag = DAG(
    'live_cricket_scores',
    default_args=default_args,
    description="First example to get Live Cricket Scores",
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='print',
    bash_command='echo Getting Live Cricket Score!!!',
    dag=dag,
)

t2 = BashOperator(
    task_id='get_cricket_scores',
    bash_command='cricket scores',
    dag=dag,
)

t1 >> t2

