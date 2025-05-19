import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import mimetypes

def extract_and_download_images(html_content, base_url):
    soup = BeautifulSoup(html_content, "html.parser")
    img_tags = soup.find_all("img")
    image_paths = []

    os.makedirs("data/extracted_images", exist_ok=True)

    for i, img in enumerate(img_tags):
        src = img.get("src")
        if not src:
            continue

        img_url = urljoin(base_url, src)
        try:
            response = requests.get(img_url, stream=True, timeout=5)
            content_type = response.headers.get("Content-Type", "")
            extension = mimetypes.guess_extension(content_type.split(";")[0]) or ".jpg"

            parsed = urlparse(img_url)
            filename = f"img_{i}{extension}"
            filepath = os.path.join("data/extracted_images", filename)

            with open(filepath, "wb") as f:
                f.write(response.content)
            image_paths.append(filepath)

        except Exception as e:
            print(f"[Image Extractor] Failed to download {img_url}: {e}")

    return image_paths