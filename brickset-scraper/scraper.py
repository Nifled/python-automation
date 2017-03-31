# scraper.py , run using 'scrapy runspider scraper.py'
import scrapy


class BrickSetSpider(scrapy.Spider):
    """
    Created class to scrape different pages off brickset.com (lego website) using scrapy and
    scrapy.spider base class. NEXT_PAGE_SELECTOR implements the next page crawling iterations,
    follows links until there are no more left.
    """
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'

        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 a ::text'  # Using CSS selectors
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'  # Using XPath selectors
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMG_SELECTOR = 'img ::attr(src)'

            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMG_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
