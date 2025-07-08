# -*- coding: utf-8 -*-
import os
import csv
import pandas as pd
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

class EbayImagesPipeline(ImagesPipeline):
    """
    Custom ImagesPipeline to download images, organize them under
    IMAGES_STORE/<sw_code>/<sw_code>_<index>.<ext>,
    and update the CSV Downloaded-Flag.
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
        ext = os.path.splitext(request.url)[1].split('?')[0]
        if not ext:
            ext = '.jpg'
        filename = f"{sw_code}_{order}{ext}"
        return f"{sw_code}/{filename}"

    def item_completed(self, results, item, info):
        """
        Called when all image downloads finish. Update CSV 'Downloaded' flag.
        """
        # Determine if at least one image was downloaded successfully
        success = any(x[0] for x in results)
        if success:
            settings = get_project_settings()
            csv_path = settings.get('CSV_LINKS_PATH')
            # Read CSV, update Downloaded field for this sw_code
            try:
                df = pd.read_csv(csv_path, dtype=str)
                col = None
                # find Downloaded column name
                for c in ['Downloaded', 'downloaded']:
                    if c in df.columns:
                        col = c
                        break
                if col is None:
                    # add new column
                    df['Downloaded'] = ''
                    col = 'Downloaded'
                # set flag
                mask = df.get('SW_Code', df.get('SW_code', df.get('sw_code')))==item['sw_code']
                df.loc[mask, col] = '1'
                # write back without index
                df.to_csv(csv_path, index=False)
            except Exception as e:
                info.spider.logger.error(f"Failed to update CSV for {item['sw_code']}: {e}")
        return item
