from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
from random import choice
count = 0
flip_timer = 0
to_learn = {}
current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
    print(to_learn)
else:
     to_learn = data.to_dict(orient="records")

###-----------------------Read Data & Display on GUI --------------------------------###

#print(to_learn)
def next_card():
    global flip_timer,to_learn,current_card
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(text_title, text="French", fill="black")
    canvas.itemconfig(text_cardword, text= current_card["French"], fill="black")
    canvas.itemconfig(bg_img, image=card_front)
    flip_timer = window.after(3000, flip_card, current_card)

    # print(f"{current_card["French"]} : {current_card["English"]}" )




###-----------------------Flip Card & Timer -----------------------------------------###
def flip_card(current_card):
        canvas.itemconfig(bg_img, image=card_back)
        canvas.itemconfig(text_title, text="English", fill="white")
        canvas.itemconfig(text_cardword, text= current_card["English"], fill= 'white')
        window.after_cancel(current_card)




##-----------------------------------Tick OK button clicked ------------------------------##

def is_ok():
     to_learn.remove(current_card)
     print(len(to_learn))
     data = pd.DataFrame(to_learn)
     data.to_csv("data/words_to_learn.csv",index=False)
     next_card()




###-------------------------------------GUI Set Up __________________________________###
window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
bg_img = canvas.create_image(400,226,image= card_front)
text_title =canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
text_cardword = canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_ok)
right_button.grid(column=0, row=1)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1)
flip_timer = window.after(3000,next_card)
next_card()
window.mainloop()


