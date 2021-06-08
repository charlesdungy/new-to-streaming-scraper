import pandas as pd 
import numpy as np 

class CleanMovieScoreDataJSON:
    def __init__(self):
        self.df = pd.read_json('../../data/raw/movie_score_data.json')

    def no_actors(self):
        """ """
        columns_no_actors = ['id', 'movie', 'tomato_score', 
                             'release_date', 'runtime', 'url'
                            ]
        df_no_actors = self.df[columns_no_actors]
        return df_no_actors
    
    def clean_no_actors(self, df_no_actors):
        """ """
        df_no_actors = df_no_actors.fillna(value = np.nan)
        df_no_actors.runtime = df_no_actors.runtime.fillna('')
        df_no_actors = df_no_actors.drop_duplicates(subset=['id'], keep='last')
        return df_no_actors

    def get_df_actors(self):
        """ """
        columns_actors = ['id', 'actors']
        df_actors = self.df[columns_actors]
        return df_actors

    def explode_actors(self, df_actors):
        """ """
        df_actors = df_actors.explode('actors')
        df_actors = df_actors.drop_duplicates(
            subset=['id', 'actors'], 
            keep='last'
        )
        return df_actors

def main():
    df = CleanMovieScoreDataJSON()

    df_no_actor = df.no_actors()
    df_no_actor = df.clean_no_actors(df_no_actor)
    df_no_actor.to_csv('../../data/processed/movies.csv', index=False)

    df_actor = df.get_df_actors()
    df_actor = df.explode_actors(df_actor)
    df_actor.to_csv('../../data/processed/actors.csv', index=False)

if __name__ == '__main__':
    main()