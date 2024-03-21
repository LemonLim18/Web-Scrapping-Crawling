from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# inherit from CrawlSpider class
class CrawlingSpider(CrawlSpider):
    # set a name to the spider
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    # define proxy_server
    PROXY_SERVER = "127.0.0.1"

    # filtering rule
    # Web Crawling: retrieve URLs based on the rules
    # Definition:  Web crawling is a process of searching links that can be found based on the rules,
    # with the rule defining which area they are allowed or restricted(denied access) to do the crawling.
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        # Allow all the URLs that have the catalog in them but I want to deny all the URLs that have the category in them
        # when the URLs are found, they will be referred to the function called 'parse_item' 
        # , meaning to let the function/method parse_item to handle all the link instances successfully retrieved.
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    )

    # Web Scraping: retrieve desired information
    def parse_item(self, response):
        # dont return the value, but generate it
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            # [1] retrieves the second element matched by the same CSS selector.
            # replace() method in this case remove the unnecessary newline and space.
            "availability": response.css(".availability::text")[1].get().replace("\n","").replace(" ","")
        }

# Note: Some websites would block you after identifying your IP addess
#       if you are scraping their website too frequently as they don't want you to do that.
#       So, you might want to use a proxy server to avoid being blocked.
#       as the proxy server sends the request using their IP address, not yours.