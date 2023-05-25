import tkinter as tk
from tkinter import ttk
import PIL
from PIL import ImageTk, Image
from datetime import datetime
from datetime import date 

from search import *


#Global stuff
Font_header = ("Alata", 32)
Font_body = ("Alata", 20)
yellow = '#F9E21B'

def logaction(logtext):
    # Appends a line with logtext to the logfile, adds how long running
    # the experiment it is in minutes and seconds.
    ct = datetime.timestamp(datetime.now()) - starttime

    # Determine minutes and seconds, another divmod could be used to also
    # include hours
    m, s = divmod(int(ct), 60)

    # String formating is used to nicely display the timestamps
    timestr = f'{m:02d}:{s:02d}'
    logfile.write(timestr + ' ' + logtext + '\n')

# Getting the current date and time for the logging of user interction
startdatetime = datetime.now()
# Convert start date to seconds so we can use it for calculations.
starttime = datetime.timestamp(startdatetime)

# Opening the logfile and append to it to indicate a new session.
logfile = open('logging.txt', 'a')
logaction('New session started @' + str(startdatetime))


def return_home(what):
    logaction('user returned home')
    for child in what.winfo_children():
      child.destroy()

    header = make_header(what)
    header.pack(fill='x')
    _body = tk.Frame(what)
    _body.pack(fill='x')
    body = make_main_body(_body)
    body.pack(fill='x')

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

    _home = Image.open("icons/home.png")
    _home = _home.resize((46,46), Image.ANTIALIAS)
    img_home= ImageTk.PhotoImage(_home)
    btn_home = tk.Button(header,
                         image=img_home,
                         bg=yellow,
                         border=0,
                         command=lambda: return_home(root))
    btn_home.image = img_home
    btn_home.grid(row=0, column=0)




    lbl_name = tk.Label(header, text="BOOMER", font=Font_header, bg=yellow)
    lbl_name.grid(row = 0,
                  column=1,
                  )
    
    lbl_blank = tk.Label(header, bg=yellow, width=2)
    lbl_blank.grid(row = 0,
                  column=2
                  )
    
    _help = Image.open("icons/help.png")
    _help = _help.resize((46,46), Image.ANTIALIAS)
    help= ImageTk.PhotoImage(_help)
    lbl_help = tk.Label(header, image=help, bg=yellow)
    lbl_help.image = help #This is weird, but it needs to be done, otherwise python forgets about the image and displays a blank spot.
    lbl_help.grid(row=0,
                  column=3)
    
    _settings = Image.open("icons/settings.png")
    _settings = _settings.resize((46,46), Image.ANTIALIAS)
    settings= ImageTk.PhotoImage(_settings)
    lbl_settings = tk.Label(header, image=settings, bg=yellow)
    lbl_settings.image = settings
    lbl_settings.grid(row=0,
                  column=4)

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
                     command=lambda: [body_place.destroy(), make_search_by_parameters(where=where), logaction('clicked on search by age')], # go to search by parameters
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
                     command=lambda: [body_place.destroy(), make_search_by_word(where=where), logaction('clicked on search by word')], # go to search by parameters
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
                     command=lambda: [body_place.destroy(), make_saved_words(where=where), logaction('clicked on saved words')], # go to saved words
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
                     command=lambda: [body_place.destroy(), make_saved_words(where=where), logaction('clicked on dictionary')],
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
    entry.pack(pady=10)

    _search = Image.open("icons/search.png")
    img_search= ImageTk.PhotoImage(_search)
    #it was command= lambda: [body_place.destroy(), results_search_by_word(where, s_word.get())] if is_in_dataset(s_word.get().lower()) == True else input_error(body)
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

def input_error(where):
    lbl_error = tk.Label(where,
                         text="Sorry, looks like this word is not in our dictionary.")
    lbl_error.pack()



    

