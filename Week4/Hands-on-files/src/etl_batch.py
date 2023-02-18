import os
from extract.extract_batch import extract_batch_files
from transform.transform_batch import transform_batch
from load.load_batch import load_data

# Extract
df = extract_batch_files()
print("extraction is completed!")


# Transform
df = transform_batch(df)
print("Transformation is done")

# Load
file_name = "result_batch.csv"
target_dir = f"data_files/data_results/{file_name}"
load_data(df, target_dir)

print("ETL batch is Done!")
