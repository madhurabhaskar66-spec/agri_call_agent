import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_ai_response(user_query: str) -> str:
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "AI Voice Agent"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful agriculture assistant."},
                    {"role": "user", "content": user_query}
                ]
            }
        )

        data = response.json()

        # DEBUG: If error returned
        if "error" in data:
            return f"OpenRouter Error: {data['error']}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"AI Exception: {str(e)}"