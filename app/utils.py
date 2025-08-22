# app/utils.py
import logging
import re

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def clean_text(text: str) -> str:
    """Remove unwanted characters from text."""
    return re.sub(r"[^a-zA-Z0-9\s]", "", text).strip()

def load_config() -> dict:
    """Dummy config loader (can extend later)."""
    return {
        "model": "gpt-neo",
        "temperature": 0.7,
        "max_tokens": 200
    }
