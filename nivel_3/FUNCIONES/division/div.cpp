//division con funciones
#include <iostream>
using namespace std;
float encontrarDiv(float d1, float d2);
int main()
{
  float d1, d2, d;
  cout << "Division: Para dividir dos numeros, ingrese el primer digito:  ";
  cin  >> d1;
  cout << "Por favor ingrese el segundo digito: ";
  cin  >> d2;
  cout << "El resultado de " << d1 << " / " << d2 << " Es: " << encontrarDiv << endl;
  return 0;
}
float encontrarDiv(float d1, float d2)
{
  float d;
  if (d2==0)
  {
    cout << "la division entre '0' no esta definida." << endl;
  }
  else
  {
    d = d1/d2;
    return d;
  }
}
