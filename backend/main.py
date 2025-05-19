from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
import datetime

from crawler.static_crawler import crawl_static_html
from crawler.dynamic_crawler import crawl_dynamic_html
from extractor.image_extractor import extract_and_download_images
from extractor.ocr import perform_ocr_on_images
from analyzer.llm_formatter import prepare_llm_input
from analyzer.llm_analyzer import analyze_with_llm

# DB Imports
from db.db import collection
from db.models import URLRequest, ResultModel

# Initialize FastAPI app
app = FastAPI()

# Add CORS (important for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Core logic for phishing detection
def detect_phishing_logic(url: str):
    static_html = crawl_static_html(url)
    rendered_html = crawl_dynamic_html(url)
    image_paths = extract_and_download_images(rendered_html, url)
    ocr_text = perform_ocr_on_images(image_paths)
    # print("OCR text", ocr_text)
    llm_input = prepare_llm_input(rendered_html, ocr_text)
    # print("LLM INPUT", llm_input)
    result = analyze_with_llm(llm_input)

    # Save result locally (optional)
    with open("outputs/results.json", "w") as f:
        json.dump(result, f, indent=2)

    return result

# ✅ Endpoint: Run phishing detection (with DB caching)
@app.post("/detect_phishing/")
async def detect_phishing(request: URLRequest):
    url = request.url

    # Check if URL already exists
    existing = await collection.find_one({"url": url})
    if existing:
        return {
            "phishing_verdict": existing.get("phishing_verdict"),
            "metadata": {"url": url, "source": "cached"}
        }

    # If not found, process it
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

# Optional: Save a given result manually
@app.post("/save/")
async def save_result(result: ResultModel):
    try:
        result_dict = result.dict()
        result_dict["timestamp"] = datetime.datetime.utcnow()
        inserted = await collection.insert_one(result_dict)
        return {"inserted_id": str(inserted.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DB Save Error: {str(e)}")
