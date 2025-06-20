# 📝 Day 5 – Text Summarizer (GUI Edition)

This project is a simple **text summarization tool** built using the `sumy` library and `Tkinter` for a user-friendly interface. It allows users to input or load a `.txt` file, summarize its content using extractive summarization (LSA), and save the output.

---

## 🔧 Libraries Used

| Library        | Purpose                                      |
| -------------- | -------------------------------------------- |
| `sumy`         | For extractive summarization using LSA       |
| `tkinter`      | To build a desktop GUI interface             |
| `os`           | For file path handling                       |
| `filedialog`   | To open file selection dialog                |
| `messagebox`   | To display save and error messages           |
| `scrolledtext` | To create scrollable text input/output areas |

---

## 🧠 Key Functions

### `summarize_text(text, sentence_count=3)`

* Uses `sumy`’s LSA summarizer to extract key sentences.
* Returns a short summary of the input text.

### `load_text_from_file()`

* Opens a `.txt` file dialog.
* Loads the content into the text input area.

### `save_summary_to_file(summary)`

* Writes the generated summary to `summary.txt` in the same directory.

### `summarize_action()`

* Retrieves user input or file content.
* Calls the summarizer and displays the result.
* Automatically saves the summary to a file.

---

## 🚀 How to Run

1. **Activate your virtual environment** (if created):

```bash
source .venv/Scripts/activate  # Windows
```

2. **Install the dependencies**:

```bash
pip install sumy
```

3. **Run the application**:

```bash
python summarizer.py
```

---

## 📂 Output

* ✅ **Generated summary** appears in the lower text area.
* 📄 **Saved automatically** as `summary.txt` in the same folder.


