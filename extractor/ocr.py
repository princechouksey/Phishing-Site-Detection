import pytesseract
from PIL import Image

def perform_ocr_on_images(image_paths):
    ocr_text = ""
    for image_path in image_paths:
        img = Image.open(image_path)
        ocr_text += pytesseract.image_to_string(img)
    return ocr_text
