#Accepting user input

monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

#Calculating monthly savings

monthly_savings = monthly_income - monthly_expenses

#Estimating projected annual savings

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Printing the results

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${int(projected_annual_savings)}.")
