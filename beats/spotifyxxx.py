from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
# from .db_model import db, User, Tweet

'''
this route returns a list of all tracks of a artist

# the Following code to make sense of the JSON file
# Album and track details
trackNames = []
trackURIs = []
trackArt = []
z = 0

# Extract album data
albumResults = spotify.artist_albums(artistID)
albumResults = albumResults['items']

for item in albumResults:
print("ALBUM " + item['name'])
albumID = item['id']
albumArt = item['images'][0]['url']
# Extract track data
trackResults = spotify.album_tracks(albumID)
trackResults = trackResults['items']
for item in trackResults:
    print(str(z) + ": " + item['name'])
    trackNames.append(item['name'])
    trackURIs.append(item['uri'])
    trackArt.append(albumArt)
    z+=1
print()

'''

load_dotenv()

market = ["us"]

client_id = getenv('SPOTIPY_CLIENT_ID')
client_secret = getenv('SPOTIPY_CLIENT_SECRET')

credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)


