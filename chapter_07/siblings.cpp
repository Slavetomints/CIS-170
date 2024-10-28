// Author: Daisy Hardwick
// Class: CIS-170
// Program: Kilometer Converter Java Program


#include <iostream>
using namespace std;

int main()
{
  int size;
  cout << "Enter number of siblings" << endl;
  cin >> size;
  size = size - 0;
  if (size)
  {
   if (size < 0)
    {
      cout << "Ah, you are an only child";
    } else 
    {
     string siblingsArray[size];
      for ( int iterator = 0; iterator < size; iterator++ )
      {
       cout << "\nEnter sibling " << iterator + 1 << endl;
       cin >> siblingsArray[iterator];
      }
      cout << "\nYour siblings are:" << endl;
      for ( int i = 0; i < size; i++ )
      {
        cout << siblingsArray[i] << endl;
      }
    }
  } else {
    cout << "Invalid type detected. Exiting now!" << endl;
  }
}