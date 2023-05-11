import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def make_header(root):
    '''
    Creates a place for a for a header and fills it up with a grid.
    To use it, use: 
    header = make_header(the window in which the header should be)
    And then, to place it and make it spread to the whole width:
    header.pack(fill='x')


    '''

    help = ImageTk.PhotoImage(Image.open("icons/help.png"))
    header_place = tk.Frame(root,
                  borderwidth=1,
                  relief="sunken",
                  bg="yellow")
    header = tk.Frame(header_place)
    header.pack()
    lbl_test = tk.Label(header, text="BOOMER", bg="yellow")
    lbl_test.config(text = "DOOMER")
    lbl_test.grid(column=0)
    lbl_test2 = tk.Label(header, width=20, bg="yellow")
    lbl_test2.grid(column=1)
    lbl_test3 = tk.Label(header, image=help)
    lbl_test3['image'] = help
    lbl_test3.grid(column=2)
    return header_place


def make_footer(root):
    '''
    Creates a place for a for a footer (lower menu) and fills it up with a grid.
    To use it, use: 
    footer = make_footer(the window in which the header should be)
    And then, to place it and make it spread to the whole width:
    footer.pack(fill='x')


    '''
    header_place = tk.Frame(root,
                  borderwidth=1,
                  relief="sunken",
                  bg="yellow")
    header = tk.Frame(header_place)
    header.pack()
    lbl_test = tk.Label(header, text="BOOMER", bg="yellow")
    lbl_test.config(text = "DOOMER")
    lbl_test.grid(row=0, column=0)
    lbl_test2 = tk.Label(header, text="BooooOOMER", bg="yellow")
    lbl_test2.grid(row = 0, column=1)
    lbl_test3 = tk.Label(header, text="BooooOOMER", bg="yellow")
    lbl_test3.grid(row = 0, column=2)
    return header_place