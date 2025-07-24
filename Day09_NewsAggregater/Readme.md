# 🗞️ Day 9 – News Aggregator (100 Days of AI)

📌 Project Overview
This project fetches live news headlines from the internet using the NewsAPI and displays them in a clean, readable format. It allows users to specify search keywords (like "AI", "technology", "sports") and returns top headlines in real-time.

### 🧰 Libraries Used

```
Library	Purpose
requests	To send HTTP requests to NewsAPI
json	To parse and process the JSON responses
os	To read environment variables
dotenv	To securely load the API key from .env
```
### 🧠 Key Functions
get_news(api_key, query='AI', language='en', page_size=5)
Fetches top headlines from NewsAPI based on a search query, language, and page size.

display_news(news_list)
Takes a list of news article dictionaries and prints their titles and sources in a user-friendly format.

### ▶️ How to Run
Step 1: Install Dependencies
```
pip install requests python-dotenv
```
Step 2: Setup .env File
```
NEWS_API_KEY=your_actual_newsapi_key
```
Step 3: Run the Script
```
python day09_news_aggregator.py
```


### 🔐 Security Tips

Keep your API key private.

Do not upload your .env file to GitHub.

Use .gitignore to exclude .env from version control.

🚀 Optional Enhancements
GUI version using Tkinter or PyQt

Add category filters (e.g., technology, sports)

Integrate with a Text-to-Speech engine (combine with Day 8)

Schedule periodic updates with schedule or cron