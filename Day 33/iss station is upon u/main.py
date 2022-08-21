import requests
from datetime import datetime
import smtplib


# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# # response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
# time_now = datetime.now()

while True:

    MY_LAT = 51.507351  # Your latitude
    MY_LONG = -0.127758  # Your longitude

    My_gmail = "homydearbestie@gmail.com"
    My_password = "jbyzxbzpyxzxfnmo"

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    if abs(MY_LAT - iss_latitude)<=10 and abs(MY_LONG - iss_longitude)<=10 or True:
        print(abs(MY_LAT - iss_latitude))
        print(abs(MY_LONG - iss_longitude))
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(My_gmail, My_password)
            connection.sendmail(from_addr=My_gmail, to_addrs="geddadavenkatapradeep@gmail.com",
                                msg=f"Subject:ISS Station Is Upon U!\n\nHey Pradeep!\n\n\tYou are just below the International Space Station.\n\n"
                                    f"Longitude: {iss_longitude}\nLatitude: {iss_latitude}")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



