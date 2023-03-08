from dotenv import load_dotenv
import os
from service.extract import get_songs_albums_of_artist, get_token
from service.transform import transform_batch
import service.load as load
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Extract
token = get_token()
artist = 'Mohammed Hamaki'
df = get_songs_albums_of_artist(token, artist)
# Transform
df_transformed = transform_batch(df)
print('Transformation done successfully!')
# Load to storage
file_name = f"{artist}.csv"
target_dir = f"Challenge/data_results/{file_name}"
load.load_data(df_transformed, target_dir)
# Load to database
conn = load.create_table(artist)
load.load_db_data(df_transformed, artist)
print('Load done successfully!')