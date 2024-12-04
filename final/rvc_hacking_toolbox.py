import os
import re
import time
# Only used to clear the terminal every time display_header() is called. It is only used on line 9 as "os.system("clear")"

def main():
  display_main_menu()

def display_header():
  os.system("clear")
  print(r"""
 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \
\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
 \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
 / /\  ,-.----.                ,----..                                               / /\ 
/ /\ \ \    /  \        ,---. /   /   \                                             / /\ \
\ \/ / ;   :    \      /__./||   :     :                                            \ \/ /
 \/ /  |   | .\ : ,---.;  ; |.   |  ;. /                                             \/ / 
 / /\  .   : |: |/___/ \  | |.   ; /--`                                              / /\ 
/ /\ \ |   |  \ :\   ;  \ ' |;   | ;                                                / /\ \
\ \/ / |   : .  / \   \  \: ||   : |                                                \ \/ /
 \/ /  ;   | |  \  ;   \  ' ..   | '___                                              \/ / 
 / /\  |   | ;\  \  \   \   ''   ; : .'|                                             / /\ 
/ /\ \ :   ' | \.'   \   `  ;'   | '/  :                                            / /\ \
\ \/ / :   : :-'      :   \ ||   :    /                                             \ \/ /
 \/ /  |   |.' ,--,    '---"  \   \ .'                                               \/ / 
 / /\  `---' ,--.'|            `---`          ,-.                                    / /\ 
/ /\ \    ,--,  | :                       ,--/ /|   ,--,                            / /\ \
\ \/ / ,---.'|  : '                     ,--. :/ | ,--.'|         ,---,              \ \/ /
 \/ /  |   | : _' |                     :  : ' /  |  |,      ,-+-. /  |  ,----._,.   \/ / 
 / /\  :   : |.'  |  ,--.--.     ,---.  |  '  /   `--'_     ,--.'|'   | /   /  ' /   / /\ 
/ /\ \ |   ' '  ; : /       \   /     \ '  |  :   ,' ,'|   |   |  ,"' ||   :     |  / /\ \
\ \/ / '   |  .'. |.--.  .-. | /    / ' |  |   \  '  | |   |   | /  | ||   | .\  .  \ \/ /
 \/ /  |   | :  | ' \__\/: . ..    ' /  '  : |. \ |  | :   |   | |  | |.   ; ';  |   \/ / 
 / /\  '   : |  : ; ," .--.; |'   ; :__ |  | ' \ \'  : |__ |   | |  |/ '   .   . |   / /\ 
/ /\ \ |   | '  ,/ /  /  ,.  |'   | '.'|'  : |--' |  | '.'||   | |--'   `---`-'| |  / /\ \
\ \/ / ;   : ;--' ;  :   .'   \   :    :;  |,'    ;  :    ;|   |/       .'__/\_: |  \ \/ /
 \/ /  |   ,/     |  ,     .-./\   \  / '--'      |  ,   / '---'        |   :    :   \/ / 
 / /\  '---'       `--`---'     `----'             ---`-'                \   \  /    / /\ 
/ /\ \         ,----,                                                     `--`-'    / /\ \
\ \/ /       ,/   .`|                                                               \ \/ /
 \/ /      ,`   .'  :                    ,--,                                        \/ / 
 / /\    ;    ;     /                  ,--.'|     ,---,                              / /\ 
/ /\ \ .'___,/    ,'  ,---.     ,---.  |  | :   ,---.'|      ,---.                  / /\ \
\ \/ / |    :     |  '   ,'\   '   ,'\ :  : '   |   | :     '   ,'\ ,--,  ,--,      \ \/ /
 \/ /  ;    |.';  ; /   /   | /   /   ||  ' |   :   : :    /   /   ||'. \/ .`|       \/ / 
 / /\  `----'  |  |.   ; ,. :.   ; ,. :'  | |   :     |,-..   ; ,. :'  \/  / ;       / /\ 
/ /\ \     '   :  ;'   | |: :'   | |: :|  | :   |   : '  |'   | |: : \  \.' /       / /\ \
\ \/ /     |   |  ''   | .; :'   | .; :'  : |__ |   |  / :'   | .; :  \  ;  ;       \ \/ /
 \/ /      '   :  ||   :    ||   :    ||  | '.'|'   : |: ||   :    | / \  \  \       \/ / 
 / /\      ;   |.'  \   \  /  \   \  / ;  :    ;|   | '/ : \   \  /./__;   ;  \      / /\ 
/ /\ \     '---'     `----'    `----'  |  ,   / |   :    |  `----' |   :/\  \ ;     / /\ \
\ \/ /                                  ---`-'  /    \  /          `---'  `--`      \ \/ /
 \/ /                                           `-'----'                             \/ / 
 / /\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'                          
  """)

def display_main_menu():
  display_header()
  print("Please select your mode")
  print("======================================== Main Menu =======================================")
  print("1 - Cryptography")
  print("2 - Password Cracking")
  print("99 - Quit")
  get_main_choice(input())

def get_main_choice(choice):
  match choice:
    case "1":
      display_cryptography_menu()
      get_cryptography_choice()
    case "2":
      display_password_cracking_menu()
      get_password_cracking_choice()
    case "99":
      raise KeyboardInterrupt
    case _:
      print("Please make a valid choice!")
      display_main_menu()

