import pdfplumber
from tkinter import Tk, filedialog, messagebox, scrolledtext, Button, Label
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return "\n".join(str(sentence) for sentence in summary)


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        raw_text = extract_text_from_pdf(file_path)
        if not raw_text.strip():
            messagebox.showerror("Error", "No extractable text found in the PDF.")
            return
        summary = summarize_text(raw_text)
        text_box.delete(1.0, "end")
        text_box.insert("end", summary)


# GUI Setup
app = Tk()
app.title("PDF Summarizer")
app.geometry("700x600")

Label(app, text="Summarized Output", font=("Arial", 16)).pack()
text_box = scrolledtext.ScrolledText(app, wrap="word", font=("Arial", 12))
text_box.pack(expand=True, fill="both", padx=12, pady=12)

Button(app, text="Open PDF & Summarize", command=open_file).pack(pady=10)

app.mainloop()
