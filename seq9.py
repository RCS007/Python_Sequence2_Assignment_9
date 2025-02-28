# Problem 4: Compound Interest

# Pretend that you have just opened a new savings account that earns 4.5 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added to the
# balance of the savings account.
# Write a program that begins by reading the amount of money deposited into the account
# from the user. Then your program should compute and display the amount in the savings
# account after 1, 2, and 3 years.
# Display each amount so that it is rounded to 2 decimal places.

# Input the initial deposit amount
deposit = float(input("Enter the initial deposit amount: Rs "))

# Define the annual interest rate
interest_rate = 0.045  # 4.5% interest

# Calculate balance after each year
year1_balance = deposit * (1 + interest_rate)
year2_balance = year1_balance * (1 + interest_rate)
year3_balance = year2_balance * (1 + interest_rate)

# Display the results rounded to 2 decimal places
print(f"Balance after 1 year: Rs {year1_balance:.2f}")
print(f"Balance after 2 years: Rs {year2_balance:.2f}")
print(f"Balance after 3 years: Rs {year3_balance:.2f}")
