import tkinter as tk
from tkinter import ttk

def make_header(root):
    '''
    Creates a place for a for a header and fills it up with a grid.
    To use it, use: 
    header = make_header(the window in which the header should be)
    And then, to place it and make it spread to the whole width:
    header.pack(fill='x')


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
