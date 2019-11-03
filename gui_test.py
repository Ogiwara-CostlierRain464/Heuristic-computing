import sys
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Monitor")
root.geometry("500x500")

img = ImageTk.PhotoImage(Image.open("monitor.jpg"))
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

root.mainloop()