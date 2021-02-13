//multiplicacion con funciones
#include <iostream>
using namespace std;
float encontrarMult(float x, float y);
int main()
{
  float mult;
  float n1, n2;
  cout << "Para realizar la multiplicacion, por favor ingrese el primer valor: ";
  cin  >> n1;
  cout << "Ingrese el segndo valor: ";
  cin  >> n2;
  mult = encontrarMult(n1,n2);
  cout << "El resultado de " << n1 << " * " << n2 << " Es: " << mult <<endl;
return 0;
}
float encontrarMult(float n1, float n2)
{
  float res;
  float n1, n2;
  res=n1*n2;
  return res;
}
