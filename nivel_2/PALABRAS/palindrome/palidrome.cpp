//mostrar si una palabra es o no palindrome (que es igual al derecho que al revez)
#include <iostream>
using namespace std;
int main ()
{
  char pb[20];
  int r=0, t=0;
  cout << "Para determinar si una palabra es o no palindrome, ingresela a continuacion: ";
  cin  >> pb;
  for (int i=0 ; pb[i]!='\0'; i++)
  {
    r++;
  }
  //cout << "La ultima letra de " << pb << " es la '" << pb[r-1] << "'" << endl ;
  
  return 0;
}
