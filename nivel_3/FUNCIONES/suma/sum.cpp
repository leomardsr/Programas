//suma con funciones
#include <iostream>
using namespace std;
float hacerSum(float x, float y);
int main()
{
  float v1, v2, r;
  float sum;
  cout << " Para realizar la suma ingrese los valores; Valor 1: ";
  cin  >> v1;
  cout << "Valor 2: ";
  cin  >> v2;
  sum=hacerSum(v1,v2);
  cout << "El resultado de la suma es: " << sum << endl;
  return 0;
}
float hacerSum(float v1, float v2)
{
  float r;
  r=v1+v2;
  return r;
}
