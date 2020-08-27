
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
import plotly.graph_objects as go
import plotly


from .spotify import search_artist_info, search_track_info, get_album_list, pull_features, plot_radar_one
# our json friend
#print(json.dumps(VARIABLE, sort_keys=True, indent=4))


def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    CORS(app)


    # TODO look where it is necessary to save new data to our database
    # TODO have to setup PostgresDB
    # TODO if song is not in database then pull from spotify api
    # TODO test this #############################################################################################################################
    @app.route('/songfeatures')
    def sf():
        # TODO user gives us song 
        user_input_fav_song = "Thriller"
        # Hard Coded

        user_input_fav_song = user_input_fav_song or request.form['user_input_fav_song']
        results = search_track_info(user_input_fav_song)# api call
        
        song_id = results['tracks']['items'][0]['id'] # song_id = '6KbQ3uYMLKb5jDxLF7wYDD'
        
        track_features = pull_features(song_id) # api call

        print(simplejson.dumps(track_features, sort_keys=True, indent=4))
        #using this for ML model

        # have to return these values to the model
        #Features I use in my NN model: ['danceability',  'instrumentalness', 'loudness', 'speechiness',  'valence']
        # TODO separate this into str(track_features[0]['danceability'])
        danceability =  track_features[0]['danceability']
        instrumentalness = track_features[0]['instrumentalness']
        loadness = track_features[0]['loudness']
        speechiness = track_features[0]['speechiness']
        valance = track_features[0]['valence']
        fav_five = [danceability, instrumentalness, loadness, speechiness, valance]
        '''
        {'danceability': 0.764, 
        'energy': 0.887, 
        'key': 11, 
        'loudness': -3.725, 
        'mode': 1, 
        'speechiness': 0.0738, 
        'acousticness': 0.0816, 
        'instrumentalness': 0.000108, 
        'liveness': 0.847, 
        'valence': 0.721, 
        'tempo': 118.421, 
        'type': 'audio_features', 
        'id': '7azo4rpSUh8nXgtonC6Pkq', 
        'uri': 'spotify:track:7azo4rpSUh8nXgtonC6Pkq', 
        'track_href': 'https://api.spotify.com/v1/tracks/7azo4rpSUh8nXgtonC6Pkq', 
        'analysis_url': 'https://api.spotify.com/v1/audio-analysis/7azo4rpSUh8nXgtonC6Pkq', 
        'duration_ms': 358053, 
        'time_signature': 4}
        '''
        y = fav_five
        x = ['danceability',  'instrumentalness', 'loudness', 'speechiness',  'valence']
        fig = plot_radar_one(x,y)
        
        # return str(fav_five) # this is return for DS ML model
        return fig


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
            
        return render_template('home.html', results=results)  # this is to render list to webpage
        # return str(results[0]) #return the first song suggestion
       





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