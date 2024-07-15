from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

class ItsCasualBlogScraper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=self.options)
    
    def scrape_blog_entries(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        subsites = self.extract_subsites()
        chapter_wise_content = []

        for item in subsites:
            self.driver.get(item)
            self.driver.maximize_window()
            content = self.extract_content()
            content_string = "\n".join(content)
            chapter_wise_content.append(content_string)
            
        self.driver.quit()
        return chapter_wise_content
    
    def extract_subsites(self):
        subsites = []
        blog_link_xpath = "//a[@class='button']"
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, blog_link_xpath)))
            elements = self.driver.find_elements(By.XPATH, blog_link_xpath)
            for item in elements:
                href = item.get_attribute("href")
                subsites.append(href)
        except TimeoutException as e:
            print(f"Timeout waiting for element: {str(e)}")
        return subsites
    
    def extract_content(self):
        content = []
        blog_content_xpath = "//div[@class='entry-content jpibfi_container']"
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, blog_content_xpath)))
            elements = self.driver.find_elements(By.XPATH, f"{blog_content_xpath}//*")
            for item in elements:
                try:
                    if item.tag_name in ['p', 'h2', 'h3', 'h4', 'ul', 'ol', 'li']:
                        content.append(item.text)
                except StaleElementReferenceException:
                    elements = self.driver.find_elements(By.XPATH, f"{blog_content_xpath}//*")
        except TimeoutException as e:
            print(f"Timeout waiting for element: {str(e)}")
        return content