
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
# from .db_model import db, Song, History
import plotly.graph_objects as go
import plotly
# DS ML model
import pickle
from sklearn.neighbors import NearestNeighbors
# functions for encapsulation and reabability
from .spotify import search_artist_info, search_track_info, get_album_list, pull_features, plot_radar_one, get_song_info
from .suggest import find_recommended_songs
# from .etl_postgres import create_tables



def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)

    CORS(app)
    
    filename = 'beats/testing_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))


    @app.route('/songsuggester', methods=["GET"])
    def feedmodel(user_input_fav_song=None):
        '''
        This function produces a suggested playlist

        params:
            user_input_fav_song : str - Song Name

        returns :
            ssresults : list of tuples of
            (track, artist, danceability, instrumentalness, loadness, speechiness, valance)
        '''
        user_input_fav_song = request.values['user_input_fav_song']
        if user_input_fav_song == "":
            return render_template('home.html')
        if "_" in user_input_fav_song:
            user_input_fav_song = user_input_fav_song.replace("_"," ")
        
        results = search_track_info(user_input_fav_song)# api call

        song_id = results['tracks']['items'][0]['id'] 
        
        track_features = pull_features(song_id) 
        
        danceability =  track_features[0]['danceability']
        instrumentalness = track_features[0]['instrumentalness']
        loadness = track_features[0]['loudness']
        speechiness = track_features[0]['speechiness']
        valance = track_features[0]['valence']
        fav_five = [danceability, instrumentalness, loadness, speechiness, valance]
        # shaping the data to fit the model inputs
        y = [fav_five]
        x = ['danceability',  'instrumentalness', 'loudness', 'speechiness',  'valence'] # Series
        df_new = pd.DataFrame(y, columns= x)
        audio_features = df_new.iloc[0, 0:].to_numpy() 

        song_list = find_recommended_songs(audio_features)
        
        results = []
        for song in song_list: 
            all_audio_features = pull_features(song)

            danceability =  all_audio_features[0]['danceability']
            instrumentalness = all_audio_features[0]['instrumentalness']
            loadness = all_audio_features[0]['loudness']
            speechiness = all_audio_features[0]['speechiness']
            valance = all_audio_features[0]['valence']
            
            result = get_song_info(song)
            artist = result['album']['artists'][0]['name'] # artist 
            track = result['album']['name']  # track                 

            ssresults = (track, artist, danceability, instrumentalness, loadness, speechiness, valance)
            ssresults = str(ssresults) 
            # NOTE ssresults this is a list
            print(ssresults)       
            results.append(ssresults)
            
        return render_template('home.html', results=results)  # this is to render list to webpage
        # return str(results) #return the list of song suggests
       

    @app.route('/suggest/<user_input_fav_song>', methods=['GET'])
    def modelweb(user_input_fav_song=None):
        '''
        This can be accessed thru the web link defined in Documentation.md
        This function produces a suggested playlist

        params:
            user_input_fav_song : str - Song Name

        returns :
            ssresults : list of tuples of
            (track, artist, danceability, instrumentalness, loadness, speechiness, valance)
        '''
        if "_" in user_input_fav_song:
            user_input_fav_song = user_input_fav_song.replace("_"," ")
        
        results = search_track_info(user_input_fav_song)# api call

        song_id = results['tracks']['items'][0]['id'] 
        
        track_features = pull_features(song_id) 
        
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

        song_list = find_recommended_songs(audio_features)
        
        results = []
        for song in song_list: 
            # search api for song features
            all_audio_features = pull_features(song)

            danceability =  all_audio_features[0]['danceability']
            instrumentalness = all_audio_features[0]['instrumentalness']
            loadness = all_audio_features[0]['loudness']
            speechiness = all_audio_features[0]['speechiness']
            valance = all_audio_features[0]['valence']
            
            result = get_song_info(song)
            artist = result['album']['artists'][0]['name'] # artist Weather Report
            track = result['album']['name']  # track                 

            ssresults = (track, artist, danceability, instrumentalness, loadness, speechiness, valance)

            ssresults = str(ssresults) 
            # NOTE ssresult this is a list
            results.append(ssresults)
            
        return str(results) #return the list of song suggests


    @app.route('/hello')
    def hello_world():
        return 'Hello from DSPT5 and DSPT6 Lambda School 2020'


    @app.route('/')
    def index():
        return render_template('home.html')


    @app.route('/song')
    def getsong():
        '''
        Test page to
            take the artist name and returns cover art additional artist info
            takes the song name and returns song details
            takes artist name and returns up to 10 tracks per artist
        '''
        return render_template('asksong.html')

     
    @app.route('/artistinfo', methods=['GET'])
    @app.route('/artist/<input_artist>', methods=['GET'])
    def getartist(input_artist=None):
        '''
        This function uses spotify.py to find track info

        params:
            name : str - name of artist

        returns:
            json file of all artist info     
        '''   
        input_artist = input_artist or request.values['input_artist']
        if input_artist == "":
            return render_template('home.html')
        if "_" in input_artist:
            input_artist = input_artist.replace("_"," ")
        name = input_artist

        searchResults = search_artist_info(name)
        artist = searchResults['artists']['items'][0]

        return artist


    @app.route('/songinfo', methods=['POST']) #/output changed to songinfo
    @app.route('/track/<user_input_song>', methods=['GET'])
    def output(user_input_song=None):
        '''
        This function uses spotify.py to find track info

        params:
            user_input_song : str - name of song

        returns:
            json file of all track info associated with track
        '''
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
        '''
        This function uses spotify.py to find albums list

        params:
            name : str - name of artist

        returns:
            json file of all albums info associated with artist
        '''
        input_artist = input_artist or request.values['input_artist']
        if input_artist == "":
            return render_template('home.html')
        if "_" in input_artist:
            input_artist = input_artist.replace("_"," ")
        name = input_artist

        # Search of the artist
        albumResults = get_album_list(name)
        return str(albumResults)


    return app