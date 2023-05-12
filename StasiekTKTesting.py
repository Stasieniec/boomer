import tkinter as tk
from tkinter import ttk
import PIL
from PIL import ImageTk, Image
from utils import*

#setting up the root window
root = tk.Tk()
root.title("Boomer")

#it was 360x640 before
root.geometry('393x852+50+50')
root.resizable(False,False)


header = make_header(root)
header.pack(fill='x')


_body = tk.Frame(root)
_body.pack(fill='x')
body = make_main_body(_body)
body.pack(fill='x')



footer = tk.Frame(root,
                  bg="#F9E21B",
                  pady=20,
                  borderwidth=2,
                  relief="raised")






btn = tk.Button(body,
                 text="CLICK ME",
                 command=header.destroy,
                 width=25,
                 height=25)
btn.pack()


root.mainloop()

