import pandas as pd 
import numpy as np 

class CleanRottenTomatoesJSON:
    def __init__(self):
        self.df = pd.read_json('../../data/raw/rotten_tomates_movie_data.json')

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
        return df_no_actors

    def get_df_actors(self):
        """ """
        columns_actors = ['id', 'actors']
        df_actors = self.df[columns_actors]
        return df_actors

    def explode_actors(self, df_actors):
        """ """
        df_actors = df_actors.explode('actors')
        return df_actors

df = CleanRottenTomatoesJSON()

df_no_actor = df.no_actors()
df_no_actor = df.clean_no_actors(df_no_actor)
df_no_actor.to_csv('../../data/processed/movies.csv', index=False)

df_actor = df.get_df_actors()
df_actor = df.explode_actors(df_actor)
df_actor.to_csv('../../data/processed/actors.csv', index=False)