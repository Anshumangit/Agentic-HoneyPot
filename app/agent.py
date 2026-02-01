# app/agent.py

from app.gemini_client import get_model


AGENT_PERSONA = """
You are an Indian bank customer.
You are worried but polite.
You are cooperative and slightly confused.
You never accuse the sender.
You never reveal you are an AI.
You respond like a real human.
Keep responses short.
"""


def generate_agent_reply(history):
    """
    Generate a human-like reply from the agent using Gemini
    """

    model = get_model()

    conversation = ""
    for msg in history:
        conversation += f"{msg['sender']}: {msg['text']}\n"

    prompt = f"""
{AGENT_PERSONA}

Conversation so far:
{conversation}

Reply as the user.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Gemini error:", e)
        return "Please give me a moment, I am checking this."
