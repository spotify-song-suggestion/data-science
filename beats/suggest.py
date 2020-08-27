import pickle
import pandas as pd


#ImportError: cannot import name 'loaded_model' from partially initialized module 'beats.app' (most likely due to a circular import) (C:\Users\jeffr\mystuff\data-science\beats\app.py)

#Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.


filename = 'beats\\testing_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
songs_new = pd.read_pickle("beats\\ML_model_db.pkl")
# def clean_data_for_model(audio_feature_response):
  
#   wanted_features = ['danceability', 'instrumentalness',	'loudness',	'speechiness',	'valence']
#   input_track_audio_features_dict = track_features[0]

#   features_nums = []
#   for feature in wanted_features:
#     features_nums.append(input_track_audio_features_dict[feature])


#    model_input = [features_nums] 

#    df_new = pd.DataFrame(model_input, columns= wanted_features)
# #   df_new.head()
#    series = df_new.iloc[0, 0:].to_numpy() # audio 
# #   return series

def find_recommended_songs(audio_features):
    neighbors = loaded_model.kneighbors([audio_features]) #.reshape(1, -1)
    new_obs = neighbors[1][0][6:20]
    return list(songs_new.loc[new_obs, 'id'])
  