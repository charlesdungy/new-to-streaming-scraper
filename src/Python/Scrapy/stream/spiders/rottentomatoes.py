import csv
import json
import scrapy

class RottenTomatoesSpider(scrapy.Spider):
    """ """
    name = 'rottentomatoes'
    allowed_domains = ['rottentomatoes.com']
    start_urls = []
    
    """ """
    with open('../../../../data/processed/rotten_tomatoes_search_url.csv') as   url_file:
        url_reader = csv.reader(url_file, delimiter=',')
        next(url_reader, None)
        for row in url_reader:
            start_urls.append(row[1])

    def parse(self, response):
        """ """
        resp = json.loads(response.body)
        movies = resp.get('movies')
        
        for movie in movies:
            movie_url = 'https://www.rottentomatoes.com' + movie.get('url')
            yield scrapy.Request(movie_url, callback=self.parse_movie)

    def parse_movie(self, response):
        """ """
        movie = response.xpath(("//div[@id='topSection']//score-board/h1/"
                                "text()")).extract()[0]
        score = response.xpath(("//div[@id='topSection']//score-board"
                                "/@tomatometerscore")).extract()[0]
        details = response.xpath(("//div[@id='topSection']"
                                  "//score-board/p/text()")).extract()[0]
        url = response.request.url

        yield {
            'Title': movie,
            'Score': score,
            'Details': details,
            'URL': url,
        }