
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfigure(timer_text, text = "00:00")
    label.config(text="Timer")
    label2.config(text="")
    return False

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    canvas.itemconfigure(timer_text, text = "25:00")
    label.config(text="Work")
    workcountdown(1)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
global sec
sec = 59

global breaks
breaks = 4

global timer
timer = None


def workcountdown(min,se=sec):
    global breaks
    global timer
    if breaks>0:
        if min>=0:
            if se>=0:
                canvas.itemconfigure(timer_text, text=f"{num.two_digit(min)}:{num.two_digit(se)}")
                timer = root.after(50, workcountdown, min,se-1)
            else:
                se = 0
                canvas.itemconfigure(timer_text, text=f"{num.two_digit(min)}:{num.two_digit(se)}")
                se = 59
                timer = root.after(10, workcountdown, min-1, se)
        else:
            breaks -= 1
            if breaks == 0:
                label.config(text= "Long Break", fg=RED)
                breakcountdown(2)
            else:
                label.config(text= "Break", fg=PINK)
                breakcountdown(0)

def breakcountdown(min, se=sec):
    global breaks
    global timer
    if min >= 0:
        if se >= 0:
            canvas.itemconfigure(timer_text, text=f"{num.two_digit(min)}:{num.two_digit(se)}")
            timer = root.after(50, breakcountdown, min, se - 1)
        else:
            se = 0
            canvas.itemconfigure(timer_text, text=f"{num.two_digit(min)}:{num.two_digit(se)}")
            se = 59
            timer = root.after(10, breakcountdown, min - 1, se)
    else:
        if breaks == 0:
            reset_timer()
            return
        label2.config(text="✔" * (4 - breaks))
        label.config(text="Work", fg=GREEN)
        workcountdown(1)



from tkinter import *
import time
from number import Number

num = Number()

root = Tk()
root.config(padx=100,pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45,"bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)



label2 = Label(text="", fg=GREEN, bg=YELLOW, font=(20))
label2.grid(column=1, row=3)


start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)


reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)



root.mainloop()
