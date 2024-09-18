def main():
  display_intro()
  kilometer_to_mile_converter()

def display_intro():
  print("Welcome to the Kilometer to Miles Converter!\n")

def kilometer_to_mile_converter():
  # Declare constant
  KILOMETER_TO_MILE_CONVERSION_RATE = 0.6214

  # Gathering input from user
  kilometers = int(input("Please enter the amount in kilometer(s)\n"))
  
  # Calculating miles
  miles = kilometers * KILOMETER_TO_MILE_CONVERSION_RATE

  # Displaying output
  print(f"{kilometers} kilometer(s) is equal to {miles} mile(s).")

main()