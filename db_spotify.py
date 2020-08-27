"""Spotify Suggested Playlist Dashboard with Flask."""
from flask_sqlalchemy import SQLAlchemy

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


class History(db.Model):
    # is this a foreign key and how to link the tables
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100))
    acousticness  = db.Column(db.Float)	
    danceability = db.Column(db.Integer)	
    energy = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)	
    liveness = db.Column(db.Float)	
    loudness = db.Column(db.Float)	
    speechiness	= db.Column(db.Float)
    tempo = db.Column(db.Float)	
    valence = db.Column(db.Float)





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
