// Author: Daisy Hardwick
// Class: CIS-170
// Program: Kilometer Converter Pseudocode

#include <iostream>
using namespace std;

void displayIntro()
{
  cout << "Welcome to the Kilometer to Miles Converter!" << endl;
};

void kilometerToMileConverter()
{
  // Declaring variables and constants
  float kilometers;
  float miles;
  const float KILOMETER_TO_MILE_CONVERSION_RATE = 0.6214;

  // Gathering input from user
  cout << endl << "Please enter the amount in kilometer(s)" << endl;
  cin >> kilometers;

  // Calculating miles
  miles = kilometers * KILOMETER_TO_MILE_CONVERSION_RATE;

  // Displaying output
  cout << kilometers << " kilometer(s) is equal to " << miles << " mile(s)." << endl;
};

int main()
{
  displayIntro();
  kilometerToMileConverter();
};