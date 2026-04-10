import os
from dotenv import load_dotenv

load_dotenv()

def get_env(key: str, default=None, required=False):
    value = os.getenv(key, default)
    if required and not value:
        raise RuntimeError(f"{key} is required")
    return value

GEMINI_API_KEY = get_env("GEMINI_API_KEY", required=True)
GEMINI_MODEL = get_env("GEMINI_MODEL", "models/gemini-flash-latest")

DEBUG = get_env("DEBUG", "False") == "True"