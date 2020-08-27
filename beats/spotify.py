from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import plotly.graph_objects as go
import plotly.express as px
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
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

def search_artist_info(name):
    '''
    this route returns more info about an artist
    # print(artist['name'])
    # print(str(artist['followers']['total']) + " followers")
    # print(artist['genres'][0])
    # print(artist['images'][0]['url'])
    '''
    searchResults = spotify.search(q='artist:' + name, limit=2, offset=0, type=['artist']) #### for spotifyxxx.py
    return searchResults


def search_track_info(user_input_song):   
    results = spotify.search(str(user_input_song), type="track", limit=1) #### for spotifyxxx.py
    return results

def get_album_list(name):
    searchResults = spotify.search(q='artist:' + name, limit=1, offset=0, type=['artist'])#### for spotifyxxx.py

    artist = searchResults['artists']['items'][0]
    artistID = artist['id']
    albumResults = spotify.artist_albums(artistID)#### for spotifyxxx.py
    return albumResults




# TODO check this
def pull_features(song_id):
    track_features = spotify.audio_features(song_id)
    return track_features


def plot_radar_one(x, y):

    # name vs song features
    
    fig = go.Figure(data=go.Scatterpolar(
      r=y,
      theta=x,
      fill='toself'
    ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True
        ),
      ),
      showlegend=False
    )
    fig.show()

    return fig

