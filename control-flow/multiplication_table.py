#This program prints the multiplication of a given number using pre-defined values

number = int(input("Enter a number to see its multiplication table: "))

#Looping through each range value and multiplying by number

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

