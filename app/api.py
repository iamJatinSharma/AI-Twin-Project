# app/api.py
from fastapi import FastAPI
from pydantic import BaseModel

from app.chatbot import Chatbot

app = FastAPI(title="AI Twin API")
chatbot = Chatbot()

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(query: Query):
    response = chatbot.get_response(query.message)
    return {"response": response}
