from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# inherit from CrawlSpider class
class CrawlingSpider(CrawlSpider):
    # set a name to the spider
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    # filtering rule
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        # Allow all the URLs that have the catalog in them but I want to deny all the URLs that have the category in them
        # when the URLs are found, they will be referred to the function called 'parse_item' 
        # , meaning to let the function/method parse_item to handle all the link instances successfully retrieved.
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    )