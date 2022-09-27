#!/bin/python

import pyautogui as gui
import time



try:
    file1 = open('speed.conf', 'r')
    Lines = file1.readlines()
    #print(type(Lines))
    speed = float(Lines[0])
    print(f"speed = {speed}")

except FileNotFoundError:
    print("speed.conf Not found")
    speed = 0.2
    file = open("scpeed.conf", "w") 
    file.write("0.2")
    file.close()

while True:

    gui.keyDown('shift')
    time.sleep(speed)
    gui.keyUp('shift')
    time.sleep(speed)

# Python tkinter hello world program
  
from tkinter import *
root = Tk()
a = Label(root, text ="Caps shifter")
a.pack()
  
root.mainloop()
