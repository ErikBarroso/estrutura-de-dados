#include <iostream>
using namespace std;

int main()
{
  // convertendo string
 string s1 = "10";
 string s2 = "20";

 int num1, num2;

 num1 = stoi(s1);
 num2 = stoi(s2);
 
 cout << "Soma:  " << num1 + num2 << endl;

 return 0;
}