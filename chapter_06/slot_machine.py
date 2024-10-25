# Author: Daisy Hardwick
# Class: CIS-170
# Program: Slot Machine Python Program

import random

def main():
  money = enter_amount_of_money()
  first_word = get_choice()
  second_word = get_choice()
  third_word = get_choice()
  check_winnings(money, first_word, second_word, third_word)


def enter_amount_of_money():
  money = input("Please enter the amount of money you wish to bet\n")
  if money == '' or float(money) < 0:
    print("Please enter an amount greater than or equal to zero.\n")
    money = enter_amount_of_money()
  money = int(float(money))
  return money

def get_choice():
  word = random.sample(["Cherries", "Oranges", "Plums", "Bells", "Melons", "Bars"], 1)
  print(word)
  return word

def check_winnings(money, first_word, second_word, third_word):
  if first_word == second_word and first_word == third_word:
    money = money * 3
    print(f"You won ${money}!")
  elif first_word == second_word or first_word == third_word or second_word == third_word:
     money = money * 2
     print(f"You won ${money}!")
  else:
    print("You loose!")
  play_again()

def play_again():
  answer = input("Do you want to play again? Please enter 'Y' or 'y' to do so.\n")
  if answer == 'Y' or answer == 'y':
    print("Have Fun!\n\n\n")
    main()
  else:
    print("Bye Bye!")

main()