import random
import tkinter
import pandas
from click import command

#------------------------------Contents---------------------------------#
BACKGROUND_COLOR = "#B1DDC6"

#-----------------------------Read Data---------------------------------#
data_df = pandas.read_csv("./data/french_words.csv")
data_dict = data_df.to_dict(orient="records")

def next_card():
    current_card = random.choice(data_dict)
    print(current_card)

    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_title, text="French")

#------------------------------UI---------------------------------------#
window = tkinter.Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tkinter.Canvas(window, width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

x_image = tkinter.PhotoImage(file="./images/wrong.png")
x_button = tkinter.Button(window, image=x_image, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

y_image = tkinter.PhotoImage(file="./images/right.png")
y_button = tkinter.Button(window, image=y_image, highlightthickness=0, command=next_card)
y_button.grid(row=1, column=1)
y_button.grid(row=1, column=1)

next_card()

window.mainloop()