


# from cgitb import text
import _tkinter
import pyttsx3 as speak
import tkinter as tk
from tkinter import HORIZONTAL, VERTICAL, BaseWidget, IntVar, PhotoImage 
from tkinter import DISABLED, NORMAL, StringVar, ttk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import execute as source

def page():
    root = tk.Tk()
    root.tk.call("wm", "iconphoto", root._w, PhotoImage(file = "Images/Dictionary image_1.png"))
    # frame = tk.Frame()
    # label = tk.Label(frame)
    # frame.place(x=100, y=100 )
    root.geometry("880x600")
    root.config(bg="Sky blue")
    root.title("Dictionary")
    # root.resizable(height=False, width=False)
    word_label= tk.Label(text="Word:", bg="Sky Blue")
    word_label.place(x=200, y=50)

    def default(event):
        word_entry.config(state=NORMAL)
        word_entry.delete(0,"end")


    # word = word_var.get()
    recents = [None]

    word_var = StringVar()
    word_entry = tk.Entry(root,width= "50",textvariable=word_var)
    word_entry.insert(tk.END, "Search Word")
    word_entry.config(state=DISABLED)
    word_entry.bind("<Button-1>", default)
    word_entry.place(x=250, y=50,height=26)
    # call function
    meaning = tk.Text(root)
    global count
    count = 0


    

    
    # print(size_scale.get())
    font_frame = tk.LabelFrame(root, text="Font size")
    font_frame.place(x=782,y=200)
    font_frame.config(bg="Sky blue")

    size_entry = tk.Entry(text='')
    size_entry.config(width=4)
    def track(x):
        size_entry.delete(0, "end")
        size_entry.insert(0,int(size_scale.get()))
        meaning.config(font=(font_var.get().lower(),int(size_scale.get())))
    size_entry.place(x=805, y=160, height=20)
    size_scale = ttk.Scale(font_frame, orient=VERTICAL, from_=100, to=1, value=20,command=track)
    size_entry.insert(0,int(size_scale.get()))

    size_scale.pack(pady=20)

    def bind(event):
        try:
            the_size = size_entry.get()
            size_entry.delete(0, "end")
            size_scale.config(value=the_size)
            size_entry.insert(0,int(size_scale.get()))
            meaning.config(font=(font_var.get().lower(), int(size_scale.get())))
        except _tkinter.TclError:
            mb.showerror(title= "Invalid Input", message="Sorry,\nYou entered invalid font size!")   
            size_entry.delete(0, "end")
            size_entry.insert("end", 20)



    fonts = [
        None,
        "Romans",
        "Arial",
        "Calibri",
        "Algerian",
        "Cambria",
        "Cambara",
        "Century",
        "Corbel",
        "Elephant"
    ]



    size_entry.bind("<Return>", bind)

    font_label = tk.Label(text="Font:")
    font_label.place(x=745, y=14)
    font_label.config(bg="Sky blue")
        



    def call(event):
        meaning.config(state=NORMAL)
        result = source.search(word_var.get().lower())
        meaning.delete("1.0","end")
        if result != None:
            if word_var.get().lower() not in recents:
                recents.append(word_var.get().lower())

            recent_label = tk.Label(text="Recent:", bg="Sky Blue")
            recent_label.place(x=52, y=18)
            recent_words = ttk.OptionMenu(root, word_var, *recents, command=call)
            recent_words.place(x=100, y=18)
            meaning.config(font=(font_var.get().lower()))
            # real_mean = tk.Label(meaning, anchor="n", text=result ,wraplength=800)
            # real_mean.pack()
            meaning.insert("end", result)       
            # forward(word_var.get().lower())
            global count
            count += 1
            meaning.config(state=DISABLED)    
            
            #   
        else:
            pass
            meaning.config(state=DISABLED)    


    # speech function
    def narrate():
        meaning.config(state=NORMAL)    
        result = source.search(word_var.get().lower())
        speaker = speak.init()
        speaker.say(word_var.get().lower())
        speaker.runAndWait()
        meaning.config(state=DISABLED)    
    font_var = tk.StringVar()
    font_option = ttk.OptionMenu(root, font_var, *fonts)  
    font_var.set("Romans") 
    font_option.place(x=780, y=10)

    def back():
        # try:
        meaning.config(state=NORMAL)    

        try:
            present_word = recents.index(word_var.get().lower())
            lastword = present_word - 1
            if present_word != 1:   
                last_word = recents[lastword]
                word_var.set(last_word)
            call(call)

        except ValueError:
            present_word = word_var.get().lower()
            last_word = recents[-1]
            # recents.append(present_word) 
            word_var.set(last_word)
            # print(last_word)
        # except IndexError:
        #     pass
        meaning.config(state=DISABLED)    

    meaning.pack(padx=100, pady=100, expand=True)

    def forward():
        meaning.config(state=NORMAL)    
        try:
            present_word = recents.index(word_var.get().lower())
            next_word = present_word + 1
            word_var.set(recents[next_word])
            call(call)
            # print(present_word)
            # print(next_word)
        except IndexError:
            pass
        except ValueError:
            pass
        meaning.config(state=DISABLED)    
        

    global font
    font = 10
        


    # frames
    word_entry.bind("<Return>", call)


    back_frame = tk.Frame(root)
    back_frame.place(x=10,y=50)
    front_frame = tk.Frame(root)
    front_frame.place(x=40, y=50)

    play_frame = tk.Frame(root)

    # pictures
    back_pic = ImageTk.PhotoImage(Image.open("Images/back.jpeg"))
    front_pic = ImageTk.PhotoImage(Image.open("Images/back - Copy.jpeg"))

    play_pic = ImageTk.PhotoImage(Image.open("Images/play.jpeg"))

    back_btn = tk.Button(back_frame,image=back_pic, borderwidth=0, command=back)
    back_btn.pack()
    front_btn = tk.Button(front_frame,image=front_pic,borderwidth=0, command=forward)
    front_btn.pack()



    # call button
    speech_picture = PhotoImage(file = "Images/Search Button.png")
    search_btn = tk.Button(root,image=speech_picture,borderwidth=0,command=lambda : call(call))
    search_btn.place(x=555, y=50)
    # speech button
    speech_frame = tk.Frame()
    speech_frame.place(x=700, y=20)
    speech_btn = tk.Button(speech_frame,image=play_pic,borderwidth=0, command=narrate)
    speech_btn.pack()

    # stop_btn = tk.Button(root, text="Stop", bg="Sky Blue")
    # stop_btn.place(x=760, y=18)
    scroll = ttk.Scrollbar(root, orient=VERTICAL, command=meaning.yview)
    scroll.place(x=860, y=0,height=500)
    meaning.config(yscrollcommand=scroll.set)

    # fr = tk.Message(frame)
    # fr.pack()

    # import pyttsx3

    # def onStart():
    #     print('starting')

    # def onWord(name, location, length):
    #     print('word', name, location, length)

    # def onEnd(name, completed):
    #     print('finishing', name, completed)

    # engine = pyttsx3.init()

    # engine.connect('started-utterance', onStart)
    # engine.connect('started-word', onWord)
    # engine.connect('finished-utterance', onEnd)

    # sen = 'Geeks for geeks is a computer portal for Geeks'


    # engine.say(sen)
    # engine.runAndWait()

    root.mainloop() 


if __name__ == "__main__":
    page()
