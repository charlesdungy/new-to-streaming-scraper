import pandas as pd 
import numpy as np 

class CleanMonthlyMovieScoresJSON:
    def __init__(self):
        """ """
        self.df = pd.read_json('../../data/raw/april_movie_scores.json')

    def clean_scores(self):
        """ """
        self.df.Score.replace("", "NR", regex=True, inplace=True)

    def clean_details(self):
        """ """
        self.df['Year'] = self.df.Details.str.split(",").str[0]
        self.df['Title_Category'] = self.df.Details.str.split(",").str[1]
        self.df['Runtime'] = self.df.Details.str.split(",").str[2]
        self.df.drop('Details', axis=1, inplace=True)

    def order_columns(self):
        """ """
        columns = ['Title', 'Year', 'Score', 'Title_Category', 'Runtime', 'URL']
        self.df = self.df[columns]

    def omit_duplicates(self):
        """ """
        self.df = self.df.drop_duplicates(subset=['Title',
                                                  'Year',
                                                  'Title_Category', 
                                                  'Runtime'],
                                          keep='last')

    def write_to_csv(self):
        """ """
        self.df.to_csv('../../data/processed/movie_score_data.csv', index=False)

x = CleanMonthlyMovieScoresJSON()
x.clean_scores()
x.clean_details()
x.order_columns()
x.omit_duplicates()
x.write_to_csv()