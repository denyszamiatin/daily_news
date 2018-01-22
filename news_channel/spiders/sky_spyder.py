import scrapy
import re
from selenium import webdriver


class RSpider(scrapy.Spider):
    name = 'sky_spider'

    for word in ['europe']:
        start_urls = ['https://news.sky.com/search?q={}&sortby=date'.format(word)]
    # start_urls = ['https://news.sky.com/search?q=europe&sortby=date']

    def parse(self, response):
        for next_page in response.xpath('//h2[@class = "sdc-news-listing__headline"]/a'):
            yield response.follow(next_page, self.parse_news)

    def parse_news(self, response):
        title = response.xpath('//h1/span/text()').extract()
        date = response.xpath('//p/time/span/text()').extract()
        text = response.xpath('//div[@class = "sdc-news-story-article__body"]/p').extract()
        yield {'title': title, 'date': ', '.join(date), 'text': text}
