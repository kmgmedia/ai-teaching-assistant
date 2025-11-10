"""
Environment configuration and API client setup.
Centralizes all environment variables and credentials.
Supports both local development and Streamlit Cloud deployment.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file (local development)
load_dotenv()

# Check if running on Streamlit Cloud
def get_config_value(key, default=None):
    """Get configuration from Streamlit secrets or environment variables."""
    try:
        import streamlit as st
        if hasattr(st, 'secrets') and key in st.secrets:
            return st.secrets[key]
    except (ImportError, AttributeError, FileNotFoundError):
        pass
    return os.getenv(key, default)

# OpenAI Configuration
OPENAI_API_KEY = get_config_value("OPENAI_API_KEY")
OPENAI_MODEL = get_config_value("OPENAI_MODEL", "gpt-3.5-turbo")
OPENAI_TEMPERATURE = float(get_config_value("OPENAI_TEMPERATURE", "0.7"))
OPENAI_MAX_TOKENS = int(get_config_value("OPENAI_MAX_TOKENS", "1000"))

# Google Sheets Configuration
GOOGLE_SHEETS_CREDENTIALS = get_config_value("GOOGLE_SHEETS_CREDENTIALS")
GOOGLE_SHEET_ID = get_config_value("GOOGLE_SHEET_ID")

# Flask Configuration
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

# Output Configuration
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "data/output")

# Validate critical settings
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in .env file.")
