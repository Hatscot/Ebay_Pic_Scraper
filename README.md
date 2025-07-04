# Ebay Pic Scraper

This project contains a small Scrapy setup used to download product images from eBay.

## Configuration

Two environment variables control where the spider reads the product links and where it stores images:

- `CSV_LINKS_PATH` – path to the CSV file with the columns `SW_Code` and `Item_Link`. It defaults to `../EBay_links_output.csv`.
- `IMAGES_STORE` – directory that receives the downloaded images. It defaults to `./downloaded_images`.

## Usage

Activate your environment and run the spider:

```bash
scrapy crawl csv_image_spider
```

Images are saved inside `IMAGES_STORE` grouped by their `SW_Code`.
