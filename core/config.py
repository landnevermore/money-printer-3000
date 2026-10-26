"""Zentrale Konfiguration"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Farben für Digital Products
COLORS = {
    "navy":   (30, 58, 95),
    "teal":   (15, 118, 110),
    "purple": (88, 28, 135),
    "rose":   (159, 18, 57),
    "forest": (20, 83, 45),
    "slate":  (51, 65, 85),
    "coral":  (194, 65, 12),
    "indigo": (67, 56, 202),
    "black":  (15, 15, 15),
    "gold":   (180, 140, 40),
}

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")
