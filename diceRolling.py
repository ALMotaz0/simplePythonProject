import random

counter = 0
while True :

    try:
        numDices = int(input("How many dices do you want to play with? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    answer = input("Roll the dice/s? (y/n): ").lower()

    if answer == "y" :
        result = []
        for _ in range(numDices) :
            result.append(str(random.randint(1,6)))
        output = "("+",".join(result)+")"
        counter += numDices
        print(output)

    elif answer == "n" :
        print("Thanks for playing <3")
        break

    else :
        print("Invalid input.")

print("Number of dice rolled : " + str(counter))