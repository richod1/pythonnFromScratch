import random

randomNumber=random.randrange(1,10)
guess_number=int(input("Enter any number! :"))
while randomNumber !=guess_number:
    if guess_number<randomNumber:
        print(f"{guess_number} is too low")
        guess_number=int(input("Enter another number :"))
    elif guess_number > randomNumber:
        print(f"{guess_number} is too high")
        guess_number=int(input("Guess again :"))
    else:
        break
    print("You guessed right!")