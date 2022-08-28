from tkinter import *
import webbrowser
from tkinter import messagebox
import json

# Initialize window
window = Tk()
window.title("A-Z Dictionary")
window.geometry("1000x700")
window.config(bg="#458AFF")
window.tk.call("wm", "iconphoto", window._w, PhotoImage(file="Images/dict-removebg-preview(2).png"))

with open("dictionary.json") as the_dict:
    data = json.load(the_dict)

# get_input = input("Enter your search: ")
#
# print(data[get_input])


# FUnction for searching
def search():
    get_meaning = entry.get().lower()
    if get_meaning != "":
        try:
            text_area.delete("1.0", "end")
            text_area.insert(END, data[get_meaning])
            # entry.delete(0, END)
        except KeyError:
            ask = messagebox.askyesno(title="Search Online", message="Sorry Word not found! Would you like to search online")
            if ask:
                webber = webbrowser.open(f"https://www.google.com/search?q={get_meaning}+meaning")
            # text_area.insert(END, f"{get_meaning} not found {webber}")
    elif get_meaning == "":
        messagebox.showerror(title="Error", message="Search box cannot be blank")
    elif get_meaning not in data:
        messagebox.showerror(title="Error", message="Dumb ass")


# Function to enable entry after click
def click(event):
    entry.config(state=NORMAL)
    entry.delete(0, END)


def previous_word():
    get_word = entry.get().lower()
    current_word = list(data)
    if get_word != "":
        try:
            result = current_word[current_word.index(get_word) - 1]
        except (ValueError, IndexError):
            result = None
        entry.delete(0, END)
        entry.insert(0, result)
        text_area.delete("1.0", END)
        text_area.insert(END, data[result])
    else:
        messagebox.showerror(title="Error", message="Search bar is still empty")


# Function to go to next meaning
def next_word():
    get_word = entry.get().lower()
    current_word = list(data)
    if get_word != "":
        try:
            result = current_word[current_word.index(get_word) + 1]
        except (ValueError, IndexError):
            result = None
        entry.delete(0, END)
        entry.insert(0, result)
        text_area.delete("1.0", END)
        text_area.insert(END, data[result])
    else:
        messagebox.showerror(title="Error", message="Search bar is still empty")


# label1 = Label(text="A-Z English Dictionary", bg="#458AFF", font=("arial", 15, "normal"))
# label1.grid(row=0, column=1)

entry_img = PhotoImage(file="Images/entry_image.png")
entry_frame = Frame(window, bg="#458AFF", width=100)
entry_frame.grid(row=1, column=1, padx=140, pady=6)

entry_bg = Label(entry_frame, image=entry_img, bg="#458AFF")
entry_bg.grid(row=0, column=1)
entry = Entry(entry_frame, width=22)
# Entry Placeholder
entry.insert(0, "Search Here")
entry.config(state=DISABLED)
# Bind to function click
entry.bind("<Button-1>", click)
entry.grid(row=0, column=1, padx=120, pady=10)


# frame = Frame(window)
# frame.grid(row=0, column=2)
search_img = PhotoImage(file="Images/search.png")
search_btn = Button(entry_frame, image=search_img, borderwidth=0, bg="#458AFF", command=search)
search_btn.grid(row=0, column=2)
# Previous and next button
previous_btn = Button(entry_frame, text="Previous", relief=GROOVE, bg="#458AFF", command=previous_word)
next_btn = Button(entry_frame, text="Next", relief=GROOVE, bg="#458AFF", command=next_word)
previous_btn.grid(row=0, column=0)
next_btn.grid(row=0, column=3, padx=17)


text_area = Text(width=120, height=30)
text_area.grid(row=2, column=1, padx=17, pady=15)


window.mainloop()
