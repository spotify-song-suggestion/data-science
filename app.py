# https://spotipy.readthedocs.io/en/2.13.0/
# pip install spotipy --upgrade
# pipenv install python-dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import time
from flask import Flask, jsonify, Response, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

market = ["us"]

client_id = getenv('SPOTIPY_CLIENT_ID')
client_secret = getenv('SPOTIPY_CLIENT_SECRET')


credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/output', methods=['POST'])
def output():
    # connecting html to request
    # User inputs song name here
    user_input_song = request.form['user_input_song']
    # spotify search params
    results = spotify.search(str(user_input_song), type="track", limit=1)

    return results

@app.route('/test-1')
def album_name():
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    # for album in albums:
    #     print(album['name'])
    return str(albums[0])
    # return render_template('home.html', results=albums['name'])