# Author: Daisy Hardwick
# Class: CIS-170
# Assignment: Miles-Per-Gallon Python Program

# Gathering input for variables
miles_driven = int(input("How many miles have you driven?\n"))
gas_used = int(input("How many gallons of gas did you use?\n"))

#Performing gas mileage calculation
miles_per_gallon = miles_driven / gas_used

#Displaying gas mileage 
print(f"You drove {miles_per_gallon} miles per gallon of gas.")