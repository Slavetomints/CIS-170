# Author: Daisy Hardwick
# Class: CIS-170
# Program: Leap Year Detector Python Program

year = int(input("Please select a year:\n"))

if ((year % 100 == 0) and (year % 400 == 0)) or ((year % 4 == 0) and (year % 100 != 0)):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")