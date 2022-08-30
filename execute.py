

import json 
import tkinter as tk
from tkinter import messagebox as mb
import _tkinter
from tkinter import ttk
import webbrowser as wb
def search(word):
    user = word
    with open("dictionary.json", "r") as dic:
        _dict = json.load(dic)
    if user in _dict:
        return _dict[user]

    if user not in _dict:
        unseen_word = mb.askyesno(title="Unseen word", message=f"""Sorry,the word you are looking for is unavalabile!
Would you like to search for "{user}" online?""")
        if unseen_word:
            ww = wb.open(f"https://www.google.com/search?q=definition+of+{user}")
