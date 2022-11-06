import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()
cid = os.getenv('CLIENT_ID')
secret = os.getenv('SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# aespa_albums = sp.artist_albums("https://open.spotify.com/artist/6YVMFz59CuY7ngCxTxjpxE?si=NgxAeWZ1S62aGJlu3f1z5Q")
# albums = aespa_albums['items']
# while aespa_albums['next']:
#     aespa_albums = sp.next(aespa_albums)
#     albums.extend(aespa_albums['items'])

# for album in albums:
#     print(album['name'])

# redvelvet_albums = sp.artist_albums("https://open.spotify.com/artist/1z4g3DjTBBZKhvAroFlhOM?si=kraFCZD3RTC7Y3FKO9EsRA")
# albums = redvelvet_albums['items']
# while redvelvet_albums['next']:
#     redvelvet_albums = sp.next(redvelvet_albums)
#     albums.extend(redvelvet_albums['items'])

# for album in albums:
#     print(album['name'])

search_in =  "" # input()

if len(search_in) > 1:
    search_str = search_in
else:
    search_str = 'queendom'

result = sp.search(search_str, type="track")
#print(result['tracks']['items'])
possible_albums = result['tracks']['items']

for idx, album in enumerate(possible_albums):
    for idxx, artist in enumerate(album['artists']):
        artist_data = sp.artist(artist['uri'])
        if 'k-pop girl group' in artist_data['genres'] or 'k-pop boy group' in artist_data['genres'] or 'k-pop' in artist_data['genres']:
            print(album['name'])
            print(artist_data['name'])