import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time
import random as ra


window= tk.Tk()
window.geometry("600x700")
window.config(bg="#0f49b5")
window.title("Dictionary")
window.tk.call("wm","iconphoto",window._w,tk.PhotoImage(file='C:/Users/USER/Desktop/dictionary/dic.png'))



def next():
	# time.sleep(1)
	window.destroy()
	time.sleep(0)
	import main

fram = tk.Frame(width=264,height=200) 
fram.pack()
fram.place(anchor="center",relx=0.5, rely=0.34)
icon = ImageTk.PhotoImage(Image.open("images.png"))
labe = tk.Label(fram, image=icon)
labe.grid(row=0,column=0)


photo = PhotoImage(file="button2.png")





massage = """
	You can use the volume button to read

"""
mass = """
	rate us
"""
mas="""
	OREX Dictionary is best dictionary you can ever find
"""


dey = massage,mass,mas
song = ra.choice(dey)




page = Button(image=photo,text="let go",bg="#0f00f0",command=next)
page.grid(row=0,pady=370,padx=180)

label = Label(text=f"{song}",bg="#0f00f0",width=100)
label.place(x=0,y=450)

	


window.mainloop()