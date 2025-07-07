import os
import random
import smtplib


def auto_email():
    name = input("Enter your name: ")
    email = input("Enter your email address")
    message = (f"Dear {name}, Welcome to Amiram1544")
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("Gmail_Sherkat", "App_Password_oon_gmail") # Login with sender's credentials
        #app password ye chizie ke bayad az khod gmail begiri ta betooni kareto rah bendazi

        s.sendmail('Gmail_Sherkat', email, message)
        s.quit() #Mohem
    except Exception as ex:
        print(f"Error {ex}")



if __name__ == "__main__":

    auto_email()


