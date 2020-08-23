
import csv
import sqlite3
import pandas as pd

"""csv to sqlite3 etl pipeline"""
con = sqlite3.connect('song.sqlite3')
cur = con.cursor()

# TODO check types with spotify.py
cur.execute("""CREATE TABLE  song (acousticness NUMERIC, artists TEXT, 
            danceability NUMERIC, duration_ms NUMERIC, energy NUMERIC, 
            explicit NUMERIC, id TEXT, instrumentalness NUMERIC, key INTEGER, 
            liveness NUMERIC, loudness NUMERIC, mode INTEGER, name TEXT, 
            popularity NUMERIC, release_date TEXT, speechiness NUMERIC, 
            tempo NUMERIC, valence NUMERIC, year NUMERIC);""")

df = pd.read_csv('csv/data.csv')
df.to_sql('song', con, if_exists='append', index=False)