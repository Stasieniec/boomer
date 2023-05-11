import tkinter as tk
from tkinter import ttk
from utils import*

root = tk.Tk()
root.title("Boomer")
root.geometry('360x640+50+50')
root.resizable(False,False)

header = make_header(root)
header.pack(fill='x')
body = tk.Frame(root)
footer = tk.Frame(root,
                  borderwidth=2,
                  relief="raised")




btn = tk.Button(body,
                 text="CLICK ME",
                 width=25,
                 height=25)
btn.pack()

message = tk.Label(footer,
                     text="BOOMER",
                     foreground="white",
                     background="black",)
message.pack()


header.pack()
body.pack()
footer.pack()
root.mainloop()

