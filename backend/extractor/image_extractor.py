import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_and_download_images(html_content, base_url):
    soup = BeautifulSoup(html_content, "html.parser")
    images = soup.find_all("img")
    image_paths = []

    save_dir = "data/extracted_images"
    os.makedirs(save_dir, exist_ok=True)

    for img in images:
        img_url = img.get("src")
        if not img_url:
            continue

        # Convert relative URLs to absolute using urljoin
        full_img_url = urljoin(base_url, img_url)

        try:
            img_data = requests.get(full_img_url).content
            filename = os.path.join(save_dir, full_img_url.split("/")[-1])
            with open(filename, "wb") as f:
                f.write(img_data)
            image_paths.append(filename)
        except Exception as e:
            print(f"[!] Failed to download image from {full_img_url}: {e}")

    return image_paths