def results_search_by_word(where, s_word: str):
    logaction('search results were generated for searching by word')
    s_word = s_word.lower()
    word_info = search_by_word(s_word)

    # A general place where it is and which can be destroyed
    body_place = tk.Frame(where, bg = 'white')
    body_place.pack(fill='x')

    #Here is the WORD and SAVE button
    body1 = tk.Frame(body_place, bg="white")
    body1.pack(pady=5)


    btn_word = tk.Button(body1,
                         command= lambda: [body_place.destroy(), make_search_by_word(where)],
                         text=s_word,
                         bg=yellow)
    btn_word.grid(row = 0,
              column = 0,
              padx=20,
              pady=20)

    _save = Image.open("icons/save.png")
    img_save= ImageTk.PhotoImage(_save)
    
    btn_save = tk.Button(body1,
                         command=lambda: [add_saved_word(s_word), logaction('user saved a word')],
                      image=img_save,
                      border=0,
                      bg="white")
    btn_save.image = img_save
    btn_save.grid(row = 0,
              column = 1,
              padx=20,
              pady=20)
    

    #Here is the definition of the word and the rest of this stuff
    body2 = tk.Frame(body_place, bg="white")
    body2.pack(pady=5)

    lbl_definition = tk.Label(body2,
                              text='Definition: \n' + str(word_info[0]),
                              fg='black',
                              bg=yellow)
    lbl_definition.pack(fill='none',
                        pady=10)

    lbl_related_words = tk.Label(body2,
                              #text=str('Related words: \n' + ', '.join(x for x in word_info[1])),
                              text=str('Related words: \n' + ', '.join(x for x in word_info[1])),
                              fg='black',
                              bg=yellow)
    lbl_related_words.pack(fill='x',
                           pady=10)

    lbl_subculture = tk.Label(body2,
                              text=str('Related subculture: \n'+ ', '.join(x for x in word_info[2])),
                              fg='black',
                              bg=yellow)
    lbl_subculture.pack(fill='x',
                           pady=10)
    
    lbl_ages = tk.Label(body2,
                              text='Age of people who use that word: \n'+ ', '.join(str(x) for x in word_info[3]),
                              fg='black',
                              bg=yellow)
    
    lbl_ages.pack(fill='x',
                  pady=10)
    
    lbl_category = tk.Label(body2,
                              text='Category: \n'+ word_info[4],
                              fg='black',
                              bg=yellow)
    
    lbl_category.pack(fill='x',
                  pady=10)



def make_search_by_parameters(where):
    s_start_age = tk.StringVar()
    s_end_age = tk.StringVar()

    body_place = tk.Frame(where, bg = 'white')
    body_place.pack(fill='x')
    body1 = tk.Frame(body_place, bg="white")
    body1.pack(pady=5)


    _age = Image.open("icons/age_range.png")
    img_age= ImageTk.PhotoImage(_age)
    
    lbl_age = tk.Label(body1,
                      image=img_age,
                      border=0,
                      bg="white")
    lbl_age.image = img_age
    lbl_age.pack()

    body2 = tk.Frame(body_place, bg='white')
    body2.pack()

    lbl_from = tk.Label(body2,
                        text="from")
    lbl_from.grid(row=0,
                  column=0)
    
    entr_start_age = tk.Entry(body2,
                              textvariable=s_start_age)
    entr_start_age.grid(row=0,
                        column=1)
    
    lbl_years1= tk.Label(body2,
                        text="years")
    lbl_years1.grid(row=0,
                  column=2)
    
    lbl_to = tk.Label(body2,
                        text="to")
    lbl_to.grid(row=1,
                  column=0)
    
    entr_start_age = tk.Entry(body2,
                              textvariable=s_end_age)
    entr_start_age.grid(row=1,
                        column=1)
    
    lbl_years2= tk.Label(body2,
                        text="years")
    lbl_years2.grid(row=1,
                  column=2)
    
    body3 = tk.Frame(body_place)
    body3.pack()

    _search = Image.open("icons/search.png")
    img_search= ImageTk.PhotoImage(_search)
    search = tk.Button(body3,
                       command= lambda: [body_place.destroy(), results_search_by_age(where, s_start_age.get(), s_end_age.get())],
                       #TODO Display an error message if there is no such word in the dataset.
                       image=img_search,
                       border=0,
                       bg="white",
                       padx=20,
                       pady=20)
    search.image = img_search
    search.pack()



