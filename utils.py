import tkinter as tk
from tkinter import ttk
import PIL
from PIL import ImageTk, Image

from search import *

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
    
    #WORD OF THE DAY
    #It is an image for now.
    _wotd = Image.open("icons/word_of_the_day.png")
    img_wotd= ImageTk.PhotoImage(_wotd)
    wotd = tk.Label(body_place, image=img_wotd)
    wotd.image = img_wotd
    wotd.pack(pady=20)


    body = tk.Frame(body_place, bg="white")
    body.pack(pady=5)

    #Adding buttons: to make them pretty, they have to be images.

    #BUTTON 1
    _btn1 = Image.open("icons/btn1.png")
    _btn1 = _btn1.resize((137,137), Image.ANTIALIAS)
    img_btn1= ImageTk.PhotoImage(_btn1)
    btn1 = tk.Button(body,
                     command=lambda: [body_place.destroy(), make_search_by_parameters(where=where)], # go to search by parameters
                      image=img_btn1,
                      border=0,
                      bg="white")
    btn1.image = img_btn1
    btn1.grid(row = 0,
              column = 0,
              padx=20,
              pady=20)
    
    #BUTTON 2
    _btn2 = Image.open("icons/btn2.png")
    _btn2 = _btn2.resize((137,137), Image.ANTIALIAS)
    img_btn2= ImageTk.PhotoImage(_btn2)
    btn2 = tk.Button(body,
                     command=lambda: [body_place.destroy(), make_search_by_word(where=where)], # go to search by parameters
                      image=img_btn2,
                      border=0,
                      bg="white")
    btn2.image = img_btn2
    btn2.grid(row = 0,
              column = 1,
              padx=20,
              pady=20)
    
    #BUTTON 3
    _btn3 = Image.open("icons/btn3.png")
    _btn3 = _btn3.resize((137,137), Image.ANTIALIAS)
    img_btn3= ImageTk.PhotoImage(_btn3)
    btn3 = tk.Button(body,
                      image=img_btn3,
                      border=0,
                      bg="white")
    btn3.image = img_btn3
    btn3.grid(row = 1,
              column = 0,
              padx=20,
              pady=20)
    
    #BUTTON 4
    _btn4 = Image.open("icons/btn4.png")
    _btn4 = _btn4.resize((137,137), Image.ANTIALIAS)
    img_btn4= ImageTk.PhotoImage(_btn4)
    btn4 = tk.Button(body,
                      image=img_btn4,
                      border=0,
                      bg="white")
    btn4.image = img_btn4
    btn4.grid(row = 1,
              column = 1,
              padx=20,
              pady=20)
    
    #grandpa picture as it is in figma
    _grandpa = Image.open("icons/grandpa.png")
    img_grandpa= ImageTk.PhotoImage(_grandpa)
    grandpa = tk.Label(body_place, image=img_grandpa)
    grandpa.image = img_grandpa
    grandpa.pack()

    return body_place




def make_search_by_word(where):

    s_word = tk.StringVar()
    body_place = tk.Frame(where, bg = 'white')
    body_place.pack(fill='x')
    body = tk.Frame(body_place, bg="white")
    body.pack(pady=5)

    entry = tk.Entry(body,
                     bg=yellow,
                     fg='black',
                     textvariable=s_word)
    entry.pack()

    _search = Image.open("icons/search.png")
    img_search= ImageTk.PhotoImage(_search)
    search = tk.Button(body,
                       command= lambda: [body_place.destroy(), results_search_by_word(where, s_word.get())],
                       #TODO Display an error message if there is no such word in the dataset.
                       image=img_search,
                       border=0,
                       bg="white",
                       padx=20,
                       pady=20)
    search.image = img_search
    search.pack()

def check_word_input(what_to_destroy, where, box_input):
    box_input = str.lower(box_input)
    if is_in_dataset(box_input):
        what_to_destroy.destroy()
        results_search_by_word(where=where, word=box_input)
    else:

        lbl_error = tk.Label(where,
                         text="Sorry, looks like this word is not in our dictionary.")
        lbl_error.pack()



    

def results_search_by_word(where, word):
    body_place = tk.Frame(where, bg = 'white')
    body_place.pack(fill='x')

    #Here is the WORD and SAVE button
    body1 = tk.Frame(body_place, bg="white")
    body1.pack(pady=5)


    #Here is the definition of the word and
    print(word)


def make_search_by_parameters(where):
    return 0

