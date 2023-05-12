import tkinter as tk
from tkinter import ttk
import PIL
from PIL import ImageTk, Image

#Global stuff
Font_header = ("Alata", 32)
Font_body = ("Alata", 20)
yellow = '#F9E21B'



def make_header(root):
    '''
    Creates a place for a for a header and fills it up with a grid.
    To use it, use: 
    header = make_header(the window in which the header should be)
    And then, to place it and make it spread to the whole width:
    header.pack(fill='x')


    '''
    header_place = tk.Frame(root,
                  bg=yellow)
    header = tk.Frame(header_place, bg=yellow)
    header.pack(pady=5)
    lbl_name = tk.Label(header, text="BOOMER", font=Font_header, bg=yellow)
    lbl_name.grid(row = 0,
                  column=0
                  )
    
    lbl_blank = tk.Label(header, bg=yellow, width=10)
    lbl_blank.grid(row = 0,
                  column=1
                  )
    
    _help = Image.open("icons/help.png")
    _help = _help.resize((46,46), Image.ANTIALIAS)
    help= ImageTk.PhotoImage(_help)
    lbl_help = tk.Label(header, image=help, bg=yellow)
    lbl_help.image = help #This is weird, but it needs to be done, otherwise python forgets about the image and displays a blank spot.
    lbl_help.grid(row=0,
                  column=2)
    
    _settings = Image.open("icons/settings.png")
    _settings = _settings.resize((46,46), Image.ANTIALIAS)
    settings= ImageTk.PhotoImage(_settings)
    lbl_settings = tk.Label(header, image=settings, bg=yellow)
    lbl_settings.image = settings
    lbl_settings.grid(row=0,
                  column=3)

    return header_place



def make_main_body(where):
    body_place = tk.Frame(where,
                  bg="white")
    body = tk.Frame(body_place, bg="white")
    body.pack(pady=5)

    #Adding buttons: to make them pretty, they have to be images.

    #BUTTON 1
    _btn1 = Image.open("icons/btn1.png")
    _btn1 = _btn1.resize((137,137), Image.ANTIALIAS)
    img_btn1= ImageTk.PhotoImage(_btn1)
    btn1 = tk.Button(body,
                      image=img_btn1,
                      border=0,
                      bg="white")
    btn1.image = img_btn1
    btn1.grid(row = 0,
              column = 0)
    
    #BUTTON 2
    _btn2 = Image.open("icons/btn2.png")
    _btn2 = _btn2.resize((137,137), Image.ANTIALIAS)
    img_btn2= ImageTk.PhotoImage(_btn2)
    btn2 = tk.Button(body,
                      image=img_btn2,
                      border=0,
                      bg="white")
    btn2.image = img_btn2
    btn2.grid(row = 0,
              column = 1)
    btn3 = tk.Button(body, bg=yellow, text="SEARCH BY PAREMETERS")
    btn3.grid(row = 1,
              column = 0)
    btn4 = tk.Button(body, bg=yellow, text="SEARCH BY PAREMETERS")
    btn4.grid(row = 1,
              column = 1)

    return body_place