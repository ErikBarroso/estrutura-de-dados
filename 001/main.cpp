#include <iostream>
using namespace std;

int main()
{
  double score[] = {8, 7, 10, 8.5};
  for (int i = 0; i < 4; i++)
  {
    cout << "Score " << i + 1 << " --> " << score[i] << endl;
  }
  return 0;
}