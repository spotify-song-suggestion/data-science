>>> from beats.db_model import db, Song
>>> db.init_app(app)
>>> db.create_all()
>>> db #<SQLAlchemy engine=sqlite:///C:\Users\jeffr\mystuff\data-science\beats\song.sqlite3>
>>> Song #<class 'beats.db_model.Song'>
>>> Song.query.filter_by(Song.id=='6llUzeoGSQ53W3ThFbReE2').all() # gives all db


# this is the code to get info
>>> Song.query.get('6llUzeoGSQ53W3ThFbReE2')
< Title  'Young and Fine' - Artist  "['Weather Report']" - Duration(ms) 413587.0 >

# note one feature from radar Plots is missing
['danceability',  'instrumentalness', 'loudness', 'speechiness',  'valence'] 


>>> Song.query.get('6llUzeoGSQ53W3ThFbReE2')
< Title  'Young and Fine' - Artist  "['Weather Report']" - Duration(ms) 413587.0 - A - 0.725 - D  0.371 - I 0.000139 - L -9.952 - S 0.0488 - V 0.6729999999999999 >