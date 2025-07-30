import os
import re
import html
import base64
import nltk
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Load environment variables
load_dotenv()
CREDENTIALS_FILE = os.getenv("GMAIL_CREDENTIALS")
TOKEN_FILE = os.getenv("GMAIL_TOKEN")

# Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Download NLTK resources if not already available
nltk.download('punkt', quiet=True)

def authenticate_gmail():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def clean_email_body(body):
    body = html.unescape(body)
    soup = BeautifulSoup(body, "html.parser")
    text = soup.get_text()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def summarize(text, sentence_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return ' '.join(str(sentence) for sentence in summary)

def fetch_unread_emails(service, max_results=5):
    results = service.users().messages().list(userId='me', labelIds=['INBOX', 'UNREAD'], maxResults=max_results).execute()
    messages = results.get('messages', [])
    return messages

def extract_email_content(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    payload = msg['payload']
    headers = payload.get("headers", [])
    
    subject = "No Subject"
    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
            break

    parts = payload.get("parts", [])
    body = ""
    for part in parts:
        if part.get("mimeType") == "text/html":
            data = part['body'].get("data", "")
            decoded = base64.urlsafe_b64decode(data).decode("utf-8")
            body += decoded
        elif part.get("mimeType") == "text/plain":
            data = part['body'].get("data", "")
            decoded = base64.urlsafe_b64decode(data).decode("utf-8")
            body += decoded
    return subject, clean_email_body(body)

def main():
    service = authenticate_gmail()
    messages = fetch_unread_emails(service)

    if not messages:
        print("📭 No unread emails found.")
        return

    print(f"\n📥 Found {len(messages)} unread emails.\n")
    for msg in messages:
        subject, body = extract_email_content(service, msg['id'])
        print(f"📌 Subject: {subject}")
        print("📝 Summary:")
        print(summarize(body))
        print("-" * 60)

if __name__ == '__main__':
    main()
