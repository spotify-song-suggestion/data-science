"""Spotify Suggested Playlist Dashboard with Flask."""
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import pandas as pd

#  pipenv install flask FLASK-SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song.sqlite3'
db = SQLAlchemy(app)


# This class is based off the data.csv file
# TODO check types with etl_pipeline.py
class Song(db.Model):
    acousticness = db.Column(db.Float)  # A
    artists = db.Column(db.String(75))  # B
    danceability = db.Column(db.Integer)  # C
    duration_ms = db.Column(db.Float)  # D
    energy = db.Column(db.Float)  # E
    explicit = db.Column(db.Float)  # F
    id = db.Column(db.String, primary_key=True)  # G
    instrumentalness = db.Column(db.Float)  # H
    key = db.Column(db.Integer)  # I
    liveness = db.Column(db.Float)  # J
    loudness = db.Column(db.Float)  # K
    mode = db.Column(db.Integer)  # L
    name = db.Column(db.String(100))  # M Label
    popularity = db.Column(db.Integer)  # N
    release_date = db.Column(db.String(20))  # O
    speechiness = db.Column(db.Float)  # P
    tempo = db.Column(db.Float)  # Q
    valence = db.Column(db.Float)  # R
    year = db.Column(db.Integer)  # S

    def __repr__(self):
        # write a nice representation of Song'
        return '< Title  %r - Artist  %r - Duration(ms) %r >' % (self.name,
                                                                 self.artists,
                                                                 self.duration_ms)


@app.route('/', methods=['GET'])
def root():
    """Base view."""
    
    # get creds
    # open connection to spotify api 




    # db.drop_all()
    # db.create_all()

    # TODO :
    results = Song.query.limit(10).all()

    # return render_template('home.html',TODO: variable for front end parameter=parameter)
    # return "Spotify Build Week Project : Bring It!!!"
    return render_template('home.html', results=results)
    # return str(results) # this was 1st trial to see 


@app.route('/update')
def update():
    root()
    """Pull fresh data from Open AQ and replace existing data."""
    db.drop_all()
    db.create_all()

    #
    # TODO: ETL pipeline data from csv to sqlite
    #

    # # Example of looping through a list, row by row
    # for i in range(len(tuple_list)):   
    #     list_new = Record(id=i, datetime=date_utc[i], value=va
    # lue[i])
    #     db.session.add(list_new)

    # STORE IN DATABASE
    db.session.commit()

    return render_template('refresh.html')


"""reset route for song sqlite3 DB"""

@app.route('/reset')
def reset():
    db.drop_all()
    db.create_all()
    con = sqlite3.connect('song.sqlite3')
    df = pd.read_csv('csv/data.csv')
    df.to_sql('song', con, if_exists='append', index=False)
    return 'Database has been reset'

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
