from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class VogueFashionScraper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=self.options)
        self.subsites = []

    def scrape_main_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        
        blog_link_xpath = "//a[@class='SummaryItemHedLink-civMjp jRfyII summary-item-tracking__hed-link summary-item__hed-link']"
        
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, blog_link_xpath)))
            elements = self.driver.find_elements(By.XPATH, blog_link_xpath)
            for item in elements:
                href = item.get_attribute("href")
                self.subsites.append(href)
        except TimeoutException as e:
            print(f"Timeout waiting for element: {str(e)}")

    def scrape_blog_content(self):
        subsites_wise_content = []
        for item in self.subsites:
            self.driver.get(item)
            self.driver.maximize_window()
            content = []
            blog_content_xpath = "//article[@class='article main-content']"
            
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
            
            content_string = "\n".join(content)
            subsites_wise_content.append(content_string)
        
        self.driver.quit()
        return subsites_wise_content