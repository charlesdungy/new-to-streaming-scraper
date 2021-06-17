from datetime import datetime
import pandas as pd
import scrapy

class WhatsOnNetflixSpider(scrapy.Spider):
    name = 'whatsonnetflix'
    allowed_domains = ['https://www.whats-on-netflix.com']
    start_urls = [("https://www.whats-on-netflix.com/coming-soon"
                   "/whats-coming-to-netflix-in-june-2021-06-16/")]

    def parse(self, response):
        """ """
        movie_and_date_stacked = response.xpath(("//div[@class='entry-inner']"
                                                 "//h4/text()|//ul/li/strong"
                                                 "/text()")).getall()
        self.write_to_csv(movie_and_date_stacked)

    def write_to_csv(self, item):
        """ """
        current_month = datetime.now().strftime('%B').lower()
        df = pd.DataFrame(item)
        df.to_csv((f'../../../../../data/raw/whatsonnetflix_{current_month}'
                    '.csv'), mode='w')