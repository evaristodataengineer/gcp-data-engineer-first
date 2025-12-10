



gcloud composer environments create my-composer-env --location=us-central1 --image-version=composer-2.7.4-airflow-2.7.3 --zone=us-central1-a



gcloud composer environments storage dags import --environment mi-entorno-composer --location us-central1 --source dag.py