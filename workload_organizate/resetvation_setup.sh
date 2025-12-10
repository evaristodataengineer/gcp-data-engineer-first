
bq mk --reservation --project_id=e-gcp-data-engineer-5 --slosts=200 myBaseReservation

bq mk --reservation --project_id=e-gcp-data-engineer-5 --location=US --slots=200 myExpReservation

bq mk --reservation_assignment --reservation_id=e-gcp-data-engineer-5:US.myexpreservation --assignee_id=e-gcp-data-engineer-5 --job_type=QUERY