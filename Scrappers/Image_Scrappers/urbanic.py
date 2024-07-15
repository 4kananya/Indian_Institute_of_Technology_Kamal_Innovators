from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class UrbanicScraper:
    def __init__(self, url, max_images=10, scroll_pause_time=2):
        self.url = url
        self.max_images = max_images
        self.scroll_pause_time = scroll_pause_time
        self.images = []
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=self.options)

    def scrape_images(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()

            while len(self.images) < self.max_images:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(self.scroll_pause_time)

                WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//img[@class='ub-image-img']")))
                elements = self.driver.find_elements(By.XPATH, "//img[@class='ub-image-img']")

                initial_count = len(self.images)

                for element in elements:
                    href = element.get_attribute("src")
                    self.images.append(href)

                if len(self.images) == initial_count:
                    break

            image_list = self.images[:self.max_images]
            return image_list

        finally:
            self.driver.quit()

