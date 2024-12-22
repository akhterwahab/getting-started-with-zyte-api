from scrapy import Spider


class WeWorkRemotelyExtractSpider(Spider):
    name = "jobs_weworkremotely_com_extract"
    start_urls = [
        "https://weworkremotely.com/"
    ]

    def parse(self, response):
        jobs_links = response.css(".jobs li a[href*='/remote-jobs/']")
        for request in response.follow_all(jobs_links, callback=self.parse_job):
            request.meta["zyte_api_automap"] = {"jobPosting": True}
            yield request

    def parse_job(self, response):
        yield response.raw_api_response["jobPosting"]
