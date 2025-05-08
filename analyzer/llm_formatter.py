def prepare_llm_input(html_content, ocr_text):
    # Combine HTML content and OCR text for LLM analysis
    return f"HTML Content: {html_content}\nOCR Text: {ocr_text}"
