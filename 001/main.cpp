#include <iostream>
using namespace std;

int main()
{
 string name;
 double notas[4];

 cout << "Digite seu nome ";
 cin >> name;
cout << "Digite a nota do primeiro periodo: ";
cin >> notas[0];

cout << "Digite a nota do segundo periodo: ";
cin >> notas[1];

cout << "Digite a nota do terceiro periodo: ";
cin >> notas[2];

cout << "Digite a nota do quarto periodo: ";
cin >> notas[3];

double media;
media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4;
cout << "A media de  "<< name << " foi: " << media << endl;

if(media >=7) {
  cout << name << " passou de ano." << endl;
} else {
  cout << name << " perdeu de ano." << endl;
}

return 0;
}