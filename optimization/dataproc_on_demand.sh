
gcloud projects add-iam-policy-binding e-gcp-data-engineer-5 --member="user:evaristodataengineer@gmail.com" --role="roles/dataproc.editor"


gcloud dataproc batches submit spark --region=us-central1 --class org.apache.spark.examples.SparkPi --jars file:///usr/lib/spark/examples/jars/spark-examples.jar -- 1000