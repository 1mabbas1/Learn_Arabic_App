#-------------------- Get Words ------------------------------------#
import pandas
import random

"""This script is a flash card app which shows the user a arabic word for 3 seconds,
The card then flips to show the english translation, the user then ticks if they got it right,
the wrong words are shown again."""

data = pandas.read_csv('data/wordstolearn.csv')
to_learn = data.to_dict(orient = 'records')
current = {}

#definte the functions 
def nextcard():
    canvas.itemconfig(card,image = front)
    global currentcard, timer
    window.after_cancel(timer)
    currentcard = random.choice(to_learn)
    arab = currentcard['Arabic']
    eng = currentcard['English']
    canvas.itemconfig(cardlang, text = 'Arabic', fill = 'black')
    canvas.itemconfig(cardword, text = f'{arab}', fill = 'black')
    timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(card,image = back)
    arab = currentcard['Arabic']
    eng = currentcard['English']
    canvas.itemconfig(cardlang, text = 'English', fill = 'white')
    canvas.itemconfig(cardword, text = f'{eng}',fill = 'white')

def newcard():
    to_learn.remove(currentcard)
    nextcard()
    data = pandas.DataFrame(to_learn)
    data.to_csv('./data/wordstolearn.csv')




# -------------------- UI Setup ------------------------------------#
BG = "#B1DDC6"
from tkinter import *

window = Tk()
window.title('Flash Cards')
canvas = Canvas(width = 800, height =600)

front = PhotoImage(file = './images/card_front.png')
back = PhotoImage(file = './images/card_back.png')
tick = PhotoImage(file = './images/right.png')
cross = PhotoImage(file = './images/wrong.png')
card = canvas.create_image(400,300,image = front,)
canvas.config(bg = BG, highlightthickness = 0)
window.config(padx = 30, pady=30, bg = BG, )
canvas.grid(row=0,column=0, columnspan=2)

timer = window.after(3000, func=flip)


#labels
cardlang = canvas.create_text(400,180, text=f'language', fill = 'black', font = ('Arial', 30,'italic'))
cardword = canvas.create_text(400,300, text = f'word', fill = 'black', font = ('Arial', 60,'bold'))

#buttons

no = Button(image = cross, command = nextcard)
no.grid(column = 0 ,row = 1)

yes = Button(image = tick, command = newcard)
yes.grid(column = 1 ,row = 1)

nextcard()



window.mainloop()