#include <iostream>
// Author: Daisy Hardwick
// Class: CIS-170
// Assignment: Miles-Per-Gallon C++ Program
using namespace std;

int main()
{
  // Declare variables
  float milesDriven;
  float gasUsed;
  float gasMileage;

  // Prompt user for miles driven
  cout << "How many miles have you driven?" << endl;
  cin >> milesDriven;

  // Prompt user for gallons of gas used
  cout << "How many gallons of gas did you use?" << endl;
  cin >> gasUsed;

  // Calculate miles-per-gallon
  gasMileage = milesDriven / gasUsed;

  // Display results
  cout << "You drove " << gasMileage << " miles per gallon of gas." << endl;
  return 0;
}