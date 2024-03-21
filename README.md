# SHORT NOTE: Web Scraping and Crawling

## Definitions
- **Web Scraping**: Extracting data from a website.
- **Web Crawling**: Finding links/URL branches off a website.
  
![image](https://github.com/LemonLim18/Web-Scrapping-Crawling/assets/116692908/bd21774e-d57a-44e2-b1f9-394466fbc5c7)

## Scrapy

Scrapy is a Python framework for web scraping that provides all the tools you need for extracting data from websites, processing it, and storing it in your preferred structure.

### response.css()

`response.css()` in Scrapy is more or less similar to `document.getElementByInnerHTML()`. However, `response.css()` only gets the object in the form of a list.

For example, `response.css().get()` retrieves the first line of code with the identifier, and `response.css("h3"::text).get()` retrieves the text within the first h3 tag.

### response.xpath()

`response.xpath("//a/text()").extract()` uses XPath to select all the text nodes ('text()') that are children of '<a>' elements ('//a'). The `.extract()` method means extracting the data selected by the XPath expression. It returns a list of strings containing the text content of all selected elements.

### Scrapy Shell

`scrapy shell target_website_url` opens the page interactively on the Scrapy shell using the terminal CLI. This means that you can request and get the response interactively with a live website using the terminal.

## Proxy Server
![image](https://github.com/LemonLim18/Web-Scrapping-Crawling/assets/116692908/cae6292b-3726-4bb2-8230-7d3f6120ee5d)
