import os
import scrapy
from scrapy.crawler import CrawlerProcess

class WikiSpider(scrapy.Spider):
    name = 'wiki-spider'
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
        'https://quotes.toscrape.com/page/3/',
        'https://quotes.toscrape.com/page/4/',
        'https://quotes.toscrape.com/page/5/',
        'https://quotes.toscrape.com/page/6/',
        'https://quotes.toscrape.com/page/7/',
        'https://quotes.toscrape.com/page/8/',
        'https://quotes.toscrape.com/page/9/',
        'https://quotes.toscrape.com/page/10/',
        ]

    def parse(self, response):
        # Ensure the 'html' folder exists
        os.makedirs('html', exist_ok=True)

        # Specify the path including the 'html' folder
        filename = os.path.join('html', 'quotes.html')

        # Open the file in append mode and write the response body
        with open(filename, 'ab') as f:
            f.write(response.body)
            self.log(f'Appended content to {filename}')

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(WikiSpider)
    process.start()
