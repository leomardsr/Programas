//mostrar la ultima letra de una palabra
#include <iostream>
using namespace std;
int main ()
{
  char pb[20];
  int r=0;
  cout << "Para contar la ultima letra de la palabra ingresela a continuacion: ";
  cin  >> pb;
  for (int i=0 ; pb[i]!='\0'; i++)
  {
    r++;
  }
  cout << "La ultima letra de " << pb << " es la '" << pb[r-1] << "'" << endl ;
  return 0;
}
