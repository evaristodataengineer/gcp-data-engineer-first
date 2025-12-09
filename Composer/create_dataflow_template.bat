"C:\Program Files\Python312\python.exe" wordcount.py ^
  --runner DataflowRunner ^
  --project e-gcp-data-engineer ^
  --region us-central1 ^
  --staging_location gs://us-central1-mi-entorno-comp-3badcdf0-bucket/staging ^
  --temp_location gs://us-central1-mi-entorno-comp-3badcdf0-bucket/temp ^
  --template_location gs://us-central1-mi-entorno-comp-3badcdf0-bucket/templates/wordcount_template ^
  --save_main_session True
