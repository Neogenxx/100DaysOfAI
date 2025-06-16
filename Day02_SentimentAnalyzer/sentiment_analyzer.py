from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    print(blob.sentiment)

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    user_input = input("Enter text: ")
    result = analyze_sentiment(user_input)
    print(f"Sentiment: {result}")

