import os
import re
import docx2txt
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

# Predefined keywords to match in resume
KEYWORDS = {
    "Python", "Machine Learning", "Deep Learning", "Data Analysis",
    "Natural Language Processing", "TensorFlow", "Keras", "Pandas",
    "NumPy", "Scikit-learn", "AI", "NLP", "Data Science"
}

stop_words = set(stopwords.words('english'))

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def clean_and_tokenize(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return set(filtered_tokens)

def match_keywords(tokens, keywords):
    return keywords.intersection(tokens)

def analyze_resume(file_path):
    print(f"\nAnalyzing: {file_path}")

    if file_path.endswith(".pdf"):
        raw_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        raw_text = extract_text_from_docx(file_path)
    else:
        print("❌ Unsupported file type.")
        return

    tokens = clean_and_tokenize(raw_text)
    matched = match_keywords(tokens, KEYWORDS)

    print(f"✅ Found {len(matched)} matching keywords:")
    for word in sorted(matched):
        print(f"- {word}")

if __name__ == "__main__":
    folder_path = os.getcwd()
    print(f"Scanning directory: {folder_path}")
    files = [f for f in os.listdir(folder_path) if f.endswith((".pdf", ".docx"))]

    if not files:
        print("⚠️ No resumes found in the current directory.")
    else:
        for file in files:
            analyze_resume(os.path.join(folder_path, file))
