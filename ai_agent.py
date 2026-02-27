import requests

# ⚠️ PASTE YOUR REAL KEY HERE
OPENROUTER_API_KEY = "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"

def get_ai_response(user_message):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "Agri Voice Assistant"
    }

    data = {
        "model": "google/gemini-2.0-flash-001",   # free model, no credits needed
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an agriculture expert assistant. "
                    "1. Give VERY SHORT, simple, and easy-to-understand answers suitable for farmers. "
                    "2. Always reply in the EXACT SAME LANGUAGE that the user speaks. "
                    "3. You MUST prefix your response with the appropriate BCP 47 language code in brackets, e.g., [en-US], [hi-IN], [te-IN], [ta-IN], [mr-IN], etc. "
                    "Example: [hi-IN] आपकी फसल के लिए यूरिया का इस्तेमाल करें।"
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    print("STATUS:", response.status_code)
    print("RESPONSE:", result)

    if response.status_code == 200 and "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return "AI not working. Check API key or credits."