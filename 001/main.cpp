#include <iostream>
using namespace std;

int main()
{
 int x = 10;

int *pointerX = &x;

 cout << "Valor de X: " << x<< endl;
 cout << "Ponteiro de  X: " << pointerX << endl;
 cout << "Valor de x  pelo ponteiro de  X: " << *pointerX << endl;

 return 0;
}