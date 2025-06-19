import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, sentence_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

def load_text_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        status_label.config(text=f"Loaded: {os.path.basename(file_path)}")

def save_summary_to_file(summary):
    output_path = os.path.join(os.path.dirname(__file__), "summary.txt")
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(summary)
    messagebox.showinfo("Saved", f"Summary saved to: summary.txt")

def summarize_action():
    text = text_area.get(1.0, tk.END).strip()
    if not text:
        messagebox.showwarning("Input Required", "Please enter or load text to summarize.")
        return
    try:
        summary = summarize_text(text)
        output_area.delete(1.0, tk.END)
        output_area.insert(tk.END, summary)
        save_summary_to_file(summary)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Text Summarizer - GUI Edition")
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(pady=10)

load_btn = tk.Button(frame, text="Load .txt File", command=load_text_from_file)
load_btn.pack(side=tk.LEFT, padx=10)

summarize_btn = tk.Button(frame, text="Summarize Text", command=summarize_action)
summarize_btn.pack(side=tk.LEFT)

status_label = tk.Label(root, text="", fg="gray")
status_label.pack()

tk.Label(root, text="Input Text:").pack()
text_area = scrolledtext.ScrolledText(root, height=12, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

tk.Label(root, text="Summary:").pack()
output_area = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD)
output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

root.mainloop()
