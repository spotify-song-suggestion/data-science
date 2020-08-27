# """Spotify Suggested Playlist Dashboard with Flask."""
# from flask_sqlalchemy import SQLAlchemy



# db = SQLAlchemy()


# # This class is based off the data.csv file
# # TODO check types with etl_pipeline.py
# class Song(db.Model):
#     acousticness = db.Column(db.Float)  # A
#     artists = db.Column(db.String(75))  # B
#     danceability = db.Column(db.Integer)  # C
#     duration_ms = db.Column(db.Float)  # D
#     energy = db.Column(db.Float)  # E
#     explicit = db.Column(db.Float)  # F
#     id = db.Column(db.String(100), primary_key=True)  # G
#     instrumentalness = db.Column(db.Float)  # H
#     key = db.Column(db.Integer)  # I
#     liveness = db.Column(db.Float)  # J
#     loudness = db.Column(db.Float)  # K
#     mode = db.Column(db.Integer)  # L
#     name = db.Column(db.String(100))  # M Label
#     popularity = db.Column(db.Integer)  # N
#     release_date = db.Column(db.String(20))  # O
#     speechiness = db.Column(db.Float)  # P
#     tempo = db.Column(db.Float)  # Q
#     valence = db.Column(db.Float)  # R
#     year = db.Column(db.Integer)  # S

#     # def __repr__(self):
#     #     # write a nice representation of Song'
#     #     return '< Title  %r - Artist  %r - Duration(ms) %r - A - %r - D  %r - I %r - L %r - S %r - V %r >' % (self.name,
#     #                                                              self.artists,
#     #                                                              self.duration_ms,
#     #                                                              self.acousticness,
#     #                                                              self.danceability,
#     #                                                              self.instrumentalness,
#     #                                                              self.loudness,
#     #                                                              self.speechiness,
#     #                                                              self.valence)
#     def __repr__(self):
#         # write a nice representation of Song'
#         return '< Title  %r - Artist  %r - Duration(ms) %r >' % (self.name,
#                                                                     self.artists,
#                                                                     self.duration_ms)

# # features used in suggest.py model
# #['danceability',  'instrumentalness', 'loudness', 'speechiness',  'valence']

# class History(db.Model):
#     # is this a foreign key and how to link the tables
#     id = db.Column(db.String, primary_key=True)
#     name = db.Column(db.String(100))
#     acousticness  = db.Column(db.Float)	
#     danceability = db.Column(db.Integer)	
#     energy = db.Column(db.Float)
#     instrumentalness = db.Column(db.Float)	
#     liveness = db.Column(db.Float)	
#     loudness = db.Column(db.Float)	
#     speechiness	= db.Column(db.Float)
#     tempo = db.Column(db.Float)	
#     valence = db.Column(db.Float)
