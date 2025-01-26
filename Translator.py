from tkinter import *
import googletrans
from textblob import TextBlob
from tkinter import ttk, messagebox

translator = googletrans.Translator()

root = Tk()
root.geometry("880x300")

def translate_it():
        translate_text.delete(1.0,END)
        try:
              from_language_key = list(languages.keys())[list(languages.values()).index(original_combo.get())]
              to_language_key = list(languages.keys())[list(languages.values()).index(translate_combo.get())]
        
              original_input = original_text.get(1.0, END).strip()
        
              translated = translator.translate(original_input, src=from_language_key, dest=to_language_key)
              
              translate_text.insert(1.0, translated.text)
        except Exception as e:
              messagebox.showerror("Translator", str(e))             
      
def clear():
       original_text.delete(1.0, END)
       translate_text.delete(1.0, END)  

languages = googletrans.LANGUAGES
languages_list = list(languages.values())

original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("Helvetica",24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translate_text = Text(root, height=10, width=40)
translate_text.grid(row=0, column=2, pady=20, padx=10)

original_combo = ttk.Combobox(root, width=50, value=languages_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translate_combo = ttk.Combobox(root, width=50, value=languages_list)
translate_combo.current(26)
translate_combo.grid(row=1, column=2)

clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()