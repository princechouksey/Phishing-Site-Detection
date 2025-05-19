# crawler/dynamic_crawler.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import os
import time
from utils.helpers import get_safe_filename, ensure_directory_exists, generate_timestamped_filename

def crawl_dynamic_html(url):
    options = Options()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(5)  # Let dynamic content load
        rendered_html = driver.page_source
        driver.quit()

        # Prepare directory and file path
        domain = urlparse(url).netloc
        safe_domain = get_safe_filename(domain)
        ensure_directory_exists("data/html_pages")
        filename = generate_timestamped_filename(safe_domain, ".rendered.html")
        output_path = os.path.join("data/html_pages", filename)

        # Save rendered HTML content
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)

        return rendered_html
    except Exception as e:
        print(f"[Dynamic Crawler] Error: {e}")
        return ""
