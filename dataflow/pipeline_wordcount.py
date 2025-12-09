from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam as beam 
def run():
    # Configuración del pipeline
    options = PipelineOptions(
        runner="DataflowRunner", # Cambiar a DirectRunner para local
        project="e-gcp-data-engineer",
        region="us-central1",
        temp_location="gs://bucket-dataflow324123/temp"
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Leer archivo" >> beam.io.ReadFromText("gs://dataflow-samples/shakespeare/kinglear.txt")
            | "Separar palabras" >> beam.FlatMap(lambda line: line.split())
            | "Contar palabras" >> beam.combiners.Count.PerElement()
            | "Guardar resultados" >> beam.io.WriteToText("gs://bucket-dataflow324123/output/wordcount")
        )

    print("Pipeline ejecutado exitosamente.")

if __name__ == "__main__":
    run()