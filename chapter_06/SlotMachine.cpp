// Author: Daisy Hardwick
// Class: CIS-170
// Program: Slot Machine C++ Program

#include <iostream>
#include <time.h>
#include <unistd.h>

using namespace std;

float enterAmountOfMoney()
{
  float money;
  cout << "Please enter the amount of money you wish to bet" << endl;
  cin >> money;
  if (money < 0) 
  {
    cout << "Please enter an amount greater than or equal to zero." << endl;
    enterAmountOfMoney();
  }
  return money;
}

string getChoice()
{
  // Allows for randomness, otherwise they're all the same
  sleep(6);
  unsigned seed = time(0);

  string stringArray[6] = {"Cherries", "Oranges", "Plums", "Bells", "Melons", "Bars"};

  srand(seed);
  
  int randomIndex;

  randomIndex = 1 + rand() % 5;

  string word = stringArray[randomIndex];
  cout << word << endl;
  return word;
}

void checkWinnings(float money, string firstWord, string secondWord, string thirdWord)
{
  if (firstWord == secondWord && firstWord == thirdWord)
  {
    money = money * 3;
    cout << "You won $" << money << "!" << endl;
  } else if (firstWord == secondWord || firstWord == thirdWord || secondWord == thirdWord)
  {
    money = money * 2;
    cout << "You won $" << money << "!" << endl;
  } else
  {
    cout << "You loose!" << endl;
  }
}

int main()
{
  string answer;

  do 
  {
    float money;
    money = enterAmountOfMoney();
    
    string firstWord;
    firstWord = getChoice();

    string secondWord;
    secondWord = getChoice();

    string thirdWord;
    thirdWord = getChoice();

    checkWinnings(money, firstWord, secondWord, thirdWord);

    cout << "Do you want to play again? Please enter 'Y' or 'y' to do so." << endl;
    cin >> answer;
  
  } while (answer == "y" || answer == "Y");

  cout << "Bye Bye!" << endl;

  return 0;
}