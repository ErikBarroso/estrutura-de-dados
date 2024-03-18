#include <iostream>
using namespace std;

int main()
{
 int x = 10;
int *pointer = &x;

*pointer = 300;
cout << "Valor de x alterado pelo ponteiro: " << x << endl; //300
cout << "pointer: " << *pointer << endl;                    // 300

x = 100;
cout << "Valor do ponteiro alterado por x: " << *pointer << endl;  //100
cout << "x: " << x << endl;                                        // 100

return 0;
}