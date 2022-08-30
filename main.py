import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image 
import json
import webbrowser
from tkinter import filedialog
from tkinter import ttk
import pygame
import pyttsx3
import time
import speech_recognition as sr
# time.sleep(5)

window = tk.Tk()
window.geometry("700x700")
window.config(bg="#000000")
window.tk.call("wm","iconphoto",window._w,tk.PhotoImage(file='C:/Users/USER/Desktop/dictionary/dic.png'))
window.title("OREX Dictionary")
window.resizable(width=False,height=False)

# time.sleep(1)
pygame.mixer.init()


with open ("dictionary.json","r") as json_obj:
		data = json.load(json_obj)


def log(event):
	status_bar.config(state=NORMAL)
	try:
		text.config(state=NORMAL)
		sreac = search.get().lower()
		text.delete("1.0","end")
		
		text.insert(tk.END,(data[sreac]))
		text.config(state=DISABLED)
		 # or text.insert(tk.END,(data[text.get("1.0","active")]))

		# text.insert(tk.END,data[sreac])
		
		# show = Listbox(bg="#ffffff",fg="#cccbbb",width=60,selectbackground="gray",selectforeground="black")
		# show.place(x=200,y=70)
		# show.insert(0,search.icursor(data[sreac]))
		status_bar.delete(0,END)
		status_bar.insert(0,sreac)
		status_bar.config(state=DISABLED)
		search.delete(0,END)
	except KeyError:
		ok = messagebox.askyesno(title="OREX dictionary",message="404 not found do you went to search online")
		if ok:
			webbrowser.open(f"Google chorme/https://www.google.com/search?q={sreac}")
		
	

def speak(event):
	# status_bar.config(state=NORMAL)
	# car = text.get("1.0","end")
	# de = Label(text,width=4,bg="#ffffff")
	# de.place(x=40,y=400)
	why = status_bar.get()
	go = pyttsx3.init()
	voices = go.getProperty('voices')
	go.setProperty('voice', voices[1].id)
	def speak(audio):
		go.say(f"{why}")
		go.runAndWait()

	speak(f"{why}")
	# de.config(text="please wait")
	# if go:
		# time.sleep(1.2)
		
	# status_bar.config(state=DISABLED)

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
	get = status_bar.get().lower()
	current_word = list(data)
	text.config(state=NORMAL)
	status_bar.config(state=NORMAL)
	try:
		result = current_word[current_word.index(get) + 1]
	except (ValueError , IndexError):
		result = None

	search.delete(0,END)
	search.insert(0,result)
	text.delete("1.0","end")
	status_bar.delete(0,END)
	status_bar.insert(0,result)
	text.insert(tk.END,data[result])
	text.config(state=DISABLED)
	status_bar.config(state=DISABLED)

def back_for():
	get = status_bar.get().lower()
	current_word = list(data)
	text.config(state=NORMAL)
	status_bar.config(state=NORMAL)
	try:
		result = current_word[current_word.index(get) - 1]
	except (ValueError , IndexError):
		result = None

	search.delete(0,END)
	search.insert(0,result)
	
	text.delete("1.0","end")
	status_bar.delete(0,END)
	status_bar.insert(0,result)
	text.insert(tk.END,data[result])
	text.config(state=DISABLED)
	status_bar.config(state=DISABLED)
global sul
sul=10
def increase(event):
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
def discrease(event):
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
	if get == 1:
		pass

def up(event):
	global sul
	num2 = num.get()
	# sul += num2
	# zoom.config(value=num2)
	text.config(font=("Arial",f"{num2}","normal"))
icon = PhotoImage(file="Search Button.png")
photo = PhotoImage(file="volumeup.png")
forward = ImageTk.PhotoImage(Image.open("back.jpeg"))
backward = ImageTk.PhotoImage(Image.open("forward.jpeg"))

def sol(event):
	scroll = tk.Scrollbar(window, orient=tk.VERTICAL, command=text.yview)
	text.configure(yscrollcommand=scroll.set)
	scroll.place(x=640,y=100,height=560)
def cal(x):
	get = num.get()
	# get2 = man.config(va)
	text.config(font=get)

# font = tk.StringVar()
# font.set("Arial")

# num = tk.StringVar()
# num.set("10")
search= Entry(font=5,width=50,selectbackground="gray",borderwidth=0)
search.pack(pady=20)
search.insert(0,"Enter your word")
search.config(state=DISABLED)
search.bind("<Button-1>",act)
search.bind("<Return>",log)
# search.bind("<Button-1>",save)


search_but= Button(image=icon,bg="#000000",borderwidth=0,command=lambda:log(log))
search_but.place(x=580,y=15)


zoom = Button(text="+",bg="#ffffff",borderwidth=0,command=lambda:increase(increase))
zoom.place(x=45,y=0)


dis = Button(text="-",bg="#ffffff",borderwidth=0,command=lambda:discrease(discrease))
dis.place(x=0,y=0)

speak_but= Button(image=photo,borderwidth=0,bg="#f0cfff",command=lambda:speak(speak))
# speak_but.
speak_but.place(x=480,y=45)


# 
text = Text(window, height=40, width=65,bg="#000000",borderwidth=0,fg="#ffffff",font=("Arial",10,"normal"))
text.config(state=DISABLED)
text.pack(pady=34,expand=True,fill=BOTH,padx=70)
scroll = tk.Scrollbar(window, orient=tk.VERTICAL, command=text.yview)
text.configure(yscrollcommand=scroll.set)
scroll.place(x=640,y=100,height=560)
scroll.bind("<p>",sol)




speak_bu= Button(image=backward,borderwidth=0,bg="#000000",command=back_for)
speak_bu.place(x=0,y=45)
speak_bu= Button(image=forward,borderwidth=0,bg="#000000",command=move_for)
speak_bu.place(x=650,y=45)

num = Entry(font=5,width=3,selectbackground="gray",borderwidth=0)
num.bind("<Return>",up)
num.bind("<Up>",increase)
num.bind("<Down>",discrease)

num.place(x=14,y=0)

num.insert(0,"10")

status_bar = Entry(window, text='',bg="#000000",fg="#000000", relief= GROOVE,width=30,highlightthickness=2.4,bd=0)
status_bar.config(state=DISABLED)
status_bar.bind("<o>",speak)
status_bar.place(x=260,y=60)

# status_ba = Label(window, text='', relief= GROOVE,anchor=N,bg="#0f00f0",width=2,highlightthickness=2.4,bd=0)
# status_ba.place(x=33,y=0)

# volum_slider = ttk.Scale(from_=7,to=20,orient=HORIZONTAL,command=increase,value=1,length=30)
# volum_slider.place(x=0,y=0)
# option2 = [
# 	None,
# 	"1",
# 	"2",
# 	"3",
# 	"4",
# 	"5",
# 	"6",
# 	"7",
# 	"8",
# 	"9",
# 	"10",
# 	"11",
# 	"12",
# 	"13"
# ]
# option = [
# 	None,
# 	"Arial",
# 	"Arial black"

# ]

# manu = ttk.OptionMenu(window,font,*option)
# manu.place(x=0,y=20)

# man = ttk.OptionMenu(window,num,*option2,command=cal)
# man.place(x=650,y=20)

my_menu =Menu(window)
window.config(menu=my_menu)

add_song =Menu(my_menu)
# my_menu.add_cascade(label="add songs",menu=add_song)
# add_song.add_command(label="Add one song to playlist",command=add)
# add_song.add_command(label="Add many song to playlist",command=add_more)
# add_song.add_command(label="save",command=save)


window.mainloop()