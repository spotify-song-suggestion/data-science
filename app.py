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

# the following routes are examples from the link below
# https://spotipy.readthedocs.io/en/2.13.0/
# here’s a quick example of using Spotipy to list the names of all the albums released by the artist ‘Birdy’:
@app.route('/test-1')
def album_name():
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])
    return str(albums[0])
    # return render_template('home.html', results=albums['name'])

#how to get 30 second samples and cover art for the top 10 tracks for Led Zeppelin:
@app.route('/test-2')
def top10():
    # URI FOR LED ZEPPELIN
    lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()
    # return str(results['tracks'][0]['name']), 
    # results['tracks'][0]['preview_url'], 
    # results['tracks'][0]['album']['images'][0]['url'])
    return str(results['tracks'][0]['name']) +' '+ str(results['tracks'][0]['preview_url']) + ' ' + str(results['tracks'][0]['album']['images'][0]['url'])

# TODO: MACHINE LEARNING MODEL FILL - EXAMPLE FROM TWITOFF
# @app.route('/suggest', methods=['POST'])
# def compare(message=''):
#     user1  = request.values['user1']
#     user2  = request.values['user2']
#     tweet_text = request.values['tweet_text']

#     if user1 == user2:
#         message = 'Cannot compare a user to themselves'
#     else:
#         prediction = predict_user(user1, user2, tweet_text)
#         # message = '"{}" is more likely to be said \nby @{} than @{}'.format(
#         #     tweet_text, user1 if prediction else user2, user2 if prediction else user1
#         # )
#         message = '@{}  is most likely to say "{}" than @{}'.format(
#             user1 if prediction else user2, tweet_text, user2 if prediction else user1)
#     # return render_template('prediction.html', title='Prediction', message=message)
#     return render_template('base.html', title='Prediction', message=message, users=User.query.all())