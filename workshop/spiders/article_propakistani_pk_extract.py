from scrapy import Spider


class ProPakistaniExtractSpider(Spider):
    name = "article_propakistani_pk_extract"
    start_urls = [
        "https://propakistani.pk/category/tech-and-telecom/"
    ]

    def parse(self, response):
        property_links = response.css("#main article h2 a")
        for request in response.follow_all(property_links, callback=self.parse_artcile):
            request.meta["zyte_api_automap"] = {"article": True}
            yield request

    def parse_artcile(self, response):
        yield response.raw_api_response["article"]
