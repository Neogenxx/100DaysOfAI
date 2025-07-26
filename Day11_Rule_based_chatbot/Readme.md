
# 📅 Day 11: Rule-Based Chatbot using NLTK

This project implements a simple rule-based chatbot using the NLTK library. The chatbot responds to predefined patterns and simulates a basic conversation with the user.

---

## 📦 Libraries Used

| Library  | Purpose                             |
|----------|-------------------------------------|
| `nltk`   | To provide the rule-based `Chat` and `reflections` utilities |

---

## 🧠 Key Functions

### `pairs`

- A list of pattern-response pairs used by the chatbot.
- Uses regular expressions to match input patterns.
- Example:
  ```python
  [r"hi|hello", ["Hello!", "Hi there!"]]
  ```

### `reflections`

- A dictionary provided by NLTK to automatically convert phrases like:
  - “I am” → “you are”
  - “you” → “me”
- Helps make the conversation more natural.

### `start_chat()`

- Initializes and starts the chatbot using `Chat(pairs, reflections)`.
- Accepts user input and provides appropriate responses.

---

## 🖥️ How to Run

1. Save the code in a file named `chatbot.py`
2. Run the script:

```bash
python chatbot.py
```

3. Type your message and interact with the bot.
4. Type `quit` to exit.

---

## 📌 Sample Interaction

```
🤖 Chatbot: Hello! Type 'quit' to end the conversation.

You: hello
Chatbot: Hey! How can I assist you today?

You: what is your name?
Chatbot: I'm a simple rule-based AI chatbot.

You: quit
Chatbot: Goodbye! It was nice talking to you.
```

---

## ✅ Dependencies

Make sure you have the required library:

```bash
pip install nltk
```
