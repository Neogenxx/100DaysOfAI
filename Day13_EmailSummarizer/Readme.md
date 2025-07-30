# 📩 Day 13: Gmail Email Summarizer

This project fetches the latest unread emails from your Gmail inbox using the Gmail API and summarizes their content using NLP techniques.

---

## 📌 Project Overview

- Uses Gmail API with OAuth2 authentication
- Extracts subject and body from unread emails
- Cleans the email content
- Summarizes using Sumy's LSA summarizer
- Console output: subject + summary

---

## 📚 Libraries Used

- `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`
- `google-api-python-client`
- `python-dotenv`
- `bs4`, `html`, `re`
- `sumy`, `nltk`

Install them:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib python-dotenv sumy nltk beautifulsoup4
```
---

## 🔑 Setup & Authentication
  - Go to: https://console.cloud.google.com
  - Create a new project

- Enable Gmail API

- Configure OAuth2 consent screen

- Download credentials.json and save it in your project folder

- First run will open a browser to authenticate and generate token.json

 .env example
``` 
GMAIL_CREDENTIALS=credentials.json
GMAIL_TOKEN=token.json
```

## 🛠 How to Run
- Create a .env file with proper Gmail API paths

- Place credentials.json in the same directory

- Run the script:
```
python gmail_summarizer.py
```
