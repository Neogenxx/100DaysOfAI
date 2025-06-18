import requests
import csv
import os
from bs4 import BeautifulSoup
from textblob import TextBlob
from collections import Counter
import matplotlib.pyplot as plt

# Step 1: Scrape headlines from Hindustan Times
def get_headlines(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = []

    for h in soup.find_all("h3"):
        text = h.get_text(strip=True)
        if text and len(text.split()) > 3:
            headlines.append(text)
    return headlines

# Step 2: Analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity 
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Step 3: Run program
if __name__ == "__main__":
    url = "https://www.hindustantimes.com/"
    headlines = get_headlines(url)
    print(f"Headlines fetched: {len(headlines)}\n")

    if not headlines:
        print("No headlines found. Try checking the site or tags.")
    else:
        print("--- Sentiment Analysis of Headlines ---\n")
        results = []
        for i, headline in enumerate(headlines, 1):
            sentiment = analyze_sentiment(headline)
            results.append((headline, sentiment))
            print(f"{i}. {headline}\n→ Sentiment: {sentiment}\n")

        # Save results to CSV inside the current script's folder
        file_path = os.path.join(os.path.dirname(__file__), "headlines_sentiments.csv")
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Headline", "Sentiment"])
            writer.writerows(results)

        # Sentiment summary
        sentiments = [s for _, s in results]
        summary = Counter(sentiments)

        print("\n--- Summary ---")
        for sentiment, count in summary.items():
            print(f"{sentiment}: {count}")

        # Step 6: Visualization
        plt.figure(figsize=(6, 4))
        plt.bar(summary.keys(), summary.values(), color=["green", "red", "gray"])
        plt.title("Sentiment Distribution of Headlines")
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(os.path.join(os.path.dirname(__file__), "sentiment_distribution.png"))
        plt.show()