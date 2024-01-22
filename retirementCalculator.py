# Retirement Calculator

# Get user inputs
current_income = float(input("Enter your current annual income: "))
current_savings = float(input("Enter your current annual savings: "))
current_expenses = float(input("Enter your current annual expenses: "))
current_portfolio_value = float(input("Enter your current portfolio value: "))

# Calculate savings rate
current_savings_rate = current_savings / current_income * 100

# Calculate years until retirement
years_until_retirement = 0
while current_portfolio_value < (current_expenses * 12 / 0.04):
    current_portfolio_value += current_portfolio_value * 0.04 + current_savings * current_savings_rate / 100
    years_until_retirement += 1

# Calculate monthly expenses and savings
monthly_expenses = current_expenses / 12
monthly_savings = current_savings / 12

# Print outputs
print("You can retire in: {} Years".format(years_until_retirement + 1))
print("with a Savings rate of: {}%".format(current_savings_rate))
print("annual expenses: {}".format(current_expenses))
print("annual savings: {}".format(current_savings))
print("monthly Expenses: {}".format(round(monthly_expenses, 2)))
print("monthly Savings: {}".format(round(monthly_savings, 2)))