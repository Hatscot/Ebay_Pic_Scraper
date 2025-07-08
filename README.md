# Ebay Pic Scraper

This project contains a small Scrapy setup used to download product images from eBay.

## Configuration

Two environment variables control where the spider reads the product links and where it stores images:

- `CSV_LINKS_PATH` – path to the CSV file with the columns `SW_Code` and `Item_Link`. It defaults to `D:\Ebay_Scraper\EBay_links_output.csv`.
- `IMAGES_STORE` – directory that receives the downloaded images. It defaults to `D:\Ebay_Scraper\Ebay_pics`.

The default paths above are Windows-style and may not exist on your machine. Set `IMAGES_STORE` to a real directory before running the spider.





## Usage

Activate your environment, set the paths and launch ``run_spider.py``:

```bash
export CSV_LINKS_PATH=/path/to/EBay_links_output.csv
export IMAGES_STORE=/path/to/Ebay_pics
python run_spider.py
```



