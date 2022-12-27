import pyautogui
from tkinter import *
from tkinter.filedialog import *
#import tkinter.font as font

root = Tk()

canvas1 = Canvas(root, width = 200, height = 120)
canvas1.pack()

def takeScreenshot():
    Screenshot = pyautogui.screenshot()
    save_path  = asksaveasfilename()
    Screenshot.save(save_path+" .png")
#myFont = font.Font(size = 30)
Button = Button(text="Take Screenshot",command = takeScreenshot,font=10)
#Button['font'] = myFont

canvas1.create_window(100,100,window=Button)

root.mainloop()