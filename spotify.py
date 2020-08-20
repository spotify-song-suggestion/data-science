"""Spotify Suggested Playlist Dashboard with Flask."""
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

#  pipenv install flask FLASK-SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song.sqlite3'
db = SQLAlchemy(app)

# This class is based off the data.csv file
class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True) # G
    acousticness = db.Column(db.Float) #A
    artists = db.Column(db.String(75)) #B
    danceability = db.Column(db.Integer) #C
    duration_ms = db.Column(db.Float) #D
    energy = db.Column(db.Float) #E
    explicit = db.Column(db.Float) #F
    instrumentalness = db.Column(db.Float) #H
    key = db.Column(db.Integer) #I
    liveness = db.Column(db.Float) #J
    loudness = db.Column(db.Float) #K
    mode = db.Column(db.Integer) #L
    name = db.Column(db.String(100)) #M Label 
    popularity = db.Column(db.Integer) #N
    release_date = db.Column(db.String(20)) #O
    speechiness = db.Column(db.Float) #P
    tempo = db.Column(db.Float) #Q
    valence = db.Column(db.Float) #R
    year = db.Column(db.Integer) #S
 
    def __repr__(self):
        # write a nice representation of Songs'
        return '< Title  %r - Artist  %r - Duration(ms) %r >' % (self.name, 
                                                                 self.artist, 
                                                                 self.duration_ms)




@app.route('/', methods=['GET'])
def root():
    """Base view."""


    """Filters results with 'value' >= 10"""
    
    # TODO : 
    # results = songs.query.all()

    # return render_template('home.html', tuple_list=tuple_list, gte10_list=results, city=city, parameter=parameter)
    # return "Spotify Build Week Project : Bring It!!!"
    return render_template('home.html')


@app.route('/refresh')
def refresh():
    root()
    """Pull fresh data from Open AQ and replace existing data."""
    db.drop_all()
    db.create_all()

    #
    # TODO: ETL pipeline data from csv to sqlite
    #

    # # Example of looping through a list, row by row
    # for i in range(len(tuple_list)):   
    #     list_new = Record(id=i, datetime=date_utc[i], value=value[i])
    #     db.session.add(list_new)
    

    # STORE IN DATABASE
    db.session.commit()
    
    return render_template('refresh.html')


@app.route('/reset')
def reset():
    db.drop_all()
    db.create_all()
    # return render_template('home.html', title='Database has been Reset!', TODO: vars=User.query.all())
    return 'Database has been reset'


#
# TODO : ETL info - data pipeline from csv to sqlite

# import sqlite3
# import pandas as pd

# # load data
# df = pd.read_csv('dict_output.csv')

# # strip whitespace from headers
# df.columns = df.columns.str.strip()

# con = sqlite3.connect("city_spec.db")

# # drop data into database
# df.to_sql("MyTable", con)

# con.close()