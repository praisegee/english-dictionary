import page

import tkinter as tk
from PIL import  ImageTk, Image
from tkinter import PhotoImage, ttk
import pyttsx3 as speak
# import page


window = tk.Tk()

window.geometry("800x500")
window.config(bg="white")
# window.config(bg="Light Grey")
window.title("Welcome")
window.tk.call("wm", "iconphoto", window._w, PhotoImage(file = "Images/Dictionary image_1.png"))


# photo = PhotoImage(file = "Dictionary image_1.png")

frame = tk.Frame(window)
frame.grid(row=10, column=3, padx=300, pady=20)


logo = ImageTk.PhotoImage(Image.open("Images/backdrop.jpeg"))
lb = tk.Label(frame, image=logo)
lb.pack()


welcome_label = tk.Label(window, text="WELCOME", font=("bold", 25))
welcome_label.place(x=340, y=260)


def start():
    speaker = speak.init()
    speaker.say("Hello" + "..." + " and welcome to My dictionary")
    speaker.runAndWait()
    window.destroy()
    page.page()

start_frame = tk.Frame(window)
start_frame.grid(row=12, column=3, padx=200,pady=100)

start_btn_pic = ImageTk.PhotoImage(Image.open("Images/Get started image.png"))
start_btn = tk.Button(start_frame, image=start_btn_pic,borderwidth=0, command = start)
start_btn.pack() 




# def home():
#     main()
# import page
# home_frame = tk.Frame()
# home_frame.place(x=10,y=10)
# home_pic = ImageTk.PhotoImage(Image.open("home.jpeg"))
# home_btn = tk.Button(home_frame, image=home_pic, borderwidth=0, command=home)
# home_btn.pack()
    



window.mainloop()

# main()