from dotenv import load_dotenv
import os

load_dotenv()
print("Key read from .env:", os.getenv("GEMINI_API_KEY"))