### 📅 Day 9: News Aggregator using NewsAPI

This project fetches live news articles from NewsAPI based on user-defined search terms, and displays them in a clean terminal interface. It demonstrates working with public APIs, secure key storage using `.env`, and user input handling.

---

### 📦 Libraries Used

| Library         | Purpose                                              |
|-----------------|------------------------------------------------------|
| `requests`      | To send GET requests to the NewsAPI                 |
| `os`            | To access environment variables                     |
| `dotenv`        | To load API key securely from a `.env` file         |

---

### 🧠 Key Functions

#### `get_news(api_key, query="AI", language="en", page_size=5)`

* Sends a GET request to NewsAPI with the given query parameters.
* Returns a list of news articles as dictionaries.
* Handles HTTP status errors gracefully.

#### `display_news(articles)`

* Displays the headline and source for each news article.
* Handles empty result sets with a fallback message.

---

### 🖼 Output

* **Terminal Output**:  
  Lists top news headlines with their source in this format:

### 🚀 How to Run

1. **Install dependencies:**

```bash
pip install requests python-dotenv
```
2. **Set up the .env file:**

   Create a file named .env in the project folder with:
```
NEWS_API_KEY=your_api_key_here
```
3. **Run the script:**
```
python news_aggregator.py
```

### 🔐 How to Get a NewsAPI Key

- Visit https://newsapi.org/

- Sign up for a free account

- Copy your API key from the dashboard

- Paste it into your .env file as shown above