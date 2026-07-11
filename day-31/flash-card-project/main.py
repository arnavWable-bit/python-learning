from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
cards = {}

def next_card():
    global flip_timer, current_card
    if flip_timer is not None:   
        window.after_cancel(flip_timer)
    current_card = random.choice(cards)
    french_current_card = current_card['French']
    canvas.itemconfig(card_word, text= french_current_card,fill='black')
    canvas.itemconfig(card_title, text= 'French',fill='black')
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000,flip_card)

def flip_card():
    english_current_card = current_card['English']
    canvas.itemconfig(card_image, image= card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=english_current_card, fill='white')
    
def known_card():
    cards.remove(current_card)
    updated_data = pd.DataFrame(cards)
    updated_data.to_csv("day-31/flash-card-project/data/words_to_learn.csv", index=False)
    next_card()
    

window = Tk()
window.title("Flashy")
# window.minsize(width=700, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR ,highlightthickness=0)
card_front_img = PhotoImage(file="day-31/flash-card-project/images/card_front.png")
card_back_img = PhotoImage(file="day-31/flash-card-project/images/card_back.png")
card_image = canvas.create_image(400,263, image= card_front_img)
card_title = canvas.create_text(400, 150, text="",fill='black' ,font=("Arial", 40, "italic"))
card_word =canvas.create_text(400, 263, text="",fill='black' ,font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

try:
    data = pd.read_csv("day-31/flash-card-project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("day-31/flash-card-project/data/french_words.csv")
    cards = original_data.to_dict(orient="records")
else:
    cards = data.to_dict(orient="records")


# BUTTONS
cross_image = PhotoImage(file="day-31/flash-card-project/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bd=0,borderwidth=0, relief="flat", command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="day-31/flash-card-project/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, bd=0,borderwidth=0, relief="flat", command=known_card )
known_button.grid(column=1, row=1)


next_card()

window.mainloop()