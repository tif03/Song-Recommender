"""use api to find an artist's top 10 songs"""

from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from random import randrange

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#get access token using client id and secret with grant type as client credentials
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes =  auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data = {"grant_type" : 'client_credentials'}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    header = get_auth_header(token)

    #query
    query = f"q={artist_name}&type=artist&limit=1"

    query_url = url + "?" + query
    result = get(query_url, headers=header)
    json_result = json.loads(result.content)['artists']['items']
    if len(json_result) == 0: 
        print("no artist with this name exists...") 
        return None
    
    return json_result[0]
    
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    header = get_auth_header(token)
    result = get(url, headers=header)
    json_result = json.loads(result.content)['tracks']
    return json_result

def get_related_artists(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    header = get_auth_header(token)
    result = get(url, headers=header)
    json_result = json.loads(result.content)['artists']
    return json_result

artist = input('What artist?\n')

token = get_token()
result = search_for_artist(token, artist)
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)

#for idx, song in enumerate(songs):
    #print(f"{idx + 1}. {song['name']}")

#get related artist
related_artists = get_related_artists(token, artist_id)
related_artists_list = [[artist, artist_id]]
for idx, artist in enumerate(related_artists):
    related_artists_list.append([artist['name'], artist['id']])

#generate playlist based on an artist and their related artists
playlist = []
for artist_name, artist_id in related_artists_list:
    songs = get_songs_by_artist(token, artist_id)
    playlist.append(songs[randrange(len(songs)//2)]['name'] + ' by ' + artist_name)

for idx, track in enumerate(playlist):
    print(f"{idx + 1}. {track}")



