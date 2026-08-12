from fastapi import FastAPI

from app.chat import router as chat_router


app = FastAPI(
    title="RRVDXB AI Shopping Chatbot",
    version="1.0.0"
)


app.include_router(chat_router)


@app.get("/")
def health_check():
    return {
        "message": "RRVDXB AI Chatbot is running"
    }