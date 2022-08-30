import tkinter as tk
from tkinter import *
import pyaudio
import pyttsx3
import speech_recognition as sr


window = tk.Tk()
window.geometry("700x300")


# num = pyttsx3.init()
# num.say("se dede ni e de")

# num.setProperty('voice', voices[1].id)
# voices = num.getProperty('voices')
# pyttsx3.init(driverName='sapi5') 
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# # num.runAndWait()
# for voice in voices:
#    engine.setProperty('voice', voice.id)  # changes the voice
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
# engine = pyttsx3.init()
# # engine.setProperty('voice', voice_id)  # use whatever voice_id you'd like
# # engine.say('The quick brown fox jumped over the lazy dog.')
# # engine = pyttsx3.init('sapi5')
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice', voices[1].id)
# # def speak(audio):
# #     engine.say(audio)
# #     engine.runAndWait()
# speak('Hello World')
def main():
	r= sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)

		print("say sometime")
		audio = r.listen(source)
		try:
			print("you say: \n " + r.recognize_google(audio))
		except Exception as e:
			print("Errr: " + str(e))
if __name__ == "__main__":
	main()
fun = Entry(width=20)
fun.pack(pady=20)
window.mainloop()

