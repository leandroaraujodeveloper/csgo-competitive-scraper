import scrapy

from scrapy.loader import ItemLoader
from csgo_scraper.items import TeamItem

CSGO_ACTIVE_TEAMS_TABLE = 0
CSGO_DISBANDED_TEAMS_TABLE = 1

class LiquidpediaSpider(scrapy.Spider):
    name = 'liquidpedia_spider'
    allowed_domains = ['https://liquipedia.net/counterstrike']
    start_urls = ['https://liquipedia.net/counterstrike/Portal:Teams']

    def parse(self, response):
        for team in response.xpath('//table')[CSGO_ACTIVE_TEAMS_TABLE].xpath('tbody/tr/td/div/ul/li/span'):
            team_item_loader = ItemLoader(item=TeamItem())
            team_item_loader.add_value('name', team.xpath('@data-highlightingclass').get())
            team_item_loader.add_value('image_url', 'https://liquipedia.net/'+team.xpath('.//img/@src').get())
            yield team_item_loader.load_item()
