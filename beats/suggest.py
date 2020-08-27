import pickle
import pandas as pd



filename = 'beats\\testing_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
songs_new = pd.read_pickle("beats\\ML_model_db.pkl")


def find_recommended_songs(audio_features):
    neighbors = loaded_model.kneighbors([audio_features]) #.reshape(1, -1)
    new_obs = neighbors[1][0][6:20]
    return list(songs_new.loc[new_obs, 'id'])
  