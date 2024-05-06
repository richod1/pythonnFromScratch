# sending automated email with python

import os
import smtplib
import random


def automate_email():
    user=input("Enter your name >>:")
    email=input("Enter your email >>:")
    message_template=(f"Dear {user} you are welcome to auto email sender")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("user email",'user pass')
    s.sendmail("&&&&&&&&&&",email,message_template)
    print("Email sent!")


automate_email()