    #Simple_Calculator

print("Select an oparation to preform : ")
print('''
1. For Add
2. For Subtract
3. For Multiply
4. For Divide
''')

try :
    oparation = int(input("> "))

        #Add
    if oparation == 1 :
        num1 = int(input("The First Number : "))
        num2 = int(input("The Second Number : "))
        sum = num1 + num2
        print(f"The sum is {sum} ")

        #Subtract
    elif oparation == 2 :
        num1 = int(input("The First Number : "))
        num2 = int(input("The Second Number : "))
        sum = num1 - num2
        print(f"The sum is {sum} ")
        
        #Multiply
    elif oparation == 3 :
        num1 = int(input("The First Number : "))
        num2 = int(input("The Second Number : "))
        sum = num1 * num2
        print(f"The sum is {sum} ")
        
        #Divide
    elif oparation == 4 :
        num1 = int(input("The First Number : "))
        num2 = int(input("The Second Number : "))
        sum = num1 / num2
        print(f"The sum is {sum} ")
        
    else :
        print("Invalid Entry")  

except ValueError :
    print("Invalid Entry")