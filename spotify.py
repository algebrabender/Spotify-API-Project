import os
import json
import webbrowser
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()
cid = os.getenv('CLIENT_ID')
secret = os.getenv('SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def search_spotify(search_query, term_type):
    if term_type == 0: #song
        search_result = sp.search(search_query, type="track")
        songs = search_result['tracks']['items']
        images = []
        urls = []
        for idx, song in enumerate(songs):
            print(song['name'])
            artist_data = sp.artist(song['artists'][0]['uri'])
            if 'k-pop girl group' in artist_data['genres'] or 'k-pop boy group' in artist_data['genres'] or 'k-pop' in artist_data['genres']:
                if len(song['album']['images']) > 0:
                    images.append(song['album']['images'][0]['url'])
                    urls.append(song['external_urls']['spotify'])
    elif term_type == 1: #album
        search_result = sp.search(search_query, type="album")
        albums = search_result['albums']['items']
        images = []
        urls = []
        for idx, album in enumerate(albums):
            print(album['name'])
            artist_data = sp.artist(album['artists'][0]['uri'])
            if 'k-pop girl group' in artist_data['genres'] or 'k-pop boy group' in artist_data['genres'] or 'k-pop' in artist_data['genres']:
                if len(album['images']) > 0:
                    images.append(album['images'][0]['url'])
                    urls.append(album['external_urls']['spotify'])
    else: #artist
        search_result = sp.search(search_query, type="artist")
        artists = search_result['artists']['items']
        images = []
        urls = []
        for idx, artist in enumerate(artists):
            print(artist['name'])
            if 'k-pop girl group' in artist['genres'] or 'k-pop boy group' in artist['genres'] or 'k-pop' in artist['genres']:
                if len(artist['images']) > 0:
                    images.append(artist['images'][0]['url'])
                    urls.append(artist['external_urls']['spotify'])
        
    return images, urls 

#search_spotify("queendom", 1)