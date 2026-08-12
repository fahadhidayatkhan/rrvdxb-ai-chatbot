from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq

from app.config import GROQ_API_KEY
from app.intent import detect_intent
from app.memory import get_history, save_message
from app.rag import search_products


router = APIRouter(prefix="/api/ai", tags=["AI"])

client = Groq(api_key=GROQ_API_KEY)


class ChatRequest(BaseModel):
    message: str
    userId: int


def load_prompt():
    with open("prompts/chatbot.txt", "r", encoding="utf-8") as file:
        return file.read()


@router.post("/chat")
def chat(request: ChatRequest):
    intent = detect_intent(request.message)
    history = get_history(request.userId)
    product_info = search_products(request.message)

    system_prompt = load_prompt()

    system_message = f"""
{system_prompt}

Product information:
{product_info}
"""

    messages = [
        {
            "role": "system",
            "content": system_message
        }
    ]

    messages.extend(history)

    messages.append({
        "role": "user",
        "content": request.message
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = response.choices[0].message.content

    save_message(request.userId, "user", request.message)
    save_message(request.userId, "assistant", reply)

    return {
        "reply": reply,
        "recommendedProducts": [],
        "deal": None,
        "intent": intent
    }