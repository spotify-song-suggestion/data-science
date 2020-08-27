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
# DS ML model
import pickle
from sklearn.neighbors import NearestNeighbors
# functions for encapsulation and reabability
from .spotify import search_artist_info, search_track_info, get_album_list, pull_features, plot_radar_one
from .suggest import find_recommended_songs
from .etl_postgres import create_tables



def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)

    # TODO switch to PostgreDB
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    #app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLITE3_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    
    CORS(app)

    
    filename = 'beats/testing_model.sav'
    # filename = 'beats\\testing_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    # TODO look where it is necessary to save new data to our database
    # TODO reset route and load data route have to setup PostgresDB
    # TODO if song is not in database then pull from spotify api
    @app.route('/songfeatures')
    def sf(user_input_fav_song=None):
        # TODO user gives us song 
        # user_input_fav_song = "Thriller"
        # Hard Coded
        user_input_fav_song =  request.values['user_input_fav_song']
        if user_input_fav_song == "":
            return render_template('home.html')
        if "_" in user_input_fav_song:
            user_input_fav_song = user_input_fav_song.replace("_"," ")
        

        results = search_track_info(user_input_fav_song)# api call

        song_id = results['tracks']['items'][0]['id'] # song_id = '6KbQ3uYMLKb5jDxLF7wYDD'
        
        track_features = pull_features(song_id) 
        # To help visualize the json file
        # print(simplejson.dumps(track_features, sort_keys=True, indent=4))
        
        danceability =  track_features[0]['danceability']
        instrumentalness = track_features[0]['instrumentalness']
        loadness = track_features[0]['loudness']
        speechiness = track_features[0]['speechiness']
        valance = track_features[0]['valence']
        fav_five = [danceability, instrumentalness, loadness, speechiness, valance]
      
        y = [fav_five]
        x = ['danceability',  'instrumentalness', 'loudness', 'speechiness',  'valence'] # Series
        df_new = pd.DataFrame(y, columns= x)
        audio_features = df_new.iloc[0, 0:].to_numpy() 

        return audio_features # this is return for DS ML model


    @app.route('/songsuggester', methods=["GET"])
    def feedmodel():
        db.create_all()

        audio_features = sf()

        song_list = find_recommended_songs(audio_features)
        
        results = []
        for song in song_list: 
            # search db for song features
            ssresults = Song.query.get(song)
            ssresults = str(ssresults) 
            # NOTE ssresult this is a list
            print(ssresults)       
            results.append(ssresults)
            
        return render_template('home.html', results=results)  # this is to render list to webpage
        # return str(results) #return the list of song suggests
       

    @app.route('/hello')
    def hello_world():
        return 'Hello from DSPT5 and DSPT6 Lambda School 2020'


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
            return render_template('home.html')
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

        if user_input_song == "":
            return render_template('home.html')
        if "_" in user_input_song:
            user_input_song = user_input_song.replace("_"," ")

        results = search_track_info(user_input_song)
        return results
   

    @app.route('/getsongs')
    @app.route('/albums/<input_artist>', methods=['GET'])
    def albumlist(input_artist=None):

        input_artist = input_artist or request.values['input_artist']
        if input_artist == "":
            return render_template('home.html')
        if "_" in input_artist:
            input_artist = input_artist.replace("_"," ")
        name = input_artist

        # Search of the artist
        albumResults = get_album_list(name)
        return str(albumResults)

    @app.route('/reset')
    def reset():
        db.drop_all()
        #db.create_all()
        create_tables()
        return render_template('home.html')


    return app