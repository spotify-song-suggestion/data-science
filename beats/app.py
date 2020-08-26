
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
from .db_model import db, Song, History


from .spotify import search_artist_info, search_track_info, get_album_list, pull_features
# our json friend
#print(json.dumps(VARIABLE, sort_keys=True, indent=4))


def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    CORS(app)

    # TODO test this #############################################################################################################################
    @app.route('/songfeatures')
    def sf():
        # TODO user gives us song 
        user_input_fav_song = "Thriller"
        # Hard Coded

        user_input_fav_song = user_input_fav_song or request.form['user_input_fav_song']
        results = search_track_info(user_input_fav_song)
        
        song_id = results['tracks']['items'][0]['id'] # song_id = '6KbQ3uYMLKb5jDxLF7wYDD'
        
        track_features = pull_features(song_id)

        print(simplejson.dumps(track_features, sort_keys=True, indent=4))
        #using this for ML model

        # have to return these values to the model
        #Features I use in my NN model: ['danceability',  'instrumentalness', 'loudness', 'speechiness',  'valence']
        # TODO separate this into str(track_features[0]['danceability'])
        return str(track_features[0])


    @app.route('/songsuggester')
    def feedmodel():
        db.create_all()
        results = []
        song_list = ['6llUzeoGSQ53W3ThFbReE2',
                     '22mLKFanGy1bEb0qWuvMV0',
                     '0psB5QzGb4653K0uaPgEyh',
                     '3R6GxZEzCWDNnwo8QWeOw6']
                     #Young and Fine,Suck My Kiss, Suck My Kiss, Waiting for Somebody
        for song in song_list:
           
            # search db for song features
            ssresults = Song.query.get(song)
            ssresults = str(ssresults) 
            # NOTE ssresult this is a list
            print(ssresults)       
            results.append(ssresults)
        # return str(results) 
        return render_template('home.html', results=results)
    





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