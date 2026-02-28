import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "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")

def get_ai_response(user_message):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "Agri Voice Assistant"
    }

    data = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful, friendly agriculture expert assistant designed for farmers. "
                    "Follow these rules strictly:\n"
                    "1. DETECT the language the user is speaking and ALWAYS reply in that EXACT SAME language.\n"
                    "2. You MUST prefix your response with the BCP 47 language code in square brackets. Examples:\n"
                    "   - English: [en-IN] or [en-US]\n"
                    "   - Hindi: [hi-IN]\n"
                    "   - Telugu: [te-IN]\n"
                    "   - Tamil: [ta-IN]\n"
                    "   - Kannada: [kn-IN]\n"
                    "   - Malayalam: [ml-IN]\n"
                    "   - Marathi: [mr-IN]\n"
                    "   - Bengali: [bn-IN]\n"
                    "   - Gujarati: [gu-IN]\n"
                    "   - Punjabi: [pa-IN]\n"
                    "   - Odia: [or-IN]\n"
                    "   - Urdu: [ur-IN]\n"
                    "   - Spanish: [es-ES]\n"
                    "   - French: [fr-FR]\n"
                    "   For any other language, use the correct BCP 47 code.\n"
                    "3. Give SHORT, SIMPLE, and EASY-TO-UNDERSTAND answers suitable for farmers.\n"
                    "4. Use simple vocabulary and short sentences.\n"
                    "5. You can answer ANY question the farmer asks — about agriculture, weather, crops, "
                    "soil, fertilizers, pesticides, animal husbandry, government schemes, market prices, "
                    "health, general knowledge, or anything else.\n"
                    "6. If a farmer asks about something non-agricultural, still help them politely with a brief answer.\n"
                    "7. Be warm, supportive, and encouraging. Address the farmer respectfully.\n"
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)

        result = response.json()

        print("STATUS:", response.status_code)
        print("RESPONSE:", result)

        if response.status_code == 200 and "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            error_msg = result.get("error", {}).get("message", "Unknown error")
            return f"[en-IN] Sorry, I could not process your request. Error: {error_msg}"
    except Exception as e:
        print("ERROR:", str(e))
        return "[en-IN] Sorry, there was a connection error. Please try again."