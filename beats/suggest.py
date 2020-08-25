'''Prediction of Users based on Tweet embeddings'''
# import numpy as np
# from sklearn.linear_model import LogisticRegression
# from .db_model import User


# def suggest_songs(name, acousticness, danceability,	energy,	instrumentalness, liveness,	loudness, speechiness,	tempo,	valence):
def suggest_songs(song):
    '''Recommend and return which songs are more likely be similar to given song.
    
    # Arguments:
        song.name
        song.ac
        

    # Returns:
        Recommendations of Songs from neural netwoks model
    '''

    labels 
    features

    # Train model and convert input text to embedding
    model = LogisticRegression(max_iter=1000).fit(embeddings, labels)
    
    return model.predict([tweet_embedding])[0]