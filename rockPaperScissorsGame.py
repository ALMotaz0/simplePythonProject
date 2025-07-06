import random

emojis = {"r":"🧱","p":"📄","s":"✂️"}
ListOfChoices = ["r","p","s"]


print(""" 
⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀
⠀⢀⣠⢋⡀⠔⠀⠉⠲⢤⢤⡀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⣸⠀⠀⠀⠀
⡞⠁⠈⠀⠀⠀⠀⢠⠤⠌⣇⢱⢸⠉⠉⢳⠀⠀⡠⠋⠀⠀⡔⡡⠔⠒⠲⡄
⡸⠒⠤⠀⠀⠀⠠⠴⢒⣂⢸⢸⠀⢧⠀⠀⡧⠊⠀⠀⢀⠞⠉⠀⠀⣀⠴⠃
⢧⡀⠀⠀⠀⠀⠀⠈⠉⢀⠞⠋⠀⠸⠀⠀⠀⠀⠀⠠⠃⠀⢀⣤⠮⠥⠤⢤
⠀⠙⢍⣁⣀⣀⣀⠤⠖⠁⠀⠀⠠⢇⢀⡴⠂⣠⠀⠀⠀⠠⠋⠀⢀⡠⠴⠚
⠀⠀⢀⡤⣄⡤⠴⠒⡲⠤⡀⠀⢰⡘⣌⠐⣊⠤⠀⠀⠀⢀⠴⠊⠁⠀⠀⠀
⠀⢠⢋⡞⣁⡀⠀⠀⠘⢤⣘⡄⠀⠑⢌⣳⠤⠤⠤⠴⠚⠁⠀⠀⠀⠀⠀⠀
⠀⡇⡜⢐⠦⣈⡀⠀⠀⠀⠀⠈⠉⠉⠉⠒⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⢣⠈⠓⠀⠁⠀⠀⠐⠂⠠⢤⡤⠤⢄⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠳⣄⠀⠀⠀⠀⣀⡀⠀⠀⠉⠲⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠒⠤⠔⠒⠉⠑⠢⢄⡀⢨⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠉⠉⠀⠀⠀⠀⠀       
""")

while True :
    userChoice = input("Rock, Paper, or Scissors? (r/p/s) : ").lower()
    robotChoice = random.choice(ListOfChoices)
    if userChoice in ListOfChoices:
        
        print(f"You Choose {emojis[userChoice]}" )
        print(f"Computer Choose {emojis[robotChoice]}" )
    else :
        print("Invalid Choice so")

    if (
            (robotChoice == "r" and userChoice == "p") or 
            (robotChoice == "s" and userChoice == "r") or 
            (robotChoice == "p" and userChoice == "s")) :
        print("You Won!")
    elif robotChoice == userChoice :
        print("Its a Tie")
    else :
        print("You Lost :(")

   
    while True : 
        answer = input("Continue? (y/n) : ").lower()
        if answer == "y" :
            break
        elif answer == "n" :
            print("Thanks for playing...")
            exit()
        else :
            print("I dont understand")





