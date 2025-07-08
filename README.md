# Ebay Pic Scraper

This project contains a small Scrapy setup used to download product images from eBay.

## Configuration

Two environment variables control where the spider reads the product links and where it stores images:

- `CSV_LINKS_PATH` – path to the CSV file with the columns `SW_Code` and `Item_Link`. It defaults to `D:\Ebay_Scraper\EBay_links_output.csv`.
- `IMAGES_STORE` – directory that receives the downloaded images. It defaults to `D:\Ebay_Scraper\Ebay_pics`.

The default paths above are Windows-style and may not exist on your machine. Set `IMAGES_STORE` to a real directory before running the spider.





## Usage

Activate your environment and run the spider:

```Python Shell (Setup Save Path)
os.environ["IMAGES_STORE"] = r"C:\path\to\Ebay_pics"   # Windows-Beispiel
# oder
os.environ["IMAGES_STORE"] = "/path/to/Ebay_pics"      # Linux/macOS

```

To Start the Spider bot run this above, IMPORTANT The first command have to be executed if not it would not work

``` Python Shell
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraping_ebay.spiders.ebay_v1 import EbayV1Spider
import os

os.environ["IMAGES_STORE"] = r"C:\path\to\Ebay_pics"

process = CrawlerProcess(get_project_settings())
process.crawl(EbayV1Spider)
process.start()
```



If something doesn't work as expected, check the debug log for details.


Issue:
Images are  should saved inside `IMAGES_STORE` grouped by their `SW_Code`but it dont happend it just Find Images but dont save it.
