

import pandas
# from numpy.core.setup_common import file

data = pandas.read_csv("french_words.csv")
# print(data)
# dictonary = {}
# for i,key in enumerate(data['French'].tolist()):
#     dictonary[key] = data['English'].tolist()[i]
# print(dictonary)
# size = len(dictonary)
# print(size)\

french = data['French'].tolist()
english = data['English'].tolist()

global answer_index
answer_index = None

global text1
text1 = None

global text2
text2 = None

global flip_timer
flip_timer = None



def answer_fun(answer):
    global text1
    global text2
    global flip_timer
    canvas1.itemconfigure(text1, text="")
    canvas1.itemconfigure(text2, text="")

    canvas1.itemconfigure(canvas_img, image=card_front_img)
    # canvas1.itemconfigure(canvas_img, image=card_front_img)

    text1 = canvas1.create_text(450, 200, fill="white", text="English", font=("Areial",40, "italic"))
    text2 = canvas1.create_text(450, 350, fill="white", text=f"{answer}", font=("Areial",60, "bold"))




def question_fun():
    global text1
    global text2
    global answer_index
    global flip_timer
    if text1 != None:
        canvas1.itemconfigure(text1, text="")
        canvas1.itemconfigure(text2, text="")

    question_word = random.choice(english)
    answer_index = english.index(question_word)
    answer_word = french[answer_index]
    canvas1.itemconfigure(canvas_img, image=card_back_img)
    text1 = canvas1.create_text(450, 200, fill="black", text="French", font=("Areial",40, "italic"))
    text2 = canvas1.create_text(450, 350, fill="black", text=f"{answer_word}", font=("Areial",60, "bold"))



    flip_timer = root.after(3000, answer_fun, question_word)
    # break
    # time.sleep(2)


def correct_choice():
    global answer_index
    global flip_timer
    root.after_cancel(flip_timer)
    french.pop(answer_index)
    english.pop(answer_index)
    question_fun()


def wrong_choice():
    question_fun()



from tkinter import *
import time
import random


root = Tk()
root.config(padx=50, pady=50, bg="#B1DDC6")

canvas1 = Canvas(width=840, height=550, bg="#B1DDC6", highlightthickness=0, borderwidth=15)


card_front_img = PhotoImage(file="images/card_back.png")
card_back_img = PhotoImage(file="images/card_front.png")

canvas_img = canvas1.create_image(440,300, image=card_back_img)
canvas1.grid(column=0,row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")




rgtbtn = Button( bg="#B1DDC6",image=right_img, highlightthickness=0, borderwidth=0, command = correct_choice)
wrgbtn = Button( bg="#B1DDC6",image=wrong_img, highlightthickness=0, borderwidth=0, command= wrong_choice)

rgtbtn.grid(column=0, row=1)
wrgbtn.grid(column=1, row=1)





question_fun()

root.mainloop()
