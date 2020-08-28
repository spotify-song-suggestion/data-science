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


def get_song_info(song_id):
    '''
    for Song Suggester
    '''
    results = spotify.track(song_id)
    return results

def search_artist_info(name):
    '''
    this route returns more info about an artist
    # print(artist['name'])
    # print(str(artist['followers']['total']) + " followers")
    # print(artist['genres'][0])
    # print(artist['images'][0]['url'])
    '''
    searchResults = spotify.search(q='artist:' + name, limit=2, offset=0, type=['artist']) 
    return searchResults

# def search_info(song_id):   
#     results = spotify.search(song_id, offset=0, type=["artist","track"], limit=1) 
#     return results



def search_track_info(user_input_song):   
    results = spotify.search(str(user_input_song), type="track", limit=1) 
    return results

def get_album_list(name):
    searchResults = spotify.search(q='artist:' + name, limit=1, offset=0, type=['artist'])

    artist = searchResults['artists']['items'][0]
    artistID = artist['id']
    albumResults = spotify.artist_albums(artistID)
    return albumResults


def pull_features(song_id):
    # song_id = '6llUzeoGSQ53W3ThFbReE2' # for testing
    track_features = spotify.audio_features(song_id)
    return track_features


def plot_radar_one(x, y):
    '''name vs song features
        y = [fav_five]
        x = ['danceability',  'instrumentalness', 'loudness', 'speechiness',  'valence']
    '''
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






# TODO for output of songsuggest PART #2
# ['danceability',  'instrumentalness', 'loudness', 'speechiness',  'valence']
# pull_features or audio_feature produces this json
# {
#     0 "acousticness": 0.725,
#     1 "analysis_url": "https://api.spotify.com/v1/audio-analysis/6llUzeoGSQ53W3ThFbReE2",
# 2 "danceability": 0.371,
#     3 "duration_ms": 413587,
#     4 "energy": 0.721,
# 5 "id": "6llUzeoGSQ53W3ThFbReE2",
# 6 "instrumentalness": 0.000139,
#     7 "key": 5,
#     8 "liveness": 0.349,
# 9 "loudness": -9.952,
#     10 "mode": 0,
# 11 "speechiness": 0.0488,
#     12 "tempo": 92.481,
#     13 "time_signature": 4,
#     14 "track_href": "https://api.spotify.com/v1/tracks/6llUzeoGSQ53W3ThFbReE2",
#     15 "type": "audio_features",
#     16 "uri": "spotify:track:6llUzeoGSQ53W3ThFbReE2",
# 17 "valence": 0.673
# }




# 5 "id": "6llUzeoGSQ53W3ThFbReE2",
# 2 "danceability": 0.371,
# 6 "instrumentalness": 0.000139,
# 9 "loudness": -9.952,
# 11 "speechiness": 0.0488,
# 17 "valence": 0.673
