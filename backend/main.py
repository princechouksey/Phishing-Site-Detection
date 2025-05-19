from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import datetime

from crawler.static_crawler import crawl_static_html
from crawler.dynamic_crawler import crawl_dynamic_html
from extractor.image_extractor import extract_and_download_images
from extractor.ocr import perform_ocr_on_images
from extractor.dom_parser import parse_html_for_dom_elements
from analyzer.llm_formatter import prepare_llm_input
from analyzer.llm_analyzer import analyze_with_llm

# DB Imports
from db.db import collection
from db.models import URLRequest, ResultModel

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Core logic for phishing detection
def detect_phishing_logic(url: str):
    static_html = crawl_static_html(url)
    rendered_html = crawl_dynamic_html(url)
    
    # Extract DOM elements
    dom_info = parse_html_for_dom_elements(rendered_html)

    # Image extraction and OCR
    image_paths = extract_and_download_images(rendered_html, url)
    ocr_text = perform_ocr_on_images(image_paths)

    # Prepare input for LLM
    llm_input = prepare_llm_input(rendered_html, ocr_text, dom_info)

    # Run LLM analysis
    result = analyze_with_llm(llm_input)

    # Optionally save locally
    with open("outputs/results.json", "w") as f:
        json.dump(result, f, indent=2)

    return result

# ✅ Endpoint: Run phishing detection
@app.post("/detect_phishing/")
async def detect_phishing(request: URLRequest):
    url = request.url

    # Check if result exists in DB
    existing = await collection.find_one({"url": url})
    if existing:
        return {
            "phishing_verdict": existing.get("phishing_verdict"),
            "metadata": {"url": url, "source": "cached"}
        }

    # Run detection pipeline
    result = detect_phishing_logic(url)

    # Save to MongoDB
    try:
        result_entry = {
            "url": url,
            "phishing_verdict": result,
            "timestamp": datetime.datetime.utcnow()
        }
        await collection.insert_one(result_entry)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB Save Error: {str(e)}")

    return {
        "phishing_verdict": result,
        "metadata": {"url": url, "source": "fresh"}
    }

# Optional: Manually save a result
@app.post("/save/")
async def save_result(result: ResultModel):
    try:
        result_dict = result.dict()
        result_dict["timestamp"] = datetime.datetime.utcnow()
        inserted = await collection.insert_one(result_dict)
        return {"inserted_id": str(inserted.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB Save Error: {str(e)}")
