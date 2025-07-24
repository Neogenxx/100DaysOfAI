import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

def get_news(api_key, query="AI", language="en", page_size=5):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": language,
        "pageSize": page_size,
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["articles"]
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return []

def display_news(articles):
    if not articles:
        print("No news articles found.")
        return
    print("\n🗞️ Top Headlines:\n")
    for idx, article in enumerate(articles, 1):
        title = article.get("title", "No Title")
        source = article.get("source", {}).get("name", "Unknown Source")
        print(f"{idx}. {title} - {source}")

if __name__ == "__main__":
    if not API_KEY:
        print("⚠️ Error: NEWS_API_KEY not found. Please set it in a .env file.")
    else:
        topic = input("Enter a topic to search (default: AI): ") or "AI"
        language = input("Enter language code (default: en): ") or "en"
        page_size = input("Enter number of articles to fetch (default: 5): ") or "5"

        try:
            articles = get_news(API_KEY, query=topic, language=language, page_size=int(page_size))
            display_news(articles)
        except Exception as e:
            print(f"❌ Error occurred: {e}")
