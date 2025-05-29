#This is a simple program calculator that performs basic arithmetic operations on 2 numbers using match-case syntax

#Accepting user inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation_type = input("Choose the operation (+, -, *, /):. ")

#Advanced control flow logic
match operation_type:
    case '+':
        print(f"The result is {num1 + num2}")
    case '-':
        print(f"The result is {num1 - num2}")
    case '*':
        print(f"The result is {num1 * num2}")
    case '/':
        if num1 or num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}")
    case _:
        print("Invalid number")
