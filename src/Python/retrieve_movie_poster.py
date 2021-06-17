import urllib.request       
from config.config_ import config
from current_month import CurrentMonth
from datetime import datetime
from mysql.connector import connect, Error
import logging
import pandas as pd

class RetrieveMoviePoster:
    def __init__(self):
        """ """
        self.current_month = CurrentMonth.CURRENT_MONTH.lower()
        self.df = None

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
        
    def get_poster_url_from_db(self):
        """ """
        current_month_int = CurrentMonth.CURRENT_MONTH_INT
        sql_stmt = ('SELECT N.Title, N.Release_year, M.Critic_score, '
                    'M.Audience_score, M.Poster_URL '
                    'FROM NETFLIX N LEFT JOIN MOVIE_SCORE_DATA M ON '
                    'M.Title=N.Title AND M.Title_year=N.Release_year '
                    'WHERE N.Title_type="Movie" AND M.Poster_URL NOT '
                    'LIKE "%.gif" AND M.Poster_URL<>"" AND MONTH(Date_Arriving'
                    f')={current_month_int}')
        
        self.df = pd.read_sql(sql_stmt, self.cnx)
        self.cnx.close()

    def download_movie_poster(self):
        """ """
        file_paths = []
        for _, row in self.df.iterrows():
            file_path = ("../../data/images/{0}/{1}_{2}_{3}_{4}.jpg".format(
                self.current_month,
                row['Title'], 
                row['Release_year'], 
                row['Critic_score'], 
                row['Audience_score'])).replace(' ', '_')

            bad_url = False
            try:
                urllib.request.urlretrieve(row['Poster_URL'], file_path)
            except:
                bad_url = True
                logging.error("error with downloading movie poster: " + row['Poster_URL'])

            if (bad_url is False):
                file_paths.append(file_path)
            else:
                file_paths.append("")

        self.df['File_path'] = file_paths

    def write_to_csv(self):
        """ """
        save_df = self.df[['Poster_URL', 'File_path']]
        save_df.to_csv(f'''../../data/processed/movie_poster_data_{self.current_month}.csv''', index=False)

def main():
    x = RetrieveMoviePoster()
    x.get_poster_url_from_db()
    x.download_movie_poster()
    x.write_to_csv()

if __name__ == '__main__':
    main()