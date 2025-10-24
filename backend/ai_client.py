import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ Missing GEMINI_API_KEY in your .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Use the latest working model from your list
MODEL_NAME = "gemini-2.5-flash"   # ✅ Fast and free tier supported model
model = genai.GenerativeModel(MODEL_NAME)

# --- Functions ---

def summarize_text(text: str) -> str:
    """Summarize text using Gemini"""
    if not text.strip():
        return "⚠️ No text provided."

    prompt = f"Summarize the following text clearly and concisely:\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") else "⚠️ No summary generated."
    except Exception as e:
        return f"⚠️ Error generating summary: {e}"


def generate_quiz(text: str, qcount: int = 5) -> str:
    """Generate quiz questions from text"""
    if not text.strip():
        return "⚠️ No text provided."

    prompt = f"Create {qcount} short quiz questions (with answers) based on the following text:\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") else "⚠️ No quiz generated."
    except Exception as e:
        return f"⚠️ Error generating quiz: {e}"
