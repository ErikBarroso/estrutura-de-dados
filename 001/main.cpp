#include <iostream>
using namespace std;

int main()
{
  // tamanho da array
  double score[] = {8, 7, 10, 8.5};

  int sizeOfArray = sizeof(score) / sizeof(double) ;
  
  for (int i = 0; i < sizeOfArray; i++)
  {
    cout << "Score " << i + 1 << " --> " << score[i] << endl;
  }
  return 0;
}