import pytesseract
from PIL import Image, UnidentifiedImageError
import os
import base64  # Added for base64 decoding

# Optional: For SVG to PNG conversion
try:
    import cairosvg
    svg_supported = True
except ImportError:
    svg_supported = False
    print("[!] 'cairosvg' not installed, SVG files will be skipped.")

def save_base64_svg(base64_data, output_path="image.svg"):
    """Decode base64 string and save as an SVG file."""
    try:
        svg_bytes = base64.b64decode(base64_data)
        with open(output_path, "wb") as f:
            f.write(svg_bytes)
        print(f"[+] SVG saved to {output_path}")
        return output_path
    except Exception as e:
        print(f"[!] Failed to save base64 SVG: {e}")
        return None

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

        # Handle SVG separately by converting to PNG first
        if ext == '.svg':
            if svg_supported:
                print(f"[+] Converting SVG to PNG: {image_path}")
                png_path = convert_svg_to_png(image_path)
                if not png_path:
                    continue

                try:
                    img = Image.open(png_path)
                    ocr_text += pytesseract.image_to_string(img)
                except UnidentifiedImageError:
                    print(f"[!] Unidentified or corrupt image: {png_path}")
                except Exception as e:
                    print(f"[!] Error processing {png_path}: {e}")

                # Optionally remove the PNG after OCR to keep directory clean
                try:
                    os.remove(png_path)
                except Exception as e:
                    print(f"[!] Could not remove temporary PNG file: {png_path} — {e}")
                continue
            else:
                print(f"[!] Skipping SVG (not supported): {image_path}")
                continue

        # For normal raster image formats
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
