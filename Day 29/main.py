# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, 'end')
    char_li = [33, 35,36,37,38,40,41] + [x for x in range(63,95) if x!=92] + [x for x in range(96,126) if x!=124] + [x for x in range(47,58)]
    password = ""
    # pa = [chr(y) for y in random.choices(char_li, k=10)]
    # print(pa, " +++++ ")
    for i in range(10):
        password += chr(random.choice(char_li))
    print(password, len(password))
    password_entry.insert(0,password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    while len(web_entry.get()) == 0 or len(email_entry.get()) ==0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Warning", message="Please fill all the details")
        return
    with open("file1.txt", mode='a') as file1:
        file1.write(f"\n{web_entry.get()}  |   {email_entry.get()}   |   {password_entry.get()}")
    messagebox.showinfo(title="Password Manager", message="Your password has been saved.")
    password_entry.delete(0, 'end')
    web_entry.delete(0, 'end')
    email_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.config(padx = 20, pady = 20)

canvas = Canvas(width = 200, height = 200)
lock_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_image)
canvas.grid(column = 1, row = 0)

web_label = Label(text="Website")
web_label.grid(column = 0, row = 1)

web_entry = Entry(width = 40)
web_entry.grid(column = 1, row = 1, columnspan = 2)
web_entry.focus()


email_label = Label(text="Email/Username")
email_label.grid(column = 0, row = 2)

email_entry = Entry(width = 40)
email_entry.grid(column = 1, row = 2, columnspan = 2)

password_label = Label(text = "Password")
password_label.grid(column = 0, row = 3)

password_entry = Entry(text="hjdfgshkj", width = 21)
password_entry.grid(column = 1, row = 3)

password_genr_btn = Button(text = "Generate Password", command=generate_password)
password_genr_btn.grid(column = 2, row = 3, padx=0)

add_btn = Button(text = "Add", width = 34, command=save_data)
add_btn.grid(column = 1, row = 4, columnspan = 2)

print(ord("'"))






root.mainloop()

