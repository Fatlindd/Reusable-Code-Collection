import scrapy

from chocolatescraper.itemsLoaders import ChocolateProductLoader
from chocolatescraper.items import ChocolatescraperItem


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        
        # here we are looping through all the products on the page, to extract the name, price & url
        products = response.css('product-item')

        # product_item = ChocolatescraperItem()
        for product in products:
            # product_item['name'] = product.css('a.product-item-meta__title::text').get()
            # product_item['price'] = product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>','').replace('</span>','')
            # product_item['url'] = product.css('div.product-item-meta a').attrib['href']

            # yield product_item
            
            # Item Loader
            chocolate = ChocolateProductLoader(item=ChocolatescraperItem(), selector=product)
            chocolate.add_css('name', "a.product-item-meta__title::text")
            chocolate.add_css('price', 'span.price', re='<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>')
            chocolate.add_css('url', 'div.product-item-meta a::attr(href)')
            yield chocolate.load_item()

        next_page = response.css('[rel="next"]::attr(href)').get()

        if next_page is not None:
            # /collections/all?page=2
            next_page_url = "https://www.chocolate.co.uk" + next_page
            yield response.follow(next_page_url, callback=self.parse)
