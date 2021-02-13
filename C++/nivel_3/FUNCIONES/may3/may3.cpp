//mayor de 3 numeros con funciones (2do intento)
#include <iostream>
using namespace std;
float encontrarMay(float x, float y, float z);
int main()
{
  float max;
  float x;
  float y;
  float z;
  cout << "Para determinar el mayor de 3 numeros por favor ingrese los montos: ";
  cin  >> x >> y >> z;
  max=encontrarMay(x,y,z);
  cout << "El mayor de los montos es: " << max << endl;
  return 0;
}
float encontrarMay(float x, float y, float z)
{
  float res;
  if(x==y && x==z)
  {
    cout << "los montos son iguales. " << endl;
    cout << "El mayor de los numeros es: "<< x;
  }
  else if(x>y && x>z)
  {
    res=x;
  }
  else if(y>x && y>z)
  {
    res=y;
  }
  else if(z>x && z>y)
  {
    res=z;
  }
  return res;
}
