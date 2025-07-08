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
    'file_path',
    r'D:\Ebay_Scraper\Ebay_pics'
)

# Aktiviere deine Bilder-Pipeline
ITEM_PIPELINES = {
    'scraping_ebay.pipelines.EbayImagesPipeline': 1,
}

# Browser-ähnlicher User-Agent und Cookies
USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/84.0.4147.125 Safari/537.36'
)
COOKIES_ENABLED = True

# robots.txt ignorieren (oder True, wenn gewünscht)
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
# Achte darauf, scrapy-rotating-proxies per pip installiert zu haben
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# Liste deiner Proxy-Server (funktionierende IP:Port-Kombinationen!)
ROTATING_PROXY_LIST = [
    '85.215.64.49:80',  #Germany
    '219.65.73.81:80', #Indian
    '57.129.81.201:8080', #Germany
    '23.157.88.25:1080', #Germany
    '193.233.140.109:8085', #Russian
    '85.239.56.88', # Russian
    '193.233.231.63', # Ruassian
    '85.215.64.49:80', # Geramany
    '219.65.73.81:80', # India
    '57.129.81.201:8080', #Germany
    '37.187.74.125:80', #France
    '4.245.123.244:80', #Netherlands
    '92.67.186.210:80', # Netherlands
    '108.141.130.146:80', #Netherlands
    '213.189.137.132:80', #Schweiz
    '213.189.137.134:80', #Schweiz
    '46.47.197.210:3128', #Russian
    '41.191.203.161:80', #Lesotho
    '139.59.1.14:80', #India
    '78.47.127.91:80', #Germany Elite Proxy
    '200.174.198.86:8888', #Brazil
    '176.126.103.194:44214', #Rusiian Elite Proxy
    '138.199.233.152:80', #Germany
    '103.217.219.37:8080', #Indonesia
    '161.35.70.249:8080', #Germany
    '103.65.237.92:5678', #Indonesia
    '81.169.213.169:8888', #Germany
    '200.174.198.86:8888', #Brazil
    '85.215.64.49:80', #Germany
    '219.65.73.81:80', #India
    '57.129.81.201:8080', #Germany
    '37.187.74.125:80', #Frane Elite Proxy
    '81.169.213.169:8888', #Germany
    '23.247.136.254:80', #Netherlands
    '4.245.123.244:80', #Netherlands
    '108.141.130.146:80', #Netherlands
    '213.143.113.82:80', #Austria
    '213.189.137.134:80', #Switzerland
    '46.47.197.210:3128', #Russian Elite Proxy
    '139.59.1.14:80', #India
    '144.22.175.58:1080', #Brazil
    '195.114.209.50:80', #Spain Elite Proxy
    '103.75.119.185:80', #Australia
    '54.194.252.228:3128', #Irland
    '47.91.65.23:3128', #Germany
    '103.160.182.125:8080', #Indonesia
    '4.195.16.140:80', #Australia
    '78.47.127.91:80', #Germany
    '193.151.142.150:8088', #Iran

    # weitere echte Proxies hinzufügen
]
# Anzahl der Versuche pro Proxy bevor gewechselt wird
ROTATING_PROXY_PAGE_RETRY_TIMES = 2
# Optional: wie lange ein toter Proxy pausiert
ROTATING_PROXY_BACKOFF_BASE = 300  # Sekunden

# AutoThrottle für dynamische Anpassung
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# Telnet-Konsole abschalten
TELNETCONSOLE_ENABLED = False

# Feed-Exporter für CSV (falls benötigt)
FEED_EXPORTERS = {
    'csv': 'scraping_ebay.exporters.HeadlessCsvItemExporter',
}
