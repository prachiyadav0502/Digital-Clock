from tkinter import Tk
from tkinter import Label
import time
import sys

root= Tk()
root.title("Digital Clock")
root.geometry("600x140")
root.resizable(0,0)

def get_time():
    timeVar = time.strftime("%I:%M:%S:%p") #I=hour ,M=minutes ,S=seconds ,p=am-pm
    clock.config(text=timeVar)  
    clock.after(200,get_time)


clock = Label(root,font=("Arial",70),fg="white",bg="black")
clock.pack()

get_time()


root.mainloop()
