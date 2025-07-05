# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy.utils.project import get_project_settings

class EbayV1Spider(scrapy.Spider):
    name = "ebay_v1"
    custom_settings = {
        # Use the custom ImagesPipeline defined in pipelines.py
        'ITEM_PIPELINES': {
            'scraping_ebay.pipelines.EbayImagesPipeline': 1,
        }
    }

    def start_requests(self):
        # Load CSV path from settings
        settings = get_project_settings()
        csv_path = settings.get('CSV_LINKS_PATH')
        # Read SW codes and item URLs
        df = pd.read_csv(csv_path, dtype=str)
        for _, row in df.iterrows():
            # support different column namings
            sw_code = row.get('SW_Code') or row.get('SW_code') or row.get('sw_code')
            url     = row.get('Item_Link') or row.get('item_link') or row.get('URL')
            if not sw_code or not url:
                continue
            yield scrapy.Request(
                url=url.strip(),
                callback=self.parse,
                meta={'sw_code': sw_code.strip()}
            )

    def parse(self, response):
        sw_code = response.meta['sw_code']
        # Extract thumbnail URLs and convert to high resolution
        thumb_urls = response.xpath("//img[contains(@src,'s-l64')]/@src").getall()
        image_urls = []
        for thumb in thumb_urls:
            full = thumb.replace('s-l64', 's-l1600')
            if full not in image_urls:
                image_urls.append(full)
        # Yield item for ImagesPipeline
        yield {
            'sw_code': sw_code,
            'image_urls': image_urls
        }
