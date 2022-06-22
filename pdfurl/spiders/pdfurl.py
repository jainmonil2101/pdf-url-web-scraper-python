import scrapy
from ..items import PdfurlItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ExampleSpider(CrawlSpider):
    name = 'pdfurl'
    # allowed_domains = ['adobe.com']
    start_urls = ['https://kimberleygrande.com.au/']

    rules = [Rule(LinkExtractor(allow=""), callback='parse', follow=True)]

    def parse(self, response):

        item = PdfurlItem()
        
        

        # CHECK IF THE LINK GOES TO A PDF
        if b'Content-Type' in response.headers.keys():
            links_to_pdf = 'application/pdf' in str(response.headers['Content-Type'])

        else:
            return None

        # IF IT DOES, SCRAPE IT
        if links_to_pdf:
            # SCRAPE THE SPECIFIED DATA
            print(response.url)
            print()
            item['filename'] = response.url.split('/')[-1]
            item['url'] = response.url

        # IF NOT, IGNORE IT AND MOVE ON TO THE NEXT LINK
        else:
            return None

        # WRITE THAT DATA TO THE CSV
        return item
        
