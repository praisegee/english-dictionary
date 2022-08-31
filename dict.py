from tkinter import *
import webbrowser
from tkinter import messagebox
import json
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import pyttsx3
# import speech_recognition as sr

# Initialize window
window = Tk()
window.title("A-Z Dictionary")
window.geometry("1000x970+200+50")
window.resizable(width=False, height=False)
window.config(bg="#458AFF")
window.tk.call("wm", "iconphoto", window._w, PhotoImage(file="Images/dict-removebg-preview(2).png"))

engine = pyttsx3.init()

with open("dictionary.json") as the_dict:
    data = json.load(the_dict)

# get_input = input("Enter your search: ")
#
# print(data[get_input])


# FUnction for searching
def search(event):
    get_meaning = entry.get().lower()
    if get_meaning != "":
        try:
            text_label.config(state=NORMAL)
            text_label.delete("1.0", "end")
            text_label.insert(END, data[get_meaning])
            text_label.config(state=DISABLED)
            play_entry.config(state=NORMAL)
            play_entry.delete(0, END)
            play_entry.insert(END, get_meaning)
            play_entry.config(state=DISABLED)
            # entry.delete(0, END)
            # text_label.config(text=data[get_meaning])
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
        text_label.config(state=NORMAL)
        text_label.delete("1.0", END)
        text_label.insert(END, data[result])
        text_label.config(state=DISABLED)
        play_entry.config(state=NORMAL)
        play_entry.delete(0, END)
        play_entry.insert(END, result)
        play_entry.config(state=DISABLED)
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
        text_label.config(state=NORMAL)
        text_label.delete("1.0", END)
        text_label.insert(END, data[result])
        text_label.config(state=DISABLED)
        play_entry.config(state=NORMAL)
        play_entry.delete(0, END)
        play_entry.insert(END, result)
        play_entry.config(state=DISABLED)
    else:
        messagebox.showerror(title="Error", message="Search bar is still empty")


def font_size():
    slider_label.delete(0, END)
    slider_label.insert(0, int(scale_1.get()))
    text_label.config(font=("arial", int(scale_1.get())))


def binder(event):
    getter = slider_label.get()
    scale_1.config(value=int(getter))
    text_label.config(font=("arial", getter))


def play_sound():
    get_text = play_entry.get()
    if get_text == "":
        pass
    else:
        engine.say(get_text)
        engine.runAndWait()


# label1 = Label(text="A-Z English Dictionary", bg="#458AFF", font=("arial", 15, "normal"))
# label1.grid(row=0, column=1)

entry_img = PhotoImage(file="Images/entry_image.png")
entry_frame = Frame(window, bg="#458AFF", width=100)
entry_frame.pack(padx=140, pady=6)

entry_bg = Label(entry_frame, image=entry_img, bg="#458AFF")
entry_bg.pack()
entry = Entry(entry_frame, width=22)
# Entry Placeholder
entry.insert(0, "Search Here")
entry.config(state=DISABLED)
# Bind to function click
entry.bind("<Button-1>", click)
entry.bind("<Return>", search)
entry.place(x=12, y=10)


# frame = Frame(window)
# frame.grid(row=0, column=2)
search_img = PhotoImage(file="Images/search_btn.png")
search_btn = Button(image=search_img, borderwidth=0, bg="#458AFF", command=lambda: search(search))
search_btn.place(x=616, y=13)
# Previous and next button
previous_img = ImageTk.PhotoImage(Image.open("Images/previous_ button.png"))
previous_btn = Button(image=previous_img, relief=GROOVE, bg="#458AFF", command=previous_word)
next_img = ImageTk.PhotoImage(Image.open("Images/next_button.png"))
next_btn = Button(image=next_img, relief=GROOVE, bg="#458AFF", command=next_word)
previous_btn.place(x=40, y=15)
next_btn.place(x=100, y=15)

play_img = PhotoImage(file="Images/volumeup.png")
play_btn = Button(image=play_img, borderwidth=0, relief=FLAT, bg="#458AFF", command=play_sound)
play_btn.pack()

# status_bar = Label(text="", bd=1, relief=GROOVE, anchor=E)
# status_bar.grid(row=3, column=0)

scale_1 = ttk.Scale(window, orient="horizontal", length=200, from_=0, to=100, value=10)
scale_1.place(x=760, y=92)

slider_label = Entry(width=4)
slider_label.insert(0, "10")
slider_label.place(x=710, y=89)
slider_label.bind("<Return>", binder)
scale_1.config(command=lambda e: font_size())

play_entry = Entry()
play_entry.config(state=DISABLED)
# play_entry.pack()


text_label = Text(padx=15, pady=10)
text_label.config(state=DISABLED)
text_label.pack(padx=40, pady=10, fill=BOTH, expand=True)
scroll = Scrollbar(orient=VERTICAL, command=text_label.yview)
text_label.configure(yscrollcommand=scroll.set)
scroll.place(x=970, y=119, height=840)


window.mainloop()
