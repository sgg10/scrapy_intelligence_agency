import scrapy
from intelligence_agency.spiders.common import config

class SpiderCia(scrapy.Spider):
    name = 'cia'
    start_urls = [
        config()["agency_sites"]["cia"]["url"]
    ]
    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        "FEED_EXPORT_ENCODING": "utf-8"
    }

    def __init__(self):
        self.queries = config()["agency_sites"]["cia"]["queries"]

    def parse(self, response):
        declassified_links = response.xpath(self.queries["declassified_links"]).getall()
        for link in declassified_links:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs["url"]
        title = response.xpath(self.queries["declassified_title"]).get()
        paragraph = response.xpath(self.queries["declassified_paragraph"]).get()

        yield {
            "url": link,
            "title": title,
            "body": paragraph
        }
