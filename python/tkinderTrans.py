import tkinter as tk
from tkinter import messagebox, ttk
from googletrans import Translator, LANGUAGES
from nltk.tokenize import sent_tokenize

# Uncomment the line below to download the punkt tokenizer model if it's not already downloaded
# nltk.download("punkt")

def translation_process(text, destLang):
    translator = Translator()
    sentences = sent_tokenize(text)
    translated_sentences = []

    for sentence in sentences:
        try:
            translation = translator.translate(sentence, dest=destLang)
            translated_sentences.append(translation.text)
        except Exception as e:
            print(f"Error translating sentence: {sentence}")
            print(f"Error: {e}")
            translated_sentences.append(sentence)  # Append the original sentence in case of error

    translated_text = ' '.join(translated_sentences)
    return translated_text

def translate_text():
    input_text = text_entry.get("1.0", "end-1c")  # Get text from text entry widget
    dest_lang = dest_lang_combobox.get()

    if not input_text.strip():
        messagebox.showerror("Error", "Please enter text to translate.")
        return

    if not dest_lang:
        messagebox.showerror("Error", "Please select a destination language.")
        return

    # Get language code from the language name
    dest_lang_code = lang_code_mapping[dest_lang]

    translated_text = translation_process(input_text, destLang=dest_lang_code)
    translated_textbox.delete("1.0", "end")  # Clear previous text
    translated_textbox.insert("1.0", translated_text)  # Insert translated text

# Create a mapping from language names to language codes
lang_code_mapping = {v: k for k, v in LANGUAGES.items()}

# Create main application window
root = tk.Tk()
root.title("Text Translator")

# Create UI widgets
label = tk.Label(root, text="Enter text to translate:")
label.pack(pady=10)

text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

dest_lang_label = tk.Label(root, text="Select destination language:")
dest_lang_label.pack(pady=5)

dest_lang_combobox = ttk.Combobox(root, values=list(lang_code_mapping.keys()))
dest_lang_combobox.pack()

translate_button = tk.Button(root, text="click to Translate", command=translate_text,bg="royal blue",fg="white")
translate_button.pack(pady=10)

translated_textbox = tk.Text(root, height=5, width=50)
translated_textbox.pack()

# Run the application
root.mainloop()
