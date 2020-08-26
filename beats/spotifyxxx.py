from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
# from .db_model import db, User, Tweet



load_dotenv()

market = ["us"]

client_id = getenv('SPOTIPY_CLIENT_ID')
client_secret = getenv('SPOTIPY_CLIENT_SECRET')

credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)


