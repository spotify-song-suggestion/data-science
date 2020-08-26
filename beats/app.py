
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


from .spotify import search_artist_info, search_track_info, get_album_list
# our json friend
#print(json.dumps(VARIABLE, sort_keys=True, indent=4))


def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    CORS(app)


    @app.route('/songfeatures')
    def sf():
        # TODO user gives us song
        # TODO see output()
        # TODO find song and songid
        #using this for ML model
        song_id = results['tracks']['items'][0]['id']
        # TODO pass id to track features
        track_features = spotify.audio_features('6KbQ3uYMLKb5jDxLF7wYDD')
        
        print(simplejson.dumps(track_features, sort_keys=True, indent=4))
        
        return str(track_features)

    @app.route('/songsuggester')
    def feedmodel():
        # User inputs song name here
        user_input_song = request.form['user_input_song']

        # search db for song features
        # twitoff app.py line 30
        ssresult = Song.query(Song.name == user_input_song).one() #### for spotifyxxx.py 
        # NOTE ssresult this is a list       
        
        return ssresults # this should break into name and features

    


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
    
        input_artist = input_artist or request.values['input_artist']
        if input_artist == "":
            return "Can't Touch This! Hammer Time!"
        if "_" in input_artist:
            input_artist = input_artist.replace("_"," ")
        name = input_artist

        # Search of the artist
        searchResults = search_artist_info(name)
        artist = searchResults['artists']['items'][0]

        print(simplejson.dumps(searchResults, sort_keys=True, indent=4)) # full json
        print(simplejson.dumps(artist, sort_keys=True, indent=4)) # short version
        return artist



    @app.route('/songinfo', methods=['POST']) #/output changed to songinfo
    @app.route('/track/<user_input_song>', methods=['GET'])
    def output(user_input_song=None):
        # User inputs song name here 
        user_input_song = user_input_song or request.form['user_input_song']
        results = search_track_info(user_input_song)

        # this helps you fish threw a json 
        # print(simplejson.dumps(results['tracks']['items'][0]['id'], sort_keys=True, indent=4))
        return results
   

    @app.route('/getsongs')
    @app.route('/albums/<input_artist>', methods=['GET'])
    def albumlist(input_artist=None):

        input_artist = input_artist or request.values['input_artist']
        if input_artist == "":
            return "Can't Touch This! Hammer Time!"
        if "_" in input_artist:
            input_artist = input_artist.replace("_"," ")
        name = input_artist

        # Search of the artist
        albumResults = get_album_list(name)
        return str(albumResults)


    return app