import os
import sys
import pytest
from scrapy.http import Request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scraping-ebay-1.0.3'))
from scraping_ebay.pipelines import EbayImagesPipeline


def test_file_path_uses_correct_extension():
    pipeline = EbayImagesPipeline(store_uri="/tmp")
    req = Request('http://example.com/img1.png?size=large', meta={'sw_code': 'abc', 'order': 1})
    assert pipeline.file_path(req) == 'abc/abc_1.png'


def test_file_path_defaults_to_jpg_when_no_extension():
    pipeline = EbayImagesPipeline(store_uri="/tmp")
    req = Request('http://example.com/img', meta={'sw_code': 'xyz', 'order': 2})
    assert pipeline.file_path(req) == 'xyz/xyz_2.jpg'
