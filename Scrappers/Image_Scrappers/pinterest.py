from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class PinterestScraper:
    def __init__(self, pinterest_links, max_images=20, scroll_pause_time=10):
        self.pinterest_links = pinterest_links
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
            image_list = []
            for link in self.pinterest_links:
                self.driver.get(link)
                self.driver.maximize_window()
                self.scroll_to_bottom()

                elements = self.get_image_elements()

                for element in elements:
                    href = element.get_attribute("src")
                    self.images.append(href)  

                image_list.extend(self.images[:self.max_images])
            return image_list
            
        finally:
            self.driver.quit()

    def scroll_to_bottom(self):
        while True:
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(self.scroll_pause_time)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break

    def get_image_elements(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//img[@class='hCL kVc L4E MIw']")))
        return self.driver.find_elements(By.XPATH, "//img[@class='hCL kVc L4E MIw']")