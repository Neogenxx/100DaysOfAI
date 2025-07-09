import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def add(x, y):
    return x + y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

# GUI setup
root = tk.Tk()
root.title("Calculator")
root.geometry("200x600")

frame = tk.Frame(root)
frame.pack(pady=20)

load_btn = tk.Button(frame, text="1")
load_btn.pack(side=tk.LEFT, padx=10)
load_btn = tk.Button(frame, text="2")
load_btn.pack(side=tk.LEFT, padx=10)
load_btn = tk.Button(frame, text="3")
load_btn.pack(side=tk.LEFT, padx=10)
load_btn = tk.Button(frame, text="4")
load_btn.pack(side=tk.LEFT, padx=10)
load_btn = tk.Button(frame, text="5")
load_btn.pack(side=tk.LEFT, padx=10)
load_btn = tk.Button(frame, text="6")
load_btn.pack(side=tk.LEFT, padx=10)
load_btn = tk.Button(frame, text="7")
load_btn.pack(side=tk.LEFT, padx=10)
load_btn = tk.Button(frame, text="8")
load_btn.pack(side=tk.LEFT, padx=10)
load_btn = tk.Button(frame, text="9")
load_btn.pack(side=tk.LEFT, padx=10)
load_btn = tk.Button(frame, text="0")
load_btn.pack(side=tk.LEFT, padx=10)

equal_btn = tk.Button(frame, text="=")
equal_btn.pack(side=tk.LEFT)

status_label = tk.Label(root, text="", fg="red")
status_label.pack()

tk.Label(root, text="Output:").pack()
text_area = scrolledtext.ScrolledText(root, height=12, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

tk.Label(root, text="Summary:").pack()
output_area = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD)
output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

root.mainloop()