def results_search_by_age(where, start_age, end_age):
    logaction('search results were generated for search by age')
    int_start_age = int(start_age)
    int_end_age = int(end_age)

    #sorting fitting words
    fitting_words = search_by_age(start_age=int_start_age, end_age=int_end_age)
    displayed_words = []
    displayed_topics = []
    displayed_activities = []
    displayed_personalities = []
    for x in fitting_words:
        if x[5] == "word":
            displayed_words.append(x[0])
        elif x[5] == "topic":
            displayed_topics.append(x[0])
        elif x[5] == "activity":
            displayed_activities.append(x[0])
        elif x[5] == "person":
            displayed_personalities.append(x[0])

    body_place = tk.Frame(where, bg = 'white')
    body_place.pack(fill='x')
    body1 = tk.Frame(body_place, bg="white")
    body1.pack(pady=5)

    _age = Image.open("icons/age_search.png")
    img_age= ImageTk.PhotoImage(_age)
    
    btn_age = tk.Button(body1,
                        command= lambda: [body_place.destroy(), make_search_by_parameters(where)],
                      image=img_age,
                      border=0,
                      bg="white")
    btn_age.image = img_age
    btn_age.pack(pady=10)

    #popular words
    #header
    _pop_words = Image.open("icons/popular_words.png")
    img_pop_words= ImageTk.PhotoImage(_pop_words)
    
    h_pop_words = tk.Label(body1,
                      image=img_pop_words,
                      border=0,
                      bg="white")
    h_pop_words.image = img_pop_words
    h_pop_words.pack(pady=5)

    #label
    lbl_words = tk.Label(body1,
                         text= ', '.join(x for x in displayed_words))
    lbl_words.pack()

    #popular topics
    #header
    _topics = Image.open("icons/topics.png")
    img_topics= ImageTk.PhotoImage(_topics)
    
    h_topics = tk.Label(body1,
                      image=img_topics,
                      border=0,
                      bg="white")
    h_topics.image = img_topics
    h_topics.pack(pady=5)
    #label
    lbl_topics = tk.Label(body1,
                         text= ', '.join(x for x in displayed_topics))
    lbl_topics.pack()

    #popular activities
    #header
    _activities = Image.open("icons/activities.png")
    img_activities= ImageTk.PhotoImage(_activities)
    
    h_activities = tk.Label(body1,
                      image=img_activities,
                      border=0,
                      bg="white")
    h_activities.image = img_activities
    h_activities.pack(pady=5)
    #label
    lbl_activities = tk.Label(body1,
                         text= ', '.join(x for x in displayed_activities))
    lbl_activities.pack()


    #popular personalities
    #header
    _people = Image.open("icons/people.png")
    img_people= ImageTk.PhotoImage(_people)
    
    h_people = tk.Label(body1,
                      image=img_people,
                      border=0,
                      bg="white")
    h_people.image = img_people
    h_people.pack(pady=5)
    #label
    lbl_people = tk.Label(body1,
                         text= ', '.join(x for x in displayed_personalities))
    lbl_people.pack()



def make_saved_words(where):
    body_place = tk.Frame(where, bg = 'white')
    body_place.pack(fill='x')
    body1 = tk.Frame(body_place, bg="white")
    body1.pack(pady=5)

    word_list = get_saved_words()

    for x in word_list:
        tk.Button(body1,
                  text=x,
                  command= lambda: [body_place.destroy(), results_search_by_word(where, x)]).pack(pady=5)
        

def make_dictionairy(where):
    body_place = tk.Frame(where, bg = 'white')
    body_place.pack(fill='x')
    body1 = tk.Frame(body_place, bg="white")
    body1.pack(pady=5)

    word_list = get_words().keys()

    for x in word_list:
        tk.Button(body1,
                  text=x,
                  command= lambda: [body_place.destroy(), results_search_by_word(where, x)]).pack(pady=5)