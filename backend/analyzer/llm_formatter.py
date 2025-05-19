def prepare_llm_input(html_content, ocr_text, dom_info):
    prompt = (
        "You are a cybersecurity analyst. "
        "Analyze the following web content and determine if it's potentially a phishing site.\n"
        "---\n"
        f"HTML Content:\n{html_content}\n"
        f"OCR Text:\n{ocr_text}\n"
        f"DOM Elements:\n{dom_info}\n"
        "---\n"
        "Respond with a clear phishing verdict and reasoning."
    )
    return prompt
         