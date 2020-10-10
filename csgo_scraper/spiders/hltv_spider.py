import scrapy

from scrapy.loader import ItemLoader
from csgo_scraper.items import TeamItem


class HLTVSpider(scrapy.Spider):
    name = 'hltv_spider'
    allowed_domains = ['https://www.hltv.org']
    start_urls = ['https://www.hltv.org/ranking/teams/']

    def parse(self, response):
        for team in response.css('.ranked-team'):
            team_item_loader = ItemLoader(item=TeamItem())
            team_item_loader.add_value('name', team.css('.team-logo').xpath('img/@alt').get())
            team_item_loader.add_value('image_url', team.css('.team-logo').xpath('img/@src').get())
            yield team_item_loader.load_item()
