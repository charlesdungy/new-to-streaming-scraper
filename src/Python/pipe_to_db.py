from config.config import config
from mysql.connector import connect, Error

import csv
import logging

class PipeToDB:
    def __init__(self):
        """ """
        logging.basicConfig(
            filename='logs/db.log',
            encoding='utf-8', 
            level=logging.ERROR,
            filemode='a'
        )

        try:
            self.cnx = connect(**config)
            self.cursor = self.cnx.cursor()
        except Error as e:
            logging.error(e)

    def insert_movies(self):
        """ """
        sql_stmt = ('INSERT INTO MOVIE (Rotten_Tomatoes_ID, Title, '       
                    'Tomato_score, Release_date, Runtime, URL) '
                    'VALUES (%s, %s, %s, %s, %s, %s)')

        with open('../../data/processed/movies.csv') as movie_file:
            movie_reader = csv.reader(movie_file)
            next(movie_reader, None)
            for row in movie_reader:
                try:
                    self.cursor.execute(sql_stmt, row)
                except Error as e:
                    logging.error(e)
            self.cnx.commit()

    def insert_actors(self):
        """ """
        sql_stmt = ('INSERT INTO ACTOR (Rotten_Tomatoes_ID, Actor) '       
                    'VALUES (%s, %s)')

        with open('../../data/processed/actors.csv') as actor_file:
            actor_reader = csv.reader(actor_file)
            next(actor_reader, None)
            for row in actor_reader:
                try:
                    self.cursor.execute(sql_stmt, row)
                except Error as e:
                    logging.error(e)
            self.cnx.commit()

    def close_connection(self):
        """ """
        self.cnx.close()
        self.cursor.close()

x = PipeToDB()
#x.insert_movies()
#x.insert_actors()
x.close_connection()