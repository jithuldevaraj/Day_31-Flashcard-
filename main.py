import random
import tkinter
import pandas
from click import command

#------------------------------Constants and variables---------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn_dict_list = []

#------------------------------------Read Data-----------------------------------------#
try:
    words_data_df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_words_data_df = pandas.read_csv("./data/french_words.csv")
    words_to_learn_dict_list = original_words_data_df.to_dict(orient="records")
else:
    words_to_learn_dict_list = words_data_df.to_dict(orient="records")


#------------------------------------Functions-----------------------------------------#
def is_known():
    # Remove the current dictionary from the list
    words_to_learn_dict_list.remove(current_card)


    # Save the updated list to a new CSV so progress isn't lost! (list -> DataFrame -> file.csv)
    to_learn_updated_DF = pandas.DataFrame(words_to_learn_dict_list)
    to_learn_updated_DF.to_csv("./data/words_to_learn.csv", index=False)

    next_card()

def next_card():
    global flip_timer, current_card

    current_card = random.choice(words_to_learn_dict_list)
    window.after_cancel(flip_timer)

    canvas.itemconfig(canvas_background, image=card_front_img)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():

    canvas.itemconfig(canvas_background, image=card_back_img)
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")


#------------------------------UI---------------------------------------#
window = tkinter.Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)
window.after(3000, func=flip_card)

canvas = tkinter.Canvas(window, width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

x_image = tkinter.PhotoImage(file="./images/wrong.png")
x_button = tkinter.Button(window, image=x_image, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

y_image = tkinter.PhotoImage(file="./images/right.png")
y_button = tkinter.Button(window, image=y_image, highlightthickness=0, command=is_known)
y_button.grid(row=1, column=1)
y_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
next_card()


window.mainloop()