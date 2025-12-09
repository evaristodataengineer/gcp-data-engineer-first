from airflow import DAG
from airflow.providers.google.cloud.operators.dataflow import DataflowTemplatedJobStartOperator
from datetime import datetime

default_args = {
    'owner': 'data-engineer',
    'start_date': datetime(2025, 9, 12),
    'retries': 1
}

dag = DAG(
    'wordcount_dataflow',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
)

dataflow_task = DataflowTemplatedJobStartOperator(
    task_id='ejecutar_wordcount',
    template='gs://us-central1-mi-entorno-comp-3badcdf0-bucket/templates/wordcount_template',
    location='us-central1',
    project_id='e-gcp-data-engineer',
    dag=dag,
)
