

import datetime as dt
import pandas
import random
import smtplib

My_gmail = "homydearbestie@gmail.com"
My_password = "jbyzxbzpyxzxfnmo"

today = dt.datetime.today()
today = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
Names= data['name'].tolist()

birthdays = {}

for i,item in data.iterrows():
    birthdays[(item.month, item.day)] = [item.email, Names[i]]


if today in birthdays:
    letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    curr_letter = random.choice(letters)
    with open(curr_letter, mode='r') as letter:
        content = letter.read()
        content = content.replace('[NAME]', birthdays[today][1])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(My_gmail, My_password)
        connection.sendmail(from_addr=My_gmail, to_addrs=birthdays[today][0],
                            msg=f"Subject:Happy Birthday {birthdays[today][1]}\n\n{content}")








