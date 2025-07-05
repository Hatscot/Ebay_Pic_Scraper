# -*- coding: utf-8 -*-
import os

BOT_NAME = 'scraping_ebay'

SPIDER_MODULES = ['scraping_ebay.spiders']
NEWSPIDER_MODULE = 'scraping_ebay.spiders'

# Pfad zur CSV mit SW-Codes und Item-Links
CSV_LINKS_PATH = os.getenv(
    'CSV_LINKS_PATH',
    r'D:\Ebay_Scraper\EBay_links_output.csv'
)

# Basis-Verzeichnis zum Speichern heruntergeladener Bilder
IMAGES_STORE = os.getenv(
    'IMAGES_STORE',
    r'D:\Ebay_Scraper\Ebay_pics'
)

# Aktiviere deine Bilder-Pipeline
ITEM_PIPELINES = {
    'scraping_ebay.pipelines.EbayImagesPipeline': 1,
}

# Identifikation & Cookies
USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59'
)
COOKIES_ENABLED = True

# Robots.txt beachten oder nicht
ROBOTSTXT_OBEY = False

# Concurrency & Delay
CONCURRENT_REQUESTS = 2
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True

# Timeouts & Retries
DOWNLOAD_TIMEOUT = 15
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 522, 524]

# Proxy / IP-Rotation mit scrapy-rotating-proxies
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'scrapy_rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'scrapy_rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}
# Liste deiner Proxy-Server (IP:Port)
ROTATING_PROXY_LIST = [
    'proxy1.example.com:8000',
    'proxy2.example.com:8031',
    # weitere Proxies eintragen
]
ROTATING_PROXY_PAGE_RETRY_TIMES = 2  # Versuche pro Proxy bis zum Wechsel

# Telnet-Konsole abschalten (Optional)
TELNETCONSOLE_ENABLED = False

# AutoThrottle für dynamische Anpassung
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# Feed-Exporter für CSV (falls benötigt)
FEED_EXPORTERS = {
    'csv': 'scraping_ebay.exporters.HeadlessCsvItemExporter',
}
