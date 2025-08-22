# app/chatbot.py
from app.utils import clean_text, load_config


class Chatbot:
    def __init__(self, name="AI Twin"):
        self.name = name
        self.config = load_config()

    def get_response(self, user_input: str) -> str:
        """Generate a dummy response for now."""
        cleaned = clean_text(user_input)
        if not cleaned:
            return "I didn’t quite catch that. Can you rephrase?"
        
        # Placeholder response (replace with ML model later)
        return f"{self.name}: You said '{cleaned}'. Interesting!"

