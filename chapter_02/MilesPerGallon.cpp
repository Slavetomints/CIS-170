#include <iostream>
// Author: Daisy Hardwick
// Class: CIS-170
// Assignment: Miles-Per-Gallon C++ Program
using namespace std;

int main()
{
  // Initializing variables
  float milesDriven;
  float gasUsed;
  float gasMileage;

  // Getting the amount of miles driven
  cout << "How many miles have you driven?" << endl;
  cin >> milesDriven;

  // Getting the amount of gas used
  cout << "How many gallons of gas did you use?" << endl;
  cin >> gasUsed;

  // Preforming gas milage calculation
  gasMileage = milesDriven / gasUsed;

  // Displaying gas mileage
  cout << "You drove " << gasMileage << " miles per gallon of gas." << endl;
  return 0;
}