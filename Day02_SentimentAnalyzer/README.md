# Day 2 – Sentiment Analyzer 🧠💬

This is a simple Python-based Sentiment Analyzer built using the `TextBlob` library. It takes input text from the user and classifies the sentiment as **Positive**, **Negative**, or **Neutral** based on the polarity score.

---

## 🔧 Technologies Used

- **Python** – Core programming language.
- **TextBlob** – Used to perform sentiment analysis by calculating polarity and subjectivity from the input text.
- **NLTK** – Used by TextBlob internally for tokenization and part-of-speech tagging. Required for TextBlob to function correctly.

---

## 🚀 How It Works

1. User inputs a sentence.
2. `TextBlob` analyzes the sentiment polarity.
3. Output:
   - `> 0` → **Positive**
   - `< 0` → **Negative**
   - `= 0` → **Neutral**

---

## 📦 Setup Instructions

1. Clone the repository or download the folder.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
