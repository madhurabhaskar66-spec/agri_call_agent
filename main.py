from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ai_agent import get_ai_response

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Agri AI Running"}

@app.post("/chat")
def chat(data: Message):
    reply = get_ai_response(data.message)
    return {"reply": reply}