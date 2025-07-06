import random

rightNum = random.randint(0,100)

while True :
    try : 
        answer = int(input("Guess a number between 0 and 100 : "))

        if answer == rightNum :
            print("Congratulations! You guessed the number ")
            break

        elif answer > rightNum :
            print("Too High")

        elif answer < rightNum :
            print("Too Low")

    except ValueError :
        print("Invalid Input, Please enter a number")
        