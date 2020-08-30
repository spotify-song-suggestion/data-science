
# import csv
# import sqlite3
# import pandas as pd

# """csv to sqlite3 etl pipeline"""
# con = sqlite3.connect('song.sqlite3')
# cur = con.cursor()



# create_query = """
#     DROP TABLE IF EXISTS song; -- allows this to be run idempotently, avoids psycopg2.error
#     CREATE TABLE IF NOT EXISTS song (
#                         acousticness NUMERIC, 
#                         artists TEXT, 
#                         danceability NUMERIC, 
#                         duration_ms NUMERIC, 
#                         energy NUMERIC, 
#                         explicit NUMERIC, 
#                         id TEXT, 
#                         instrumentalness NUMERIC, 
#                         key INTEGER, 
#                         liveness NUMERIC, 
#                         loudness NUMERIC, 
#                         mode INTEGER, 
#                         name TEXT, 
#                         popularity NUMERIC, 
#                         release_date TEXT, 
#                         speechiness NUMERIC, 
#                         tempo NUMERIC, 
#                         valence NUMERIC, 
#                         year NUMERIC);"""

# cur.execute(create_query)




# df = pd.read_csv('csv/data.csv')
# df.to_sql('song', con, if_exists='append', index=False)
# con.commit()


