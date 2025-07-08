import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Allow importing the bundled spider package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scraping-ebay-1.0.3"))
from scraping_ebay.spiders.ebay_v1 import EbayV1Spider

# Example paths - update these to match your local setup
os.environ.setdefault("CSV_LINKS_PATH", "path/to/EBay_links_output.csv")
os.environ.setdefault("IMAGES_STORE", "path/to/Ebay_pics")

def main() -> None:
    process = CrawlerProcess(get_project_settings())
    process.crawl(EbayV1Spider)
    process.start()


if __name__ == "__main__":
    main()
