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
        "model": "openai/gpt-4o-mini",   # reliable model
        "messages": [
            {
                "role": "system",
                "content": "You are an agriculture expert assistant. Give helpful answers."
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