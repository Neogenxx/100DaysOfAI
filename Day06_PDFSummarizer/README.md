# 📄 Day 6: PDF Summarizer

A simple GUI tool that extracts text from a PDF file using `pdfplumber` and generates a concise summary using the `sumy` library.

---

## 🧠 Project Overview

This app helps you quickly summarize large PDF documents by:
- Extracting raw text from each page
- Using NLP techniques (LSA algorithm) to create a short summary
- Displaying the summary in a scrollable text box

---

## 🛠️ Libraries Used

| Library        | Purpose                                      |
| -------------- | -------------------------------------------- |
| `sumy`         | For extractive summarization using LSA       |
| `tkinter`      | For GUI file upload and text display         |
| `filedialog`   | To open file selection dialog                |
| `scrolledtext` | To create scrollable text input/output areas |
| `pdfplumber`   | For extracting text from PDF files           |   

---

## 🧠 Key Functions

### `summarize_text(text, sentence_count=5)`

* Uses `sumy` PlaintextParser and LsaSummarizer to process the text.
* Returns the summary as a string.

### `open_file()`

* Opens a `.pdf` file dialog.
* Extracts text from the selected PDF using extract_text_from_pdf()
* If text is found, it summarizes it using summarize_text()

### `extract_text_from_pdf(file_path)`

* Opens the PDF using pdfplumber.
* Extracts text from each page using .extract_text().
* Concatenates all text and returns it as a single string.



---

## ▶️ How to Run

1. **Activate your virtual environment** (if created):

```bash
source .venv/Scripts/activate  # Windows
```

2. **Install dependencies**:

```bash
pip install pdfplumber sumy
```

3. **Run the app**:

```bash
python pdfsummarizer.py
```

4. **Use the GUI**:

* Click `Open PDF & Summarize`
* Select a PDF file
* View the summarized output

---

## 📂 Output

* Extracts text from the pdf and gives a brief summary of its contents
* GUI-based summarization tool

---

## 📌 Notes

* Works best on PDFs with selectable/extractable text.
* For scanned image PDFs, consider integrating OCR with `pytesseract`.

---


