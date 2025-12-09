import apache_beam as beam
from apache_beam.options.pipeline_options import (
    PipelineOptions,
    GoogleCloudOptions,
    StandardOptions,
    SetupOptions
)

def run():

    # Leer parámetros desde la terminal (MUY IMPORTANTE)
    pipeline_options = PipelineOptions()

    # Opciones necesarias para Dataflow Runner
    google_options = pipeline_options.view_as(GoogleCloudOptions)
    standard_options = pipeline_options.view_as(StandardOptions)
    setup_options = pipeline_options.view_as(SetupOptions)

    # Requerido para crear templates
    setup_options.save_main_session = True

    with beam.Pipeline(options=pipeline_options) as p:
        (
            p
            | "Leer archivo" >> beam.io.ReadFromText(
                "gs://dataflow-samples/shakespeare/kinglear.txt"
            )
            | "Separar palabras" >> beam.FlatMap(lambda line: line.split())
            | "Contar palabras" >> beam.combiners.Count.PerElement()
            | "Guardar resultados" >> beam.io.WriteToText(
                "gs://us-central1-mi-entorno-comp-3badcdf0-bucket/output/wordcount"
            )
        )

    print("Pipeline ejecutado exitosamente.")

if __name__ == "__main__":
    run()
