import scrapy
import json

class RottenTomatoesSpider(scrapy.Spider):
    name = 'rottentomatoes'
    allowed_domains = ['rottentomatoes.com/']
    start_urls = ['https://www.rottentomatoes.com/api/private/v2.0/browse?     maxTomato=100&services=netflix_iw&certified&sortBy=release& type=dvd-streaming-all&page=1']
    page = 1

    def parse(self, response):
        """ """
        resp = json.loads(response.body)
        movies = resp.get('results')
        
        for movie in movies:
            yield {
                'movie': movie.get('title'),
                'tomato_score': movie.get('tomatoScore'),
                'release_date': movie.get('dvdReleaseDate'),
                'synopsis': movie.get('synopsis'),
                'actors': movie.get('actors'),
                'runtime': movie.get('runtime'),
                'url': movie.get('url'),
                'id': movie.get('id')
            }
        
        check_count = resp.get('counts').get('count')
        if (check_count > 0):
            self.page += 1
            yield scrapy.Request (
                url = f'https://www.rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&services=netflix_iw&certified&sortBy=release&type=dvd-streaming-all&page={self.page}',
                callback = self.parse,
                dont_filter = True 
            )