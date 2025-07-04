import pandas as pd
import scrapy

from .. import settings


class CsvImageSpider(scrapy.Spider):
    name = "csv_image_spider"

    def start_requests(self):
        df = pd.read_csv(settings.CSV_LINKS_PATH)
        for _, row in df.iterrows():
            url = row["Item_Link"]
            sw = row["SW_Code"]
            yield scrapy.Request(url, callback=self.parse, meta={"sw": sw})

    def parse(self, response):
        sw = response.meta.get("sw")
        image_urls = []
        for url in response.css("img::attr(src)").getall():
            if url.lower().endswith(".jpg"):
                if url not in image_urls:
                    image_urls.append(url)
        yield {"prod_id": sw, "images_url": image_urls}
