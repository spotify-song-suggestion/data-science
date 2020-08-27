# # Copied from DS U3S2 DS 15 with Mike Rossetti
# from os import getenv
# from dotenv import load_dotenv
# import psycopg2
# from psycopg2.extras import execute_values
# import pandas as pd
# from sqlalchemy import create_engine

# load_dotenv() # looks inside the .env file for some env vars

# # passes env var values to python var


# # DONE TODO get from Heroku 
# DB_HOST = getenv("DB_HOST")
# DB_NAME = getenv("DB_NAME")
# DB_USER = getenv("DB_USER")
# DB_PASS = getenv("DB_PASS")
# DATABASE_URL = getenv("DATABASE_URL")

# connection = psycopg2.connect(dbname=DB_NAME, 
#                               user=DB_USER, 
#                               password=DB_PASS, 
#                               host=DB_HOST)
# cursor = connection.cursor()

# def create_tables():
#     create_query = """
#         DROP TABLE IF EXISTS song; -- allows this to be run idempotently, avoids psycopg2.error
#         CREATE TABLE IF NOT EXISTS song (
#                            acousticness NUMERIC, 
#                            artists TEXT, 
#                            danceability NUMERIC, 
#                            duration_ms NUMERIC, 
#                            energy NUMERIC, 
#                            explicit NUMERIC, 
#                            id TEXT, 
#                            instrumentalness NUMERIC, 
#                            key INTEGER, 
#                            liveness NUMERIC, 
#                            loudness NUMERIC, 
#                            mode INTEGER, 
#                            name TEXT, 
#                            popularity NUMERIC, 
#                            release_date TEXT, 
#                            speechiness NUMERIC, 
#                            tempo NUMERIC, 
#                            valence NUMERIC, 
#                            year NUMERIC);"""
#     print(create_query)
#     cursor.execute(create_query)

#     df = pd.read_csv('csv/data.csv')

#     engine = create_engine(DATABASE_URL)
#     df.to_sql('song', engine, if_exists='append', index=False)

#     connection.commit()


# if __name__ == '__main__':
#     create_tables()
#     print("Got this!!!")