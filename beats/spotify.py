from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import plotly.graph_objects as go
import plotly.express as px


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
    This function uses the Spotify API to find track info

    params:
        song_id : str - id of song in Spotify

    returns:
        json file of all info associated with song
    '''    
    results = spotify.track(song_id)
    return results


def search_artist_info(name):
    '''
    This function uses the Spotify API to find track info

    params:
        name : str - name of artist

    returns:
        json file of all artist info     
    '''
    searchResults = spotify.search(q='artist:' + name, limit=2, offset=0, type=['artist']) 
    return searchResults


def search_track_info(user_input_song):
    '''
    This function uses the Spotify API to find track info

    params:
        user_input_song : str - name of song

    returns:
        json file of all track info associated with track
    '''
    results = spotify.search(str(user_input_song), type="track", limit=1) 
    return results


def get_album_list(name):

    searchResults = spotify.search(q='artist:' + name, limit=1, offset=0, type=['artist'])

    artist = searchResults['artists']['items'][0]
    artistID = artist['id']
    albumResults = spotify.artist_albums(artistID)
    return albumResults


def pull_features(song_id):
    '''
    This function uses the Spotify API to find track info

    params:
        song_id : str - id of song in Spotify

    returns:
        json file of song features associated with song for ML model
    '''
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

