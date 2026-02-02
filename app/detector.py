# app/detector.py

import json
import re

from app.gemini_client import get_model


def detect_scam(text: str):
    """
    Detect whether a message is a scam using Gemini
    """

    model = get_model()

    prompt = f"""
Analyze the message below and determine if it is a scam.

Message:
{text}

Respond ONLY in JSON:
{{
  "scamDetected": true or false,
  "reason": "short explanation"
}}
"""

    try:
        response = model.generate_content(prompt)
    except Exception:
        return {
            "scamDetected": False,
            "reason": "Model request failed"
        }

    text_resp = getattr(response, "text", "") or ""
    json_match = re.search(r"\{.*\}", text_resp, re.DOTALL)
    if not json_match:
        return {
            "scamDetected": False,
            "reason": "Unable to parse model response"
        }

    try:
        parsed = json.loads(json_match.group(0))
    except json.JSONDecodeError:
        return {
            "scamDetected": False,
            "reason": "Unable to parse model response"
        }

    scam_detected = bool(parsed.get("scamDetected", False))
    reason = parsed.get("reason", "No reason provided")
    return {
        "scamDetected": scam_detected,
        "reason": reason
    }
