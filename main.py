import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image 
import json
import webbrowser
from tkinter import filedialog
from tkinter import ttk
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


def log(event):
	try:
		sreac = search.get().lower()
		text.delete("1.0","end")
		
		text.insert(tk.END,(data[sreac]))
		 # or text.insert(tk.END,(data[text.get("1.0","active")]))

		# text.insert(tk.END,data[sreac])
		status_bar.config(text=f"{sreac}")
		# search.delete(0,END)
	except KeyError:
		ok = messagebox.askyesno(title="OREX dictionary",message="404 not found do you went to search online")
		if ok:
			webbrowser.open(f"Google chorme/https://www.google.com/search?q={sreac}")
		
			

def speak():
	pass
	# song =text.get("1.0","end")
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
	text.insert(tk.END,data[result])

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
	text.insert(tk.END,data[result])
global sul
sul=10
def increase():
	global sul
	sul += 1
	get = text.get("1.0","end")
	current_word = list(get)
	try:
		result = current_word[current_word.index(get)]
	except (ValueError , IndexError):
		result = None
		text.config(font=("Arial",f"{sul}","normal"))
		num.delete(0,END)
		num.insert(0,int(sul))
def discrease():
	global sul
	sul -= 1
	get = text.get("1.0","end")
	current_word = list(get)
	try:
		result = current_word[current_word.index(get)]
	except (ValueError , IndexError):
		result = None
		text.config(font=("Arial",f"{sul}","normal"))
		num.delete(0,END)
		num.insert(0,sul)

def up(event):
	num2 = num.get()
	text.config(font=("Arial",f"{num2}","normal"))
icon = PhotoImage(file="Search Button.png")
photo = PhotoImage(file="volumeup.png")
forward = ImageTk.PhotoImage(Image.open("back.jpeg"))
backward = ImageTk.PhotoImage(Image.open("forward.jpeg"))



search= Entry(font=5,width=50,selectbackground="gray",borderwidth=0)
search.pack(pady=20)
search.insert(0,"Enter your word")
search.config(state=DISABLED)
search.bind("<Button-1>",act)
search.bind("<Return>",log)
# search.bind("<Button-1>",save)


search_but= Button(image=icon,bg="#0f00f0",borderwidth=0,command=lambda:log(log))
search_but.place(x=580,y=15)


zoom = Button(text="+",bg="#0f00f0",borderwidth=0,command=increase)
zoom.place(x=60,y=0)


dis = Button(text="-",bg="#0f00f0",borderwidth=0,command=discrease)
dis.place(x=0,y=0)

speak_but= Button(image=photo,borderwidth=0,bg="#0f00f0",command=speak)
speak_but.place(x=480,y=45)


# 
text = Text(window, height=40, width=65,bg="#ffffff",borderwidth=0)
text.pack(pady=34,expand=False,fill=BOTH)

speak_bu= Button(image=backward,borderwidth=0,bg="#0f00f0",command=back_for)
speak_bu.place(x=0,y=45)
speak_bu= Button(image=forward,borderwidth=0,bg="#0f00f0",command=move_for)
speak_bu.place(x=650,y=45)

num = Entry(font=5,width=3,selectbackground="gray",borderwidth=0)
num.bind("<Return>",up)
num.place(x=30,y=0)

num.insert(0,"10")

status_bar = Label(window, text='', relief= GROOVE,anchor=N,bg="#0f00f0",width=30,highlightthickness=2.4,bd=0)
status_bar.place(x=260,y=60)

# status_ba = Label(window, text='', relief= GROOVE,anchor=N,bg="#0f00f0",width=2,highlightthickness=2.4,bd=0)
# status_ba.place(x=33,y=0)

# volum_slider = ttk.Scale(from_=7,to=20,orient=HORIZONTAL,command=increase,value=1,length=30)
# volum_slider.place(x=0,y=0)


window.mainloop()