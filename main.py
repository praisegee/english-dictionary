import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image 
import json
import webbrowser
from tkinter import filedialog
import pygame


# time.sleep(5)

window = tk.Tk()
window.geometry("700x700")
window.config(bg="#0f00f0")
window.tk.call("wm","iconphoto",window._w,tk.PhotoImage(file='C:/Users/USER/Desktop/dictionary/dic.png'))
window.title("OREX Dictionary")

# time.sleep(1)
pygame.mixer.init()


with open ("dictionary.json","r") as json_obj:
		data = json.load(json_obj)


def log():
	try:
		sreac = search.get().lower()
		text.delete("1.0","end")
		text.insert(tk.END,(data[sreac]))
		status_bar.config(text=f"{sreac}")
		# search.delete(0,END)
	except KeyError:
		ok = messagebox.askyesno(title="OREX dictionary",message="404 not found do you went to search online")
		if ok:
			webbrowser.open(f"Google chorme/https://www.google.com/search?q={sreac}")
		
			

def speak():
	song =text.get("1.0","end")
	# pygame.mixer.music.load(song)
	# pygame.mixer.music.play(loops=0)

def save():
	try:
		sreac = search.get().lower()
		# show.insert(tk.END,data[sreac])
		show = Listbox(bg="#ffffff",fg="#cccbbb",width=60,selectbackground="gray",selectforeground="black")
		show.place(x=200,y=70)
		# show.search("1.0", "end", stopindex=None, forwards=True, backwards=True, exact=True, regexp=True, nocase=True, count=True, elide=True).configure(text=data[sreac])
		rat =data[sreac]
		show.option_readfile(rat , priority=None)
		# rat =data[sreac]
	except KeyError:
		pass
		
		# show.config(text=f"{sreac}")
	# search.config(text=)
def act(event):
	search.config(state=NORMAL)
	search.delete(0,END)
	# save()
# data=0
def move_for():
	get = search.get().lower()
	current_word = list(data)
	try:
		result = current_word[current_word.index(get) + 1]
	except (ValueError , IndexError):
		result = None

	search.delete(0,END)
	search.insert(0,result)
	text.delete("1.0","end")
	status_bar.config(text=f"{result}")
	text.insert(END,data[result])
def back_for():
	get = search.get().lower()
	current_word = list(data)
	try:
		result = current_word[current_word.index(get) - 1]
	except (ValueError , IndexError):
		result = None

	search.delete(0,END)
	search.insert(0,result)
	text.delete("1.0","end")
	status_bar.config(text=f"{result}")
	text.insert(END,data[result])

icon = PhotoImage(file="search.png")
photo = PhotoImage(file="volumeup.png")
forward = PhotoImage(file="fastforward_.png")
backward = PhotoImage(file="fastrewind.png")



search= Entry(font=5,width=50,selectbackground="gray",borderwidth=0)
search.pack(pady=20)
search.insert(0,"Enter your word")
search.config(state=DISABLED)
search.bind("<Button-1>",act)
# search.bind("<Button-1>",save)


search_but= Button(image=icon,bg="#0f00f0",borderwidth=0,command=log)
search_but.place(x=580,y=8)


speak_but= Button(image=photo,borderwidth=0,bg="#0f00f0",command=speak)
speak_but.place(x=480,y=45)



text = Text(window, height=40, width=65,font=("Arial black",10,"normal"),bg="#ffffff",selectbackground="gray",selectforeground="black",borderwidth=0)
text.pack(pady=34)
scroll = tk.Scrollbar(window,orient=tk.VERTICAL, command=text.yview)
text.configure(yscrollcommand=scroll.set)
scroll.place(x=680,y=88,height=620)

speak_bu= Button(image=backward,borderwidth=0,bg="#0f00f0",command=back_for)
speak_bu.place(x=0,y=45)
speak_bu= Button(image=forward,borderwidth=0,bg="#0f00f0",command=move_for)
speak_bu.place(x=650,y=45)


status_bar = Label(window, text='', relief= GROOVE,anchor=N,bg="#0f00f0",width=30,highlightthickness=2.4,bd=0)
status_bar.place(x=260,y=60)



window.mainloop()