"""Hilfsfunktionen"""
import re
from pathlib import Path
from core.config import OUTPUT_DIR

def safe_filename(text: str) -> str:
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[\s]+', '_', text).strip('_')[:80]

def make_output_folder(name: str) -> Path:
    folder = OUTPUT_DIR / safe_filename(name)
    folder.mkdir(parents=True, exist_ok=True)
    return folder

def write_text(path: Path, content: str):
    path.write_text(content, encoding="utf-8")
