import base64
from requests import post, get
import json
from dotenv import load_dotenv
import os
import pandas as pd


load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")



def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


# Get id of any artist by his name only.
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url +query
    result = get(query_url, headers= headers)
    json_result = json.loads(result.content)['artists']['items']
    if len(json_result) == 0:
        print("No artist with this name")
        return None
    
    return json_result[0]


# Get all albums of this artist
def get_albums_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?country=EG"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)
    return json_result

# Parse albums in a dataframe
def extract_from_albums(albums):
    list_items = albums.get('items')
    list_albums = []
    for i in list_items:
        list_albums.append({'Album Type': i.get('album_type'), \
                            'Name': i.get('name'), 'Total tracks': i.get('total_tracks'), \
                                'Release Date': i.get('release_date'), 'ID': i.get('id')})
    df = pd.DataFrame.from_records(list_albums)
    return df


# Get songs of any album by its id
def get_songs_by_albums(token, album_id):
    url = f"	https://api.spotify.com/v1/albums/{album_id}/tracks?country=EG"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)
    return json_result

# Parse songs in a dataframe
def extract_from_songs(songs, album_name):
    list_items = songs.get('items')
    list_songs = []
    for i in list_items:
        list_songs.append({'Album Name': album_name,'Song Name': i.get('name'), 'Track Number': i.get('track_number'), \
                            'Duration': i.get('duration_ms'), 'ID': i.get('id')})
    df = pd.DataFrame.from_records(list_songs)
    return df

# Get top songs for any artist
def get_top_tracks(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=EG"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)
    return json_result

# Parse top songs in a dataframe
def extract_from_top_tracks(tracks):
    list_items = tracks.get('tracks')
    list_songs = []
    for i in list_items:
        list_songs.append({'Album': i.get('album').get('name'), 'Name': i.get('name'), \
                           'Date Release': i.get('album').get('release_date'),
                            'Duration': i.get('duration_ms'), 'ID': i.get('id')})
    df = pd.DataFrame.from_records(list_songs)
    return df


# Parse songs and albums of an artist in a dataframe
def get_songs_albums_of_artist(token, artist_name):
    print('Wait a few seconds, please!')
    artist = search_for_artist(token, artist_name)
    artist_id = artist.get('id')
    albums = get_albums_by_artist(token, artist_id)
    df_albums = extract_from_albums(albums)
    list=[]
    dict_albums = df_albums.to_dict('records')
    for i in dict_albums:
        songs = get_songs_by_albums(token, i.get('ID'))
        df = extract_from_songs(songs, i.get('Name'))
        dict_df = df.to_dict('records')
        for i in dict_df:
            list.append(i)
    dataframe = pd.DataFrame(list)
    required_df = dataframe[['Album Name','Song Name']]
    print('Extract done successfully!')
    return required_df


if __name__ == "__main__":
    token = get_token()
    # album_id = '6XFBQAGNOez6octj9v4MUo'
    # album_name = 'Shoft El Ayam'
    # songs = get_songs_by_albums(token, album_id)
    # cols = albums.get('items')[0].keys()
    # print(cols)
    # df = extract_from_songs(songs, album_name)
    # print(df)

    # top_songs = get_top_tracks(token, '5abSRg0xN1NV3gLbuvX24M')
    # cols = top_songs.get('tracks')[0].get('album').keys()
    # print(cols)
    # df = extract_from_top_tracks(top_songs)
    # print(df)

    df = get_songs_albums_of_artist(token, 'Amr Diab')
    print(df)