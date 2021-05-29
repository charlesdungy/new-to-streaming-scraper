from config.config import config
from datetime import datetime
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
        except Error as e:
            logging.error(e)

    def insert_movies(self):
        """ """
        sql_stmt = ('INSERT INTO MOVIE (Rotten_Tomatoes_ID, Title, '       
                    'Tomato_score, Release_date, Runtime, URL) '
                    'VALUES (%s, %s, %s, %s, %s, %s)')

        file_path = '../../data/processed/movies.csv'
        self.place_into_db(file_path, sql_stmt)

    def insert_actors(self):
        """ """
        sql_stmt = ('INSERT INTO ACTOR (Rotten_Tomatoes_ID, Actor) '       
                    'VALUES (%s, %s)')

        file_path = '../../data/processed/actors.csv'
        self.place_into_db(file_path, sql_stmt)

    def insert_new_to_netflix(self):
        """ """
        sql_stmt = ('INSERT INTO NETFLIX (Title, Date_arriving, '       
                    'Title_type, Release_year, Season, Weekly) '
                    'VALUES (%s, %s, %s, %s, %s, %s)')

        current_time = datetime.now()
        current_month_text = current_time.strftime('%b').lower()
        
        file_name = f'../../data/processed/netflix_{current_month_text}.csv'
        self.place_into_db(file_name, sql_stmt)

    def insert_movie_score_data(self):
        """ """
        sql_stmt = ('INSERT INTO MOVIE_SCORE_DATA (Title, '
            'Title_year, Movie_score, Title_category, Runtime, URL) '
            'VALUES (%s, %s, %s, %s, %s, %s)')

        file_name = '../../data/processed/movie_score_data.csv'
        self.place_into_db(file_name, sql_stmt)

    def place_into_db(self, file_name, sql_stmt):
        """ """
        cursor = self.cnx.cursor()
        with open(file_name) as obj_file:
            obj_reader = csv.reader(obj_file)
            next(obj_reader, None)
            for row in obj_reader:
                try:
                    cursor.execute(sql_stmt, row)
                except Error as e:
                    logging.error(e)
            self.cnx.commit()

    def close_connection(self):
        """ """
        self.cnx.close()
        self.cursor.close()

x = PipeToDB()
x.insert_movies()
x.insert_actors()
x.insert_new_to_netflix()
x.insert_movie_score_data()
x.close_connection()