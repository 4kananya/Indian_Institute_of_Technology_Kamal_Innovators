from vogue import VogueFashionScraper
from itscasualblog import ItsCasualBlogScraper
from blog_scraper_constants import CASUAL_BLOG_URL, VLOGUE_URL

class BlogScraper:
    def __init__(self):
        self.casual_url = CASUAL_BLOG_URL
        self.vlogue_url = VLOGUE_URL
        self.blogs = []
 
    def scrape_blogs(self):
        self.blogs.extend(self._scrape_casual_blogs())
        self.blogs.extend(self._scrape_vlogue_blogs())
        return self.blogs

    def _scrape_casual_blogs(self):
        casual_scraper = ItsCasualBlogScraper()
        return casual_scraper.scrape_blog_entries(self.casual_url)

    def _scrape_vlogue_blogs(self):
        vlogue_scraper = VogueFashionScraper()
        vlogue_scraper.scrape_main_page(self.vlogue_url)
        return vlogue_scraper.scrape_blog_content()
        