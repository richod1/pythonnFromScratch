import datetime

def ageCalculator(y,m,d):
    today=datetime.datetime.now().date()
    dob=datetime.date(y,m,d)
    age=int((today-dob).days/365.25)
    print(age)


ageCalculator(2000,8,23)