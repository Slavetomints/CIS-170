# Author: Daisy Hardwick
# Class: CIS-170
# Program: Siblings Python Program 

def main():
  try:
    size = int(input("Enter number of siblings:"))

    if size == 0:
      print("Ah, you are an only child")
    else:
       siblings = [None] * size
       iterator = 0
       while iterator < size:
         print(f"\nEnter sibling {iterator + 1}")
         siblings[iterator] = input()
         iterator += 1
       
       print("\nYour siblings are:")
       for sibling in siblings:
         print(sibling)
  except:
    print("Invalid type detected. Exiting now!")

main()