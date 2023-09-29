# Akalwa Rebecca Shirievo N.
# SCT211-0538/2022
# SIMPLE CALCULATOR

def calculate():
    #take input from user
    char = input('''
                 Hello
                 Please type in the math operation you would like to complete:
                 + for addition
                 - for subtraction
                 * for mulitiplication
                 / for division
                 ''')
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    #check which operation is to be carried out
    if char == '+':
        print("{} + {} = ".format(num1, num2))
        print(num1 + num2)
    elif char == '-':
        print("{} - {} = ".format(num1, num2))
        print(num1 - num2)
    elif char == '*':
        print("{} * {} = ".format(num1, num2))
        print(num1 * num2)
    elif char == '/':
        print("{} / {} = ".format(num1, num2))
        print(num1 / num2)
    else:
        print("Invalid input. Try again")
        calculate()
    
    again()

#check if user wants another calculation
def again():
    choice = input("Do you wish to continue? (Y/N): ")

    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print("See you later.")
    else:
        print("Invalid input!")
        again()

calculate()