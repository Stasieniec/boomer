import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Boomer")
root.geometry('360x640+50+50')
root.resizable(False,False)

def make_header():
    header_place = tk.Frame(root,
                  borderwidth=1,
                  relief="sunken",
                  bg="yellow")
    header = tk.Frame(header_place)
    header.pack()
    lbl_test = tk.Label(header, text="BooooOOMER", bg="yellow")
    lbl_test.config(text = "DOOMER")
    lbl_test.grid(row=0, column=0)
    lbl_test2 = tk.Label(header, text="BooooOOMER", bg="yellow")
    lbl_test2.grid(row = 0, column=1)
    lbl_test3 = tk.Label(header, text="BooooOOMER", bg="yellow")
    lbl_test3.grid(row = 0, column=2)
    return header_place


header = make_header()
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

