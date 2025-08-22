# app/main.py
import uvicorn

from app.chatbot import Chatbot


def run_app():
    """Start the chatbot in CLI mode."""
    bot = Chatbot()
    print("🤖 AI Twin Chatbot is running. Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye! 👋")
            break
        print(bot.get_response(user_input))

if __name__ == "__main__":
    # Run FastAPI if you want REST API mode
    uvicorn.run("app.api:app", host="127.0.0.1", port=8000, reload=True)
