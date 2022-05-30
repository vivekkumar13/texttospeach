import tkinter as tk
from tkinter import *

import pyttsx3


engine=pyttsx3.init()

class Widget():
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('tts')
        self.root.resizable(0,0)
        self.labell=tk.Label(self.root,text="what do you want me to speak")
        self.labell.pack()
        self.entery=tk.Entry(self.root)
        self.entery.pack()
        self.button=tk.Button(self.root,text="speak",command=self.clicked)
        self.button.pack()
        
    def speak (self,text):
        engine.say(text)
        engine.runAndWait()

    def clicked(self):
        text=self.entery.get()
        self.speak(text)

if __name__=="__main__" :
    widget=Widget()

