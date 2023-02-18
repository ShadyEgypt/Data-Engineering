from extract.extract_db import extract_db_data
from transform.transform_db import transform_db_data
from load.load_db import load_db_data

# Extract
df, db_conn = extract_db_data()
print("Extraction is done")


# Transformation
df, db_conn = transform_db_data(df, db_conn)
print("Transformation is done")


# Load
load_db_data(df, db_conn)
print("ETL db is Done")
