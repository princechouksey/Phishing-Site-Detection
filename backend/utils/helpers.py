# utils/helpers.py
import re
import os
from datetime import datetime

def get_safe_filename(name):
    """
    Sanitize a string to be used as a safe filename.
    """
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)

def ensure_directory_exists(directory_path):
    """
    Ensure that the given directory exists; if not, create it.
    """
    os.makedirs(directory_path, exist_ok=True)

def generate_timestamped_filename(base_name: str, ext: str = ".html") -> str:
    """
    Generate a timestamped filename for unique saving.
    """
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}{ext}"