import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


class RuleBasedBot:
    """Simple rule-based chatbot using pattern matching."""

    RESPONSES = {
        r'\b(hi|hello|hey|greetings|howdy)\b': {
            'responses': [
                "Hello! 👋 How can I help you today?",
                "Hey there! What's on your mind?",
                "Hi! Nice to see you. What can I do for you?",
            ]
        },
        r'\b(how are you|how \'s it going|how do you do)\b': {
            'responses': [
                "I'm running great, thanks for asking! 😊",
                "Doing well! Ready to chat with you.",
                "All good! How about you?",
            ]
        },
        r'\b(what is your name|who are you|your name)\b': {
            'responses': [
                "I'm Chip, your friendly rule-based chatbot! 🤖",
                "You can call me Chip! I'm powered by pattern matching.",
                "I'm Chip — simple, but effective!",
            ]
        },
        r'\b(what can you do|your abilities|help)\b': {
            'responses': [
                "I can chat about general topics, tell jokes, share facts, and more! Just ask away. 😄",
                "I'm a rule-based chatbot — try asking me a joke, a fact, or just say hello!",
                "I support greetings, jokes, facts, time queries, and casual conversation!",
            ]
        },
        r'\b(joke|funny|make me laugh)\b': {
            'responses': [
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
                "Why was the JavaScript developer sad? Because he didn't Node how to Express himself! 😂",
                "What's a programmer's favorite hangout place? Foo Bar! 🍺",
                "Why do Python programmers never get stuck? They always have good escape sequences! 🐍",
            ]
        },
        r'\b(what is ai|what is artificial intelligence|explain ai)\b': {
            'responses': [
                "AI (Artificial Intelligence) is the simulation of human intelligence in machines — they can learn, reason, and make decisions! 🧠",
                "AI is a branch of computer science focused on creating systems that can perform tasks requiring human-like intelligence.",
            ]
        },
        r'\b(what is python|tell me about python)\b': {
            'responses': [
                "Python is a popular, beginner-friendly programming language known for its clean syntax and versatility! 🐍",
                "Python is widely used in web development, data science, AI/ML, automation, and more!",
            ]
        },
        r'\b(thanks|thank you|thx|appreciate)\b': {
            'responses': [
                "You're welcome! Happy to help! 😊",
                "Anytime! Don't hesitate to ask more.",
                "Glad I could help! 🙌",
            ]
        },
        r'\b(bye|goodbye|see you|catch up later)\b': {
            'responses': [
                "Goodbye! Have a wonderful day! 👋",
                "See you later! It was great chatting with you! 😊",
                "Bye! Come back anytime! 🌟",
            ]
        },
        r'\b(what time|current time|time is it)\b': {
            'responses': ["I don't have access to a real-time clock, but check your system clock! ⏰"],
        },
        r'\b(who made you|who created you|your developer)\b': {
            'responses': [
                "I was created as a simple rule-based chatbot to showcase Flask and pattern matching!",
                "I'm built with Flask and Python — my creator loves clean code! 💻",
            ]
        },
        r'\b(what is flask|tell me about flask|flask framework)\b': {
            'responses': [
                "Flask is a lightweight Python web framework perfect for building APIs and small web apps! 🍶",
                "Flask is a micro web framework for Python — it's simple, flexible, and great for prototyping!",
            ]
        },
        r'\b(love you|like you|u cool)\b': {
            'responses': [
                "Aww, that's sweet! I like you too! ❤️",
                "You're pretty awesome yourself! 😄",
            ]
        },
        r'\b(how old are you|your age)\b': {
            'responses': [
                "I was just born — every conversation is my first! 🆕",
                "Age is just a number for a chatbot like me! 😄",
            ]
        },
    }

    FALLBACK_RESPONSES = [
        "I'm not sure I understand. Try asking me a joke, or say 'help' to see what I can do! 🤔",
        "Hmm, I didn't catch that. Try 'help' for a list of things I can respond to!",
        "Sorry, I don't have a response for that yet. I'm a simple rule-based bot! 😅",
        "That's interesting! Try asking about AI, Python, jokes, or just say hello! 👋",
    ]

    def respond(self, message: str) -> str:
        """Match the message against patterns and return an appropriate response."""
        lower_msg = message.lower()
        for pattern, data in self.RESPONSES.items():
            if re.search(pattern, lower_msg):
                return self._random_choice(data["responses"])
        return self._random_choice(self.FALLBACK_RESPONSES)

    @staticmethod
    def _random_choice(choices: list[str]) -> str:
        import random
        return random.choice(choices)


bot = RuleBasedBot()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"response": "Please type a message! 💬"}), 200
    bot_response = bot.respond(user_message)
    return jsonify({"response": bot_response})


if __name__ == "__main__":
    app.run(debug=True, port=5000)