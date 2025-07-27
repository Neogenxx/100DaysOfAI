# 📅 Day 12: Resume Analyzer

This project scans resume files (`.pdf` and `.docx`) in the current folder and analyzes them for relevant AI/ML keywords using NLP techniques.

---

## 📦 Libraries Used

| Library       | Purpose                                      |
|---------------|----------------------------------------------|
| `os`          | To scan local directories                    |
| `re`          | For regex cleaning of text                   |
| `docx2txt`    | To extract text from `.docx` files           |
| `PyPDF2`      | To extract text from `.pdf` files            |
| `nltk`        | For tokenization and stopword filtering      |

---

## 🧠 Key Functions

### `extract_text_from_pdf(file_path)`
- Extracts raw text from PDF using `PyPDF2`.

### `extract_text_from_docx(file_path)`
- Extracts text from `.docx` files using `docx2txt`.

### `clean_and_tokenize(text)`
- Cleans text with regex and tokenizes using NLTK.
- Removes stopwords.

### `match_keywords(tokens, KEYWORDS)`
- Matches tokens with predefined skill-related keywords.

### `analyze_resume(file_path)`
- Determines file type and analyzes resume content.
- Prints out matching skills.

---

## ✅ Predefined Keywords Checked

  Python, Machine Learning, Deep Learning, Data Analysis,
  Natural Language Processing, TensorFlow, Keras, Pandas,
  NumPy, Scikit-learn, AI, NLP, Data Science

## 🚀 How to Run

```
 python resume_analyzer.py
```

📂 Place your .pdf or .docx resumes in the same directory as the script.

✅ Ensure that the required libraries are installed.