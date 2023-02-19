from dotenv import load_dotenv
import os
from service.extract import get_songs_albums_of_artist, get_token
from service.transform import transform_batch
from service.load import load_data
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


token = get_token()
artist = 'Haifa Wahbi'
df = get_songs_albums_of_artist(token, artist)

df_transformed = transform_batch(df)
print('Transformation done successfully!')

file_name = f"{artist}.csv"
target_dir = f"data_results/{file_name}"
load_data(df_transformed, target_dir)
print('Load done successfully!')