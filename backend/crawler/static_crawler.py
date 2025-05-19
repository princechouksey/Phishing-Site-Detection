import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
from utils.helpers import get_safe_filename, ensure_directory_exists, generate_timestamped_filename

def crawl_static_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        html_content = response.text

        # Prepare directory and file path
        domain = urlparse(url).netloc
        safe_domain = get_safe_filename(domain)
        ensure_directory_exists("data/html_pages")
        filename = generate_timestamped_filename(safe_domain)
        output_path = os.path.join("data/html_pages", filename)

        # Save HTML content
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        return html_content
    except requests.RequestException as e:
        print(f"[Static Crawler] Error: {e}")
        return ""
