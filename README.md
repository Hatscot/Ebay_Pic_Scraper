# Ebay Pic Scraper

This project contains a small Scrapy setup used to download product images from eBay.

## Configuration

Two environment variables control where the spider reads the product links and where it stores images:

- `CSV_LINKS_PATH` – path to the CSV file with the columns `SW_Code` and `Item_Link`. It defaults to `D:\Ebay_Scraper\EBay_links_output.csv`.
- `IMAGES_STORE` – directory that receives the downloaded images. It defaults to `D:\Ebay_Scraper\Ebay_pics`.

The default paths above are Windows-style and may not exist on your machine. Set `IMAGES_STORE` to a real directory before running the spider.





## Usage

Activate your environment and run the spider:


Python Shell
``` 
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraping_ebay.spiders.ebay_v1 import EbayV1Spider

# Setze das Verzeichnis für die Bilder
os.environ["IMAGES_STORE"] = r"C:\Users\Fabian\PycharmProjects\Ebay_Pic_Scraper\Ebay_pics"

# Optional: aktuelles Verzeichnis explizit setzen, falls du das Script außerhalb startest
#os.chdir(r"C:\Users\Fabian\PycharmProjects\Ebay_Pic_Scraper\scraping-ebay-1.0.3\scraping_ebay\spiders")

# Projekt-Settings laden
settings = get_project_settings()
process = CrawlerProcess(settings)

# Spider über die Klasse starten
process.crawl(EbayV1Spider)
process.start()
```


Issues / should be fix:
- There is somthing wrong with the Start Skript for the spider under ##Usage

Note 
Ignore the Project.zip thats just a old version and has nothing to do with all of the rest files in this repos


