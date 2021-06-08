import pandas as pd

class BuildSearchURL:
    def __init__(self):
        """ """
        self.df = pd.read_csv('../../data/processed/netflix_april.csv')

    def create_search_url(self):
        """ """
        df_title = pd.DataFrame(self.df.Title)
        df_title['search_url'] = df_title.Title.replace(to_replace=['\s+'], 
                                                        value='%20', 
                                                        regex=True)
        df_title['search_url'] = ("https://www.rottentomatoes.com/api"
                                  "/private/v2.0/search/?limit=20&q=") + df_title['search_url']
        self.write_to_csv(df_title)

    def write_to_csv(self, df):
        """ """
        df.to_csv('../../data/processed/rotten_tomatoes_search_url.csv',    
                  index=False)

def main():
    x = BuildSearchURL()
    x.create_search_url()

if __name__ == '__main__':
    main()