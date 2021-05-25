import scrapy
import pandas as pd

class WhatsOnNetflixSpider(scrapy.Spider):
    name = 'whatsonnetflix'
    allowed_domains = ['https://www.whats-on-netflix.com']
    start_urls = ['https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-april-2021-04-11/']

    def parse(self, response):
        """ """
        movie_and_date_stacked = response.xpath("//div[@class='entry-inner']//h4/text()|//ul/li/strong/text()").getall()
        self.write_to_csv(movie_and_date_stacked)

    def write_to_csv(self, item):
        """ """
        df = pd.DataFrame(item)
        df.to_csv('../../data/raw/whatsonnetflix.csv')