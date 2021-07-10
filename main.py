import requests
import smtplib
from datetime import datetime
import time

EMAIL = "testting1232@gmail.com"
PASSWORD = "Test12345#$"
MY_LAT = 25.761681
MY_LONG = -80.191788

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

respons = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
respons.raise_for_status()
data = respons.json()
sunrise = data["results"]["sunrise"][:2]
sunset = data["results"]["sunset"][:2]

now = datetime.now()
time_now = datetime.strftime(now, "%I")

while True:
    time.sleep(60)
    if iss_latitude == MY_LAT and iss_longitude == MY_LONG and time_now == sunset:

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL, 
                to_addrs="israelsagesse@gmail.com", 
                msg="Subject:Look Up \n\n The ISS is above you in the sky.")
