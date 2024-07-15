from pinterest import PinterestScraper
from urbanic import UrbanicScraper
from image_scraper_constants import URBANIC_URL, PINTEREST_LINKS

class ImageScraper:
    def __init__(self):
        self.urbanic_url = URBANIC_URL
        self.pinterest_urls = PINTEREST_LINKS
        self.images = [] 

    def scrape_images(self):
        self.images.extend(self._scrape_urbanic_images())
        self.images.extend(self._scrape_pinterest_images())
        return self.images

    def _scrape_urbanic_images(self):
        urbanic_scraper = UrbanicScraper(self.urbanic_url)
        return urbanic_scraper.scrape_images()

    def _scrape_pinterest_images(self):
        pinterest_scraper = PinterestScraper(self.pinterest_urls)
        return pinterest_scraper.scrape_images()