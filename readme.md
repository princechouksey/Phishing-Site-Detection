# 🛡️ AI-Powered Phishing Website Detection System

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green?logo=fastapi)
![React](https://img.shields.io/badge/React-18+-61DAFB?logo=react)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

An intelligent multi-modal phishing detection platform that uses:

- 🌐 Web Crawling
- 🧠 OCR (Optical Character Recognition)
- 🧩 DOM Parsing
- 🤖 Google Gemini (Large Language Model)
- ⚡ FastAPI for backend
- 🎯 React + TailwindCSS for frontend

---

## 📌 Features

- 🔍 Crawls static and dynamic HTML content from any given URL.
- 🖼️ Downloads and scans images on the page using OCR.
- 🧾 Extracts DOM data: forms, scripts, links.
- 📊 Combines all content and prompts Gemini to analyze phishing likelihood.
- ✅ Verdicts returned via a clean and responsive frontend.
- 📬 API tested with Postman and integrated smoothly with React.js.

---

## 🗂️ Folder Structure

```
chatphishdetector/
├── main.py                     # FastAPI backend entry point
├── requirements.txt            # Backend dependencies
├── config/
│   └── settings.py             # API keys and config
├── crawler/
│   ├── static_crawler.py       # Static HTML crawling using requests + BeautifulSoup
│   └── dynamic_crawler.py      # Dynamic crawling using Selenium
├── extractor/
│   ├── image_extractor.py      # Extract and download <img> tags
│   ├── ocr.py                  # OCR using pytesseract
│   └── dom_parser.py           # Extract form/scripts/links
├── analyzer/
│   ├── llm_formatter.py        # Prepares prompt for Gemini
│   └── llm_analyzer.py         # Calls Gemini API
├── utils/
│   ├── logger.py               # Logging utility (optional)
│   └── helpers.py              # URL/file/path utils
├── data/
│   ├── screenshots/            # (Optional) Page screenshots
│   ├── html_pages/             # Raw HTML dumps
│   └── extracted_images/       # Downloaded images
├── outputs/
│   └── results.json            # Final output from Gemini
└── frontend/
    └── [React App]             # React + Tailwind frontend
```

---

## 🚀 Getting Started

### 🔧 Backend Setup (Python + FastAPI)

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/chatphishdetector.git
   cd chatphishdetector
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. Add your Gemini API Key:
   - Rename `config/settings_example.py` to `settings.py`
   - Add your Google Gemini API key:
     ```python
     GEMINI_API_KEY = "your_api_key_here"
     ```

4. Run FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. Visit:
   - Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### 🌐 Frontend Setup (React + TailwindCSS)

1. Navigate to frontend folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm start
   ```

4. Visit the app in your browser:
   ```
   http://localhost:3000
   ```

---

## 📬 API Usage

### POST `/detect_phishing`

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "phishing_verdict": {
    "phishing_score": 0,
    "verdict": "Safe",
    "explanation": "The HTML content appears to be a legitimate render of the page."
  },
  "metadata": {
    "url": "https://example.com"
  }
}
```

You can test this API using Postman or via the React frontend form.

---

## 🧠 Gemini Prompting Logic

The app prepares a structured prompt including:
- Cleaned HTML content
- Extracted links, forms, scripts
- OCR-extracted text from images

This data is formatted and sent to Google Gemini, which returns a phishing assessment.

---

## 🖼️ Frontend Screenshots

| 🌐 Home Page | ✅ Results Page |
|-------------|----------------|
| ![Home](https://via.placeholder.com/400x250?text=Home+Page) | ![Results](https://via.placeholder.com/400x250?text=Results+Page) |

---

## 🧪 Tech Stack

- **Frontend:** React.js, TailwindCSS, React Router
- **Backend:** Python, FastAPI, Uvicorn
- **AI Model:** Google Gemini
- **Tools:** Selenium, BeautifulSoup, Tesseract OCR, Postman

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🔗 Useful Links

- [Google Gemini API Docs](https://ai.google.dev/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [ReactJS Docs](https://reactjs.org/)
- [TailwindCSS Docs](https://tailwindcss.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

---

> Made with ❤️ using Python, React & AI by ❤️ 
