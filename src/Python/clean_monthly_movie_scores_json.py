from current_month import CurrentMonth
import numpy as np 
import pandas as pd 

class CleanMonthlyMovieScoresJSON:
    def __init__(self):
        """ """
        self.current_month = CurrentMonth.CURRENT_MONTH.lower()
        self.df = pd.read_json(f'''../../data/raw/{self.current_month}_movie_scores.json''')

    def replace_blank_values(self):
        """ """
        self.df.replace("", np.NaN, inplace=True)

    def replace_missing_scores(self):
        """ """
        self.df.Critic_score.replace(np.NaN, "NR", inplace=True)
        self.df.Audience_score.replace(np.NaN, "NR", inplace=True)
        
    def replace_missing_ratings(self):
        """ """
        self.df.Rating.replace(np.NaN, "NR", inplace=True)

    def transform_details(self):
        """ """
        self.df['Year'] = self.df.Details.str.split(",").str[0].str.strip()
        self.df['Title_category'] = self.df.Details.str.split(",").str[1]
        self.df['Title_category'] = self.df.Title_category.str.strip()
        self.df['Runtime'] = self.df.Details.str.split(",").str[2].str.strip()
        self.df.drop('Details', axis=1, inplace=True)

    def order_columns(self):
        """ """
        columns = ['Title', 
                   'Year', 
                   'Critic_score', 
                   'Audience_score', 
                   'Title_category',
                   'Rating', 
                   'Runtime', 
                   'URL', 
                   'Poster_URL']
        self.df = self.df[columns]

    def omit_duplicates(self):
        """ """
        self.df = self.df.drop_duplicates(subset=['Title', 
                                                  'Year', 
                                                  'Critic_score', 'Audience_score'],
                                          keep='last')

    def write_to_csv(self):
        """ """
        self.df.to_csv(f'''../../data/processed/movie_score_data_{self.current_month}.csv''', index=False)

def main():
    x = CleanMonthlyMovieScoresJSON()
    x.replace_blank_values()
    x.replace_missing_scores()
    x.replace_missing_ratings()
    x.transform_details()
    x.order_columns()
    x.omit_duplicates()
    x.write_to_csv()

if __name__ == '__main__':
    main()