# run using 'scrapy crawl <name of spider>' from root of project
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    # V1 --- Gets every page and saves it as local file in html format.
    # def parse(self, response):
    #     page = response.url.split('/')[-2]  # gets page number
    #     filename = 'quotes-{}.html'.format(page)

    #     with open(filename, 'wb') as f:
    #         f.write(response.body)  # saves file as .html to local file in folder
