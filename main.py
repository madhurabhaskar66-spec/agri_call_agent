from fastapi import FastAPI, HTTPException
from ai_agent import get_ai_response
from voice import text_to_speech

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Voice Agent Running Successfully 🚀"}

@app.get("/call")
def make_call(phone: str, query: str):

    # Validate Indian number
    if not phone.startswith("+91") or len(phone) != 13:
        raise HTTPException(
            status_code=400,
            detail="Phone number must be in format +91XXXXXXXXXX"
        )

    # Step 1: Get AI response
    ai_reply = get_ai_response(query)

    # Step 2: Convert to speech
    audio_file = text_to_speech(ai_reply)

    return {
        "status": "success",
        "phone": phone,
        "user_question": query,
        "agent_reply": ai_reply,
        "audio_file": audio_file
    }