user_income = int(input("Enter your monthly income: "))
user_finances = int(input("Enter your total monthly expenses: "))
monthly_savings = user_income - user_finances

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${int(projected_annual_savings)}.")
