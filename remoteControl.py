buttonsName = {"1":"Button num 1","2":"Button num 2","3":"Button num 3","4":"Button num 4"}
buttonsNum = ["1","2","3","4"]
holdState = {"1":False,"2":False,"3":False,"4":False}
output = {"1":"","2":"","3":"","4":""}

while True :
    command = input(">> ").lower()
        
    if command.startswith("hold") :
            btn = command.split("hold ")[1]
            holdState[btn] =  True      
            command = btn

    if command in buttonsNum :

        if holdState[command] :
            signal = input("Enter singal : ")
            output[command] = signal
            holdState[command] = False
        else :
            print(f"Output : {output[command]}")    

    elif command == "help" :
        print('''
Type the button number (1, 2, 3, 4) to get or set its signal.
Commands:
    hold X     - Set button X to hold mode (allow new signal input)
    help       - Show this help message
    exit       - Quit the program
        ''')

    elif command == "exit" :
        break

    else :
        print("Invalid Input")