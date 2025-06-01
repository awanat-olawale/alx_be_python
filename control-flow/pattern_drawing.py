#This program prints a square pattern with 4 rows and columns, using a while loop to iterate through the rows
# and a for loop to iterate through columns

user_number = int(input("Enter the size of the pattern: "))
pattern_row = 0
while pattern_row < user_number:
    for i in range(user_number):
        print("*", end=" ")
    print()
    pattern_row += 1
