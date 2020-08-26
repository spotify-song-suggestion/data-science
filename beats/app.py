# https://spotipy.readthedocs.io/en/2.13.0/
# pip install spotipy --upgrade
# pipenv install python-dotenv
# pipenv install simplejson
# pipenv install  flask-cors
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
from json.decoder import JSONDecodeError
import json as simplejson
from flask_cors import CORS

# our json friend
#print(json.dumps(VARIABLE, sort_keys=True, indent=4))


#### TODO wrapping this in spotifyxxx.py
load_dotenv()

# wrap this in a function
market = ["us"]

client_id = getenv('SPOTIPY_CLIENT_ID')
client_secret = getenv('SPOTIPY_CLIENT_SECRET')

credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)
##################



def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    CORS(app)
    # app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # db.init_app(app)

    @app.route('/songfeatures')
    def sf():
        '''
        SELECT * FROM song
        WHERE id = '6KbQ3uYMLKb5jDxLF7wYDD'
        '''
        # TODO get name of song and return id
        track_features = spotify.audio_features('6KbQ3uYMLKb5jDxLF7wYDD')
        print(simplejson.dumps(track_features, sort_keys=True, indent=4))
        return str(track_features)

    @app.route('/hello')
    def hello_world():
        return 'hello'

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/song')
    def getsong():
        '''
        this takes the song name and returns song details
        this takes artist name and returns up to 10 tracks per artist
        '''
        return render_template('asksong.html')

     
    @app.route('/artistinfo', methods=['GET'])
    @app.route('/artist/<input_artist>', methods=['GET'])
    def getartist(input_artist=None):
        '''
        this route returns more info about an artist
        # print(artist['name'])
        # print(str(artist['followers']['total']) + " followers")
        # print(artist['genres'][0])
        # print(artist['images'][0]['url'])
        '''
    
        input_artist = input_artist or request.values['input_artist']
        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
        if input_artist == "":
            return "Can't Touch This! Hammer Time!"
        if "_" in input_artist:
            input_artist = input_artist.replace("_"," ")
        name = input_artist

        # Search of the artist
        searchResults = spotify.search(q='artist:' + name, limit=2, offset=0, type=['artist']) #### for spotifyxxx.py
        artist = searchResults['artists']['items'][0]

        print(simplejson.dumps(searchResults, sort_keys=True, indent=4)) # full json
        print(simplejson.dumps(artist, sort_keys=True, indent=4)) # short version
        return artist



    @app.route('/songinfo', methods=['POST']) #/output changed to songinfo
    @app.route('/track/<user_input_song>', methods=['GET'])
    def output(user_input_song=None):
        # User inputs song name here 
        user_input_song = user_input_song or request.form['user_input_song']
        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
        # spotify search params
        results = spotify.search(str(user_input_song), type="track", limit=1) #### for spotifyxxx.py
        return results
   


    @app.route('/getsongs')
    @app.route('/albums/<input_artist>', methods=['GET'])
    def albumlist(input_artist=None):

        input_artist = input_artist or request.values['input_artist']
        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials()) #### for spotifyxxx.py
        if input_artist == "":
            return "Can't Touch This! Hammer Time!"
        if "_" in input_artist:
            input_artist = input_artist.replace("_"," ")
        name = input_artist

        # Search of the artist
        searchResults = spotify.search(q='artist:' + name, limit=1, offset=0, type=['artist'])#### for spotifyxxx.py
        artist = searchResults['artists']['items'][0]
        artistID = artist['id']
        albumResults = spotify.artist_albums(artistID)#### for spotifyxxx.py

        return str(albumResults)


    @app.route('/songsuggester')
    def feedmodel():
        # User inputs song name here
        user_input_song = request.form['user_input_song']

        # search db for song features
        # twitoff app.py line 30
        ssresult = Song.query(Song.name == user_input_song).one() #### for spotifyxxx.py 
        # NOTE ssresult this is a list       
        
        return ssresults # this should break into name and features


    return app