def display_cryptography_menu():
  display_header()
  print("Please select your mode")
  print("=================================== Cryptography Menu ====================================")
  print("1 - Encode ROT13")
  print("2 - Decode ROT13")
  print("3 - Go to Main Menu")
  print("99 - Quit")
  get_cryptography_choice(input())


def get_cryptography_choice(choice):
  match choice:
    case "1":
      encode_rot13()
      display_cryptography_menu()
    case "2":
      decode_rot13()
      display_cryptography_menu()
    case "3":
      display_main_menu()
    case "99":
      raise KeyboardInterrupt
    case _:  
      print("Please make a valid choice!")
      display_cryptography_menu()

def encode_rot13():
  display_header()
  string = input("Please enter a string you wish to encode\n")
  cipher_text = ""
  for letter in string:
    if re.match("[a-zA-Z]", letter):
      if letter.upper() == letter:
        if ord(letter) + 13 > 90:
          cipher_char = ord(letter) - 13
          cipher_text = cipher_text + chr(cipher_char)
        else:
          cipher_char = ord(letter) + 13
          cipher_text = cipher_text + chr(cipher_char)
      elif letter.lower() == letter:
        if ord(letter) + 13 > 122:
          cipher_char = ord(letter) - 13
          cipher_text = cipher_text + chr(cipher_char)
        else:
          cipher_char = ord(letter) + 13
          cipher_text = cipher_text + chr(cipher_char)
    else:
      cipher_text = cipher_text + letter
  print(f"Your encoded message is {cipher_text}")
  input("Press Enter to continue...")

def decode_rot13():
  display_header()
  string = input("Please enter a string you wish to decode\n")
  cipher_text = ""
  for letter in string:
    if re.match("[a-zA-Z]", letter):
      if letter.upper() == letter:
        if ord(letter) + 13 > 90:
          cipher_char = ord(letter) - 13
          cipher_text = cipher_text + chr(cipher_char)
        else:
          cipher_char = ord(letter) + 13
          cipher_text = cipher_text + chr(cipher_char)
      elif letter.lower() == letter:
        if ord(letter) + 13 > 122:
          cipher_char = ord(letter) - 13
          cipher_text = cipher_text + chr(cipher_char)
        else:
          cipher_char = ord(letter) + 13
          cipher_text = cipher_text + chr(cipher_char)
    else:
      cipher_text = cipher_text + letter
  print(f"Your decoded message is {cipher_text}")
  input("Press Enter to continue...")


def display_password_cracking_menu():
  display_header()
  print("================================= Password Cracking Menu =================================")
  print("1 - Generate Wordlist")
  print("2 - Go to Main Menu")
  print("99 - Quit")
  get_password_cracking_choice(input())

def get_password_cracking_choice(choice):
  match choice:
    case "1":
      generate_wordlist()
      display_password_cracking_menu()
    case "2":
      display_main_menu()
    case "99":
      raise KeyboardInterrupt

def generate_wordlist():
  display_header()
  filename = input("Enter a filename to save to: ")
  prefix = input("Enter a prefix for the password: ")
  file = open(filename, "w")
  i = 0
  while i < 10000:
    appended_number = str(i).zfill(4)
    file.write(f"{prefix}{appended_number}\n")
    i = i + 1
  print(f"Passwords written to {filename} in current directory.")
  input("Press Enter to continue...")

def quit():
  os.system("clear")
  print(r"""
/==================================================================================================\
||      # ###                             ##      /                              ###      ###     ||
||    /  /###  /                           ##   #/                                ###      ###    ||
||   /  /  ###/                            ##   ##                                 ##       ##    ||
||  /  ##   ##                             ##   ##                                 ##       ##    ||
|| /  ###                                  ##   ##                                 ##       ##    ||
||##   ##            /###     /###     ### ##   ## /###   ##   ####      /##       ##       ##    ||
||##   ##   ###     / ###  / / ###  / ######### ##/ ###  / ##    ###  / / ###      ##       ##    ||
||##   ##  /###  / /   ###/ /   ###/ ##   ####  ##   ###/  ##     ###/ /   ###     ##       ##    ||
||##   ## /  ###/ ##    ## ##    ##  ##    ##   ##    ##   ##      ## ##    ###    ##       ##    ||
||##   ##/    ##  ##    ## ##    ##  ##    ##   ##    ##   ##      ## ########     ### /    ### / ||
|| ##  ##     #   ##    ## ##    ##  ##    ##   ##    ##   ##      ## #######       ##/      ##/  ||
||  ## #      /   ##    ## ##    ##  ##    ##   ##    ##   ##      ## ##                          ||
||   ###     /    ##    ## ##    ##  ##    /#   ##    /#   ##      ## ####    /     #        #    ||
||    ######/      ######   ######    ####/      ####/      #########  ######/     ###      ###   ||
||      ###         ####     ####      ###        ###         #### ###  #####       #        #    ||
||                                                                  ###                           ||
||                                                           #####   ###                          ||
||                                                         /#######  /#                           ||
||                                                        /      ###/                             ||
\==================================================================================================/
""")
  time.sleep(3)
  os.system("clear")

try:
  main()
except KeyboardInterrupt:
  quit()
