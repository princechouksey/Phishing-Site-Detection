# ChatPhishDetector 🕵️‍♂️🔍

**ChatPhishDetector** is a multi-modal, AI-powered phishing detection system. It simulates real-world browsing by fetching static HTML, rendering JavaScript-driven content, extracting images for OCR, and leveraging Google’s Gemini LLM to identify deceptive techniques and phishing indicators.

---

## 🚀 Features

- **Static Crawler**: Fetch and prettify raw HTML using `requests` + `BeautifulSoup`.  
- **Dynamic Crawler**: Load and render JS content via headless Chrome & `selenium`.  
- **Image Extraction & OCR**: Download all `<img>` assets and extract embedded text with `pytesseract`.  
- **DOM Parsing**: Pull out forms, scripts, inputs and other structural features.  
- **LLM Analysis**: Format multi-modal content into a single prompt and call Gemini to classify phishing vs. legitimate.  
- **Configurable**: Easy to drop in your Gemini API key.  
- **Extensible**: Modular architecture for adding screenshots, feature-engines, UI front-ends, etc.

---

## 🗂️ Folder Structure

chatphishdetector/
├── main.py # Orchestrates the full pipeline
├── requirements.txt # All Python dependencies
├── config/
│ └── settings_example.py # Rename to settings.py and insert your API key
├── crawler/
│ ├── static_crawler.py # requests + BeautifulSoup
│ └── dynamic_crawler.py # selenium headless browser
├── extractor/
│ ├── image_extractor.py # download <img> resources
│ ├── ocr.py # run pytesseract on images
│ └── dom_parser.py # extract forms, links, scripts
├── analyzer/
│ ├── llm_formatter.py # prepare combined prompt
│ └── llm_analyzer.py # call Gemini model
├── utils/
│ ├── logger.py # optional logging helpers
│ └── helpers.py # URL normalization, file helpers
├── data/
│ ├── screenshots/ # (optional) full-page screenshots
│ ├── html_pages/ # raw HTML dumps for audit
│ └── extracted_images/ # downloaded images for OCR
└── outputs/
└── results.json # final phishing verdict + metadata


---

## 🛠️ Prerequisites

- **Python** 3.8+  
- **Google Chrome** & matching **ChromeDriver** (for Selenium)  
- **Tesseract OCR** engine installed & in your PATH  

---

## 📦 Installation

1. **Clone or create** the repo:

   ```bash
   git clone https://github.com/yourusername/chatphishdetector.git
   cd chatphishdetector



<!-- uvicorn main:app --reload -->