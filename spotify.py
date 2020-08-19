"""Spotify Suggested Playlist Dashboard with Flask."""
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song.sqlite3'
db = SQLAlchemy(APP)


class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True) # G
    acousticness = db.Column(db.Float) #A
    artists = db.Column(DB.String(75)) #B
    danceability = db.Column(db.Integer) #C
    duration_ms = db.Column(db.Float) #D
    energy = db.Column(db.Float) #E
    explicit = db.Column(db.Float) #F
    instrumentalness = db.Column(db.Float) #H
    key = db.Column(db.Integer) #I
    liveness = db.Column(db.Float) #J
    loudness = db.Column(db.Float) #K
    mode = db.Column(db.Integer) #L
    name = db.Column(DB.String(100)) #M Label 
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




@APP.route('/', methods=['GET'])
def root():
    """Base view."""
    ## PART 2
    ## This pulls in fresh data from the OpenAQ API
    api = openaq.OpenAQ()
    tuple_list = get_api_data(api, city, parameter)
    
    # TODO :
    # 2nd pull from api
    # second_pull_from_api = get_api_latest_data(api)

    """Filters results with 'value' >= 10"""
    # PART 4
    # This queries the DB to filter value >= 10
    results = Record.query.filter(Record.value >= 10).all()
    
    # TODO : 
    # results_2nd_pull = Place.query.all()

    return render_template('home.html', tuple_list=tuple_list, gte10_list=results, city=city, parameter=parameter)




@APP.route('/refresh')
def refresh():
    root()
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()

    #
    # TODO: ETL pipeline data from csv to sqlite
    #

    # # Example of looping through a list, row by row
    # for i in range(len(tuple_list)):   
    #     list_new = Record(id=i, datetime=date_utc[i], value=value[i])
    #     DB.session.add(list_new)
    

    # STORE IN DATABASE
    DB.session.commit()
    
    return render_template('refresh.html')


@APP.route('/reset')
def reset():
    DB.drop_all()
    DB.create_all()
    # return render_template('base.html', title='Database has been Reset!', users=User.query.all())
    return 'Database has been reset'