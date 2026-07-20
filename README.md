# 🤖 Chip — Rule-Based Chatbot

A simple, elegant rule-based chatbot built with **Flask** and vanilla **HTML/CSS/JS**. No AI backend required — just pattern matching!

## Features

- 💬 Pattern-matching responses using regex
- 🎨 Modern dark-themed chat UI with smooth animations
- ⚡ Instant responses with typing indicator
- 🏷️ Quick suggestion chips for easy exploration
- 📱 Fully responsive — works on mobile
- 🐍 Python 3.8+ with zero heavy dependencies

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the server
python app.py

# 3. Open http://localhost:5000 in your browser
```

## What It Can Talk About

| Topic | Trigger Examples |
|---|---|
| Greetings | `hi`, `hello`, `hey` |
| Jokes | `joke`, `make me laugh` |
| AI Knowledge | `what is ai`, `artificial intelligence` |
| Python | `what is python`, `tell me about python` |
| Flask | `what is flask`, `flask framework` |
| Identity | `who are you`, `your name` |
| Abilities | `what can you do`, `help` |

Plus casual banter about feelings, age, and more!

## Architecture

```
chatbot/
├── app.py              # Flask backend + rule-based bot logic
├── requirements.txt    # Python dependencies
├── README.md
├── .gitignore
└── templates/
    └── index.html      # Chat UI (HTML + CSS + JS)
```

## How It Works

1. The **Flask backend** (`app.py`) hosts a `RuleBasedBot` class with regex patterns mapped to response sets.
2. Each incoming message is matched against patterns — the first match wins, and a random response from the set is returned.
3. The **frontend** sends messages via POST to `/chat` and renders responses with smooth animations.

## Extending It

Want to add new conversation topics? Just add an entry to `RESPONSES` in `RuleBasedBot`:

```python
r'\b(keyword1|keyword2)\b': {
    'responses': [
        "Response option 1",
        "Response option 2",
    ]
}
```

## Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Font:** Inter (Google Fonts)

## License

MIT

---

Built by **ArchanaMylsamy** 💜