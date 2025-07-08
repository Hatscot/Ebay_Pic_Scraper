# Ebay Pic Scraper

This project contains a small Scrapy setup used to download product images from eBay.

## Configuration

Two environment variables control where the spider reads the product links and where it stores images:

- `CSV_LINKS_PATH` – path to the CSV file with the columns `SW_Code` and `Item_Link`. It defaults to `D:\Ebay_Scraper\EBay_links_output.csv`.
- `IMAGES_STORE` – directory that receives the downloaded images. It defaults to `D:\Ebay_Scraper\Ebay_pics`.

The default paths above are Windows-style and may not exist on your machine. Set `IMAGES_STORE` to a real directory before running the spider.

### Setting `IMAGES_STORE`

- **Windows** (Command Prompt)

  ```cmd
  set IMAGES_STORE=C:\path\to\Ebay_pics
  ```

- **Linux/macOS**

  ```bash
  export IMAGES_STORE=/path/to/Ebay_pics
  ```

## Usage

Activate your environment and run the spider:

```bash
scrapy crawl ebay_v1
```


Issue:
Images are  should saved inside `IMAGES_STORE` grouped by their `SW_Code`but it dont happend it just Find Images but dont save it.
