# Author: Daisy Hardwick
# Class: CIS-170
# Assignment: Miles-Per-Gallon Python Program

# Declare variables and prompt user for values
miles_driven = int(input("How many miles have you driven?\n"))
gas_used = int(input("How many gallons of gas did you use?\n"))

# Calculate miles-per-gallon
miles_per_gallon = miles_driven / gas_used

# Display results
print(f"You drove {miles_per_gallon} miles per gallon of gas.")