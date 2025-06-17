Here is a complete `README.md` file for your **Day 3: News Sentiment Analyzer** project:

---

### 📅 Day 3: News Sentiment Analyzer

This project fetches news headlines from **Hindustan Times**, performs sentiment analysis on each headline using **TextBlob**, and visualizes the sentiment distribution using **matplotlib**.

---

### 📦 Libraries Used

| Library               | Purpose                                   |
| --------------------- | ----------------------------------------- |
| `requests`            | To make HTTP requests to the news website |
| `BeautifulSoup`       | To parse and extract data from HTML       |
| `textblob`            | To perform sentiment analysis             |
| `csv`                 | To store sentiment results in a CSV file  |
| `collections.Counter` | To count sentiment categories             |
| `matplotlib`          | To visualize the sentiment distribution   |
| `os`                  | To manage file paths                      |

---

### 🧠 Key Functions

#### `get_headlines(url)`

* Sends an HTTP request to the given URL.
* Parses the HTML to extract headlines (`<h3>` tags).
* Filters headlines with more than 3 words.
* Returns a list of headlines.

#### `analyze_sentiment(text)`

* Uses `TextBlob` to determine sentiment polarity.
* Returns:

  * `"Positive"` if polarity > 0
  * `"Negative"` if polarity < 0
  * `"Neutral"` if polarity = 0

#### `save_to_csv(headlines, sentiments, path)`

* Saves headlines and their corresponding sentiments to a `.csv` file.

#### `visualize_sentiments(sentiments)`

* Plots and saves a bar chart representing the sentiment distribution.

---

### 🖼 Output

* **CSV File**: `headlines_sentiments.csv` contains each headline with its sentiment.
* **Visualization**: `sentiment_distribution.png` shows the number of Positive, Negative, and Neutral headlines.

---

### 🚀 How to Run

```bash
python new_sentiment_analyzer.py
```

Ensure that your virtual environment is activated and the required packages are installed.


