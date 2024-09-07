// Author: Daisy Hardwick
// Class: CIS-170
// Program: Leap Year Detector C++ Program

#include <iostream>

using namespace std;

int main()
{
  // Declare variables
  int year;

  // Prompt user for year
  cout << "Please select a year" << endl;
  cin >> year;

  // Test to see if year is a leap year and display results
  if (((year % 100 == 0) && (year % 400 ==0)) || ((year % 4 == 0) && (year % 100 != 0)))
  {
    cout << year << " is a leap year" << endl;
  }
  else 
  {
    cout << year << " is not a year year" << endl;
  }
  
  return 0;
}