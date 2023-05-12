import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


Font_tuple = ("Alata", 32)

def make_header(root):
    '''
    Creates a place for a for a header and fills it up with a grid.
    To use it, use: 
    header = make_header(the window in which the header should be)
    And then, to place it and make it spread to the whole width:
    header.pack(fill='x')


    '''



    header_place = tk.Frame(root,
                  bg="yellow")
    header = tk.Frame(header_place, bg="yellow")
    header.pack(pady=5)
    lbl_name = tk.Label(header, text="BOOMER", font=Font_tuple, bg="yellow")
    lbl_name.grid(row = 0,
                  column=0
                  )
    
    lbl_blank = tk.Label(header, bg="yellow", width=10)
    lbl_blank.grid(row = 0,
                  column=1
                  )
    
    _help = Image.open("icons/help.png")
    _help = _help.resize((46,46), Image.ANTIALIAS)
    help= ImageTk.PhotoImage(_help)
    lbl_help = tk.Label(header, image=help, bg="yellow")
    lbl_help.image = help
    lbl_help.grid(row=0,
                  column=2)
    
    _settings = Image.open("icons/settings.png")
    _settings = _settings.resize((46,46), Image.ANTIALIAS)
    settings= ImageTk.PhotoImage(_settings)
    lbl_settings = tk.Label(header, image=settings, bg="yellow")
    lbl_settings.image = settings
    lbl_settings.grid(row=0,
                  column=3)
    

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