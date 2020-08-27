# Copied from DS U3S2 DS 15 with Mike Rossetti
from os import getenv
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
from sqlalchemy import create_engine

load_dotenv() # looks inside the .env file for some env vars

# passes env var values to python var


# DONE TODO get from Heroku 
DB_HOST = getenv("DB_HOST", default="OOPS")
DB_NAME = getenv("DB_NAME", default="OOPS")
DB_USER = getenv("DB_USER", default="OOPS")
DB_PASS = getenv("DB_PASS", default="OOPS")
DATABASE_URL = getenv("DATABASE_URL", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, 
                              user=DB_USER, 
                              password=DB_PASS, 
                              host=DB_HOST)
cursor = connection.cursor()

def create_tables():
    create_query = """
        DROP TABLE IF EXISTS song; -- allows this to be run idempotently, avoids psycopg2.error
        CREATE TABLE IF NOT EXISTS song (
                           acousticness NUMERIC, 
                           artists TEXT, 
                           danceability NUMERIC, 
                           duration_ms NUMERIC, 
                           energy NUMERIC, 
                           explicit NUMERIC, 
                           id TEXT, 
                           instrumentalness NUMERIC, 
                           key INTEGER, 
                           liveness NUMERIC, 
                           loudness NUMERIC, 
                           mode INTEGER, 
                           name TEXT, 
                           popularity NUMERIC, 
                           release_date TEXT, 
                           speechiness NUMERIC, 
                           tempo NUMERIC, 
                           valence NUMERIC, 
                           year NUMERIC);"""
    print(create_query)
    cursor.execute(create_query)

    df = pd.read_csv('csv/data.csv')

    engine = create_engine(DATABASE_URL)
    df.to_sql('song', engine)

    connection.commit()

# def insert_characters(characters):
#     """
#     Param characters needs to be a list of tuples, each representing a row to insert (each should have a each column)
#     """

#     # TODO for future check if a duplicate row before adding
#     insertion_query = """
#         INSERT INTO characters (character_id, name, level, exp, hp, strength, intelligence, dexterity, widsom)
#         VALUES %s ;
#     """
#     execute_values(cursor, insertion_query, characters)
#     connection.commit()


# if __name__ == "__main__":

#     #
#     # EXTRACT AND TRANSFORM
#     #

#     sqlite_service = SQLiteService()

#     characters = sqlite_service.fetch_characters()
#     print(type(characters), len(characters))
#     print(type(characters[0]), characters[0])

#     #
#     # LOAD
#     #

#     pg_service = ElephantSQLService()

#     pg_service.create_characters_table()

#     pg_service.insert_characters(characters)
