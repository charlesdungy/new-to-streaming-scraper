import csv
import json
import scrapy

class RottenTomatoesSpider(scrapy.Spider):
    """ """
    name = 'rottentomatoes'
    allowed_domains = ['rottentomatoes.com']
    start_urls = []
    
    """ """
    with open('../../../../../data/processed/rotten_tomatoes_search_url.csv') as   url_file:
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
        critic_score = response.xpath(("//div[@id='topSection']//score-board"
                                       "/@tomatometerscore")).extract()[0]
        audience_score = response.xpath(("//div[@id='topSection']//score-board"
                                         "/@audiencescore")).extract()[0]
        details = response.xpath(("//div[@id='topSection']"
                                  "//score-board/p/text()")).extract()[0]
        rating = response.xpath(("//div[@id='topSection']//score-board"
                                 "/@rating")).extract()[0]
        poster_url = response.xpath(("//div[@id='topSection']//div//div"
                                     "[@class='center']//img/"
                                     "@data-src")).extract()[0]
        url = response.request.url

        yield {
            'Title': movie,
            'Critic_score': critic_score,
            'Audience_score': audience_score,
            'Details': details,
            'Rating': rating,
            'URL': url,
            'Poster_URL': poster_url
        }