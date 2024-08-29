#include <iostream>
#include <string>
using namespace std;

int main()
{
  string name;
  int age;

  cout << "What is your name?" << endl;
  getline(cin, name);
  cout << "What is your age?" << endl;
  cin >> age;

  cout << "Your name is " << name << ", and you are " << age << " years old." << endl;
  return 0;
}