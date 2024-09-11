# Author: Daisy Hardwick
# Class: CIS-170
# Program: Factorial Calculator

# Declare variables and gather input
total = 1
max_value = int(input("Please select a number to get a factorial of: "))
current_value = 1

# Calculate factorial
while current_value <= max_value:
  total *= current_value
  current_value += 1

# Display results
print(f"{max_value}! is equal to {total}")