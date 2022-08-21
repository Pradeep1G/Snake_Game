







from tkinter import *
import requests

root = Tk()
root.config(padx=50, pady=50)
root.title("Kanye Say's")

global text_init

def print_quote(sent):
    global text_init
    if len(sent) > 110:
        text_init = canvas.create_text(150, 150, fill="black", width="250", text=sent, font=("Areial", 16, 'bold'))
    elif len(sent) > 70:
        text_init = canvas.create_text(150, 150, fill="black", width="250", text=sent, font=("Areial", 20, 'bold'))

    elif len(sent)>40:
        text_init = canvas.create_text(150,150, fill="black",width="250", text=sent, font=("Areial",25, 'bold'))
    elif len(sent)>20:
        text_init = canvas.create_text(150,150, fill="black",width="250", text=sent, font=("Areial",28, 'bold'))



def change_quote():
    global text_init
    canvas.itemconfigure(text_init, text="")
    create_quote()


def create_quote():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    print_quote(data['quote'])


canvas = Canvas(height= 414, width=300)
background_img = PhotoImage(file="background.png")
canvas.create_image(152,207,image = background_img)
create_quote()

btn_image = PhotoImage(file="kanye.png")
btn = Button(image=btn_image, command=change_quote)

canvas.grid(row=0, column=0)
btn.grid(row=1, column =0)



root.mainloop()