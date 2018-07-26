#include <iostream>
using namespace std;
float hacerRes(float x, float y);
int main()
{
  float v1, v2, res;
  float resta;
  cout << "Para realizar la resta ingrese el primer valor: ";
  cin  >> v1;
  cout << "Ingrese el segundo valor: ";
  cin  >> v2;
  resta=hacerRes(v1,v2);
  cout << "El resultado de la resta es: " << resta << endl ;
  return 0;
}
float hacerRes(float v1, float v2)
{
  float res;
  res=v1-v2;
  return res;
}
