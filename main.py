from crawler.static_crawler import crawl_static_html
from crawler.dynamic_crawler import crawl_dynamic_html
from extractor.image_extractor import extract_and_download_images
from extractor.ocr import perform_ocr_on_images
from analyzer.llm_formatter import prepare_llm_input
from analyzer.llm_analyzer import analyze_with_llm
import os
import json

if __name__ == "__main__":
    url = input("Enter URL to scan: ")

    # 1. Static HTML crawl
    static_html = crawl_static_html(url)

    # 2. JS-rendered DOM crawl
    rendered_html = crawl_dynamic_html(url)

    # 3. Image extraction and OCR
    image_paths = extract_and_download_images(rendered_html, url)
    ocr_text = perform_ocr_on_images(image_paths)

    # 4. Prepare input for LLM
    llm_input = prepare_llm_input(rendered_html, ocr_text)

    # 5. Analyze using LLM
    result = analyze_with_llm(llm_input)

    print("\n🔍 Final Phishing Analysis Result:")
    print(result)

    # Optional: save to output
    with open("outputs/results.json", "w") as f:
        json.dump(result, f, indent=2)
