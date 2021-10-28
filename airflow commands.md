# airflow

 - pip install virtualenv
    - in case of a problem sudo apt-get install --reinstall python3-apt
 - virtualenv airflow-venv
 - source airflow-venv/bin/activate
 - export AIRFLOW_HOME=~/airflow
 - pip install apache-airflow

 - if needed - pip uninstall apache-airflow

 - nano airflow.cfg - edit the config file with the directory where your dags are.

    - airflow db init

    - airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org


 - airflow webserver -p 8080


 * in separate terminal

 - source airflow-venv/bin/activate
 - airflow scheduler