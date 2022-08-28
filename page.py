from tkinter import *

window = Tk()
window.title("A-Z Dictionary")
window.geometry("620x690")
window.resizable(width=FALSE, height=FALSE)
window.tk.call("wm", "iconphoto", window._w, PhotoImage(file="Images/dict-removebg-preview(2).png"))
window.config(bg="#458AFF")

image_frame = Frame(window, bg="#458AFF")
image_frame.grid(row=1, column=1, padx=40, pady=10)
bg_image = PhotoImage(file="Images/dict-removebg-preview(2).png")
label = Label(image_frame, image=bg_image, bg="#458AFF")
label.grid(row=0, column=1, padx=10)


def next_page():
    window.destroy()
    import dict


btn_image = PhotoImage(file="Images/button2.png")
btn = Button(image=btn_image, relief=GROOVE, width=250, command=next_page)
btn.grid(row=2, column=1, pady=20)

window.mainloop()
