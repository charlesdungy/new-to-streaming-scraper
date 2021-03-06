from config.config_ import config
from current_month import CurrentMonth
from datetime import datetime
from mysql.connector import connect, Error

import csv
import logging

class PipeToDB:
    def __init__(self):
        """ """
        self.current_month = CurrentMonth.CURRENT_MONTH.lower()

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
            quit()

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

        file_name = f'../../data/processed/netflix_{self.current_month}.csv'
        self.place_into_db(file_name, sql_stmt)

    def insert_movie_score_data(self):
        """ """
        sql_stmt = ('INSERT INTO MOVIE_SCORE_DATA (Title, '
                    'Title_year, Critic_score, Audience_score, ' 'Title_category, Rating, Runtime, URL, Poster_URL) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)')

        file_name = f'''../../data/processed/movie_score_data_{self.current_month}.csv'''
        self.place_into_db(file_name, sql_stmt)

    def insert_movie_poster_data(self):
        """ """
        sql_stmt = ('INSERT INTO MOVIE_POSTER_DATA (Poster_URL, '
                    'Poster_file_path) VALUES (%s, %s)')

        file_name = f'''../../data/processed/movie_poster_data_{self.current_month}.csv'''
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
            cursor.close()

    def close_connection(self):
        """ """
        self.cnx.close()

def main():
    x = PipeToDB()
    x.insert_new_to_netflix()
    x.insert_movie_score_data()
    x.insert_movie_poster_data()
    x.close_connection()

if __name__ == '__main__':
    main()
