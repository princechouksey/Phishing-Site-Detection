from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def crawl_dynamic_html(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Wait for JS to load content
    rendered_html = driver.page_source
    driver.quit()
    return rendered_html
