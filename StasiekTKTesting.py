import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Boomer")
root.geometry('600x400+50+50')
root.resizable(False,False)

header = ttk.Label(root)
message = ttk.Label(header, text="BOOMER")
another = ttk.Label(header, text="BOOMER")
another.config(text = "DOOMER")

header.pack()
message.pack()
another.pack()


root.mainloop()

