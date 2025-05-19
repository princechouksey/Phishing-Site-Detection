import pytesseract
from PIL import Image, UnidentifiedImageError
import os

# Optional: For SVG to PNG conversion
try:
    import cairosvg
    svg_supported = True
except ImportError:
    svg_supported = False
    print("[!] 'cairosvg' not installed, SVG files will be skipped.")

def convert_svg_to_png(svg_path):
    png_path = svg_path.replace('.svg', '.png')
    try:
        cairosvg.svg2png(url=svg_path, write_to=png_path)
        return png_path
    except Exception as e:
        print(f"[!] Failed to convert SVG: {svg_path} — {e}")
        return None

def perform_ocr_on_images(image_paths):
    ocr_text = ""
    supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']

    for image_path in image_paths:
        ext = os.path.splitext(image_path)[-1].lower()

        # Handle SVG separately
        if ext == '.svg':
            if svg_supported:
                print(f"[+] Converting SVG to PNG: {image_path}")
                image_path = convert_svg_to_png(image_path)
                if not image_path:
                    continue
                ext = '.png'
            else:
                print(f"[!] Skipping SVG (not supported): {image_path}")
                continue

        if ext not in supported_extensions:
            print(f"[!] Skipping unsupported file: {image_path}")
            continue

        try:
            img = Image.open(image_path)
            ocr_text += pytesseract.image_to_string(img)
        except UnidentifiedImageError:
            print(f"[!] Unidentified or corrupt image: {image_path}")
        except Exception as e:
            print(f"[!] Error processing {image_path}: {e}")

    return ocr_text
