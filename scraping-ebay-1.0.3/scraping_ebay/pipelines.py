# -*- coding: utf-8 -*-
import os
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

class EbayImagesPipeline(ImagesPipeline):
    """
    Custom ImagesPipeline to download images and organize them under
    IMAGES_STORE/<sw_code>/<sw_code>_<index>.<ext>
    """

    def get_media_requests(self, item, info):
        """
        For each image URL, send a request carrying sw_code and sequential order.
        """
        sw_code = item.get('sw_code')
        for idx, url in enumerate(item.get('image_urls', []), start=1):
            yield Request(
                url,
                meta={
                    'sw_code': sw_code,
                    'order': idx
                }
            )

    def file_path(self, request, response=None, info=None):
        """
        Compute file path: <sw_code>/<sw_code>_<order>.<extension>
        """
        sw_code = request.meta.get('sw_code')
        order   = request.meta.get('order')
        # Extract extension (without query string)
        ext = os.path.splitext(request.url)[1].split('?')[0] or '.jpg'
        # Build filename and relative path
        filename = f"{sw_code}_{order}{ext}"
        return f"{sw_code}/{filename}"
