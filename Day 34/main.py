


from tkinter import *
from create_question import Question
import time

root = Tk()



root.config(padx = 60, pady =40, bg="#2B4865")



global textt, score, answer, new_question, Question_no
textt=None
score = 0
Question_no =0


def display_question():

    # time.sleep(1)
    global textt, answer, new_question, Question_no

    Question_no += 1

    canvas.itemconfigure(textt, text="")

    question = Question()
    new_question = question.new_question()
    new_question = f"Q. {Question_no} : " + new_question
    # print(new_question)
    answer = question.answer()
    # print(len(new_question), answer)
    canvas.config(bg="white")
    # root.update()
    if len(new_question) > 130:
        textt = canvas.create_text(180, 130, fill="black", width=340, text = new_question, font=("Arieal", 18, "normal"))
    elif len(new_question) > 90:
        textt = canvas.create_text(180, 120, fill="black", width=340, text = new_question, font=("Arieal", 20, "normal"))
    elif len(new_question) > 60:
        textt = canvas.create_text(180, 120, fill="black", width=340, text = new_question, font=("Arieal", 24, "normal"))
    elif len(new_question) > 30:
        textt = canvas.create_text(180, 140, fill="black", width=340, text = new_question, font=("Arieal", 28, "normal"))
    else:
        textt = canvas.create_text(180, 150, fill="black", width=340, text = new_question, font=("Arieal", 30, "normal"))

def just_display():
    global texttt
    if len(new_question) > 130:
        texttt = canvas.create_text(180, 130, fill="black", width=340, text = new_question, font=("Arieal", 18, "normal"))
    elif len(new_question) > 90:
        texttt = canvas.create_text(180, 120, fill="black", width=340, text = new_question, font=("Arieal", 20, "normal"))
    elif len(new_question) > 60:
        texttt = canvas.create_text(180, 120, fill="black", width=340, text = new_question, font=("Arieal", 24, "normal"))
    elif len(new_question) > 30:
        texttt = canvas.create_text(180, 140, fill="black", width=340, text = new_question, font=("Arieal", 28, "normal"))
    else:
        texttt = canvas.create_text(180, 150, fill="black", width=340, text = new_question, font=("Arieal", 30, "normal"))


def correct_answer():
    global score, answer, textt
    if answer == "True":
        canvas.config(bg="green")
        just_display()
        root.update()
        canvas.itemconfigure(texttt, text="")
        root.update()
        score+=1
        score_board.config(text=f"Score : {score}")
        display_question()
    else:
        canvas.config(bg="red")
        just_display()
        root.update()
        canvas.itemconfigure(texttt, text="")
        root.update()
        display_question()


def wrong_answer():
    global score, answer, textt
    if answer == "False":
        canvas.config(bg="green")
        just_display()
        root.update()
        canvas.itemconfigure(texttt, text="")
        root.update()
        score+=1
        score_board.config(text=f"Score : {score}")
        display_question()
    else:
        canvas.config(bg="red")
        just_display()
        root.update()
        canvas.itemconfigure(texttt, text="")
        root.update()
        display_question()


canvas = Canvas(width=380, height=320)
textt = canvas.create_text(180, 130, fill="black", width=340, text="", font=("Arieal", 18, "normal"))
canvas.grid(row=1, column=0, columnspan=2, pady=30)

score_board = Label(text=f"Score : {score}", bg="#2B4865", fg="white", font=(20))
score_board.grid(row=0, column=1)

wrg_img = PhotoImage(file="images/false.png")
crt_img = PhotoImage(file="images/true.png")

wrg_btn = Button(image = wrg_img, padx=30, pady=30, highlightthickness=0, borderwidth = 0, command=wrong_answer)
crt_btn = Button(image = crt_img, padx=30, pady=30, highlightthickness=0, borderwidth = 0, command=correct_answer)

wrg_btn.grid(row=2, column=1)
crt_btn.grid(row=2, column=0)

display_question()


root.mainloop()

