#Text Translator
#By: Yogita Dahiya

from tkinter import *
from tkinter import messagebox
from deep_translator import GoogleTranslator

# --------- Function to Translate Text ---------
def translate_text():
    try:
        text_to_translate = input_box.get("1.0", "end-1c")
        selected_lang = lang_var.get()

        # Check if user entered something
        if text_to_translate.strip() == "":
            messagebox.showwarning("Oops!", "Please type something to translate 🙂")
            return

        # Translate the text
        translated_text = GoogleTranslator(source="auto", target=selected_lang).translate(text_to_translate)

        # Display result in output box
        output_box.delete("1.0", "end")
        output_box.insert("1.0", translated_text)

        status_label.config(text="✅ Translation Successful!", fg="green")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong 😢\n\nDetails: {e}")
        status_label.config(text="⚠️ Translation Failed!", fg="red")


# --------- Function to Clear Both Text Boxes ---------
def clear_text():
    input_box.delete("1.0", "end")
    output_box.delete("1.0", "end")
    status_label.config(text="📝 Ready for translation...", fg="blue")


# --------- Create Main Window ---------
root = Tk()
root.title("🌐 Human-Friendly Text Translator")
root.geometry("700x550")
root.resizable(False, False)
root.config(bg="#f0faff")

# --------- Heading ---------
heading = Label(
    root,
    text="🌍 Language Translator",
    font=("Helvetica", 22, "bold"),
    bg="#f0faff",
    fg="#1a73e8"
)
heading.pack(pady=15)

# --------- Input Text Section ---------
input_label = Label(root, text="🔹 Enter text to translate:", font=("Arial", 12), bg="#f0faff", fg="#333")
input_label.pack()
input_box = Text(root, height=6, width=70, font=("Arial", 12), bd=2, relief=SOLID)
input_box.pack(pady=8)

# --------- Language Dropdown ---------
lang_label = Label(root, text="🌐 Select language:", font=("Arial", 12), bg="#f0faff", fg="#333")
lang_label.pack(pady=5)

lang_var = StringVar(value="en")  # Default language
languages = ["en", "hi", "fr", "es", "de", "ta", "te", "mr", "gu", "bn"]
language_menu = OptionMenu(root, lang_var, *languages)
language_menu.config(font=("Arial", 11), width=10, bg="#e1f5fe")
language_menu.pack()

# --------- Buttons Frame ---------
btn_frame = Frame(root, bg="#f0faff")
btn_frame.pack(pady=12)

translate_button = Button(
    btn_frame,
    text="Translate ✅",
    command=translate_text,
    font=("Arial", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=15,
    pady=5,
    relief=RAISED
)
translate_button.grid(row=0, column=0, padx=8)

clear_button = Button(
    btn_frame,
    text="Clear 🧹",
    command=clear_text,
    font=("Arial", 13, "bold"),
    bg="#f44336",
    fg="white",
    padx=15,
    pady=5,
    relief=RAISED
)
clear_button.grid(row=0, column=1, padx=8)

# --------- Output Text Section ---------
output_label = Label(root, text="🔸 Translated text:", font=("Arial", 12), bg="#f0faff", fg="#333")
output_label.pack()
output_box = Text(root, height=6, width=70, font=("Arial", 12), bd=2, relief=SOLID)
output_box.pack(pady=8)

# --------- Status Label ---------
status_label = Label(root, text="📝 Ready for translation...", font=("Arial", 11), bg="#f0faff", fg="blue")
status_label.pack(pady=5)

# --------- Run the App ---------
root.mainloop()
