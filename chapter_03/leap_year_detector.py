# Author: Daisy Hardwick
# Class: CIS-170
# Program: Leap Year Detector Python Program

year = input("Please select a year:\n")

if (year % 100 == 0) and (year % 400 == 0):
  print(f"{year} is a leap year.")
elif year % 4 == 0:
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")