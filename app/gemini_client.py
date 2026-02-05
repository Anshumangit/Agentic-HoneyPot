# app/gemini_client.py

import os

import google.generativeai as genai

_MODEL = None
def get_model():
    """
    Returns a configured Gemini GenerativeModel
    """
    global _MODEL
    if _MODEL is None:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        _MODEL = genai.GenerativeModel("gemini-3-flash-preview")
    return _MODEL

def generate_content(prompt: str):
    """
    Generates content using the shared Gemini model.
    """

    model = get_model()
    return model.generate_content(prompt)