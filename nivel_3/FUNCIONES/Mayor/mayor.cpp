//encontrar mayor con funciones
#include <iostream>
using namespace std;
float mostrarMay(float x, float y);
int main()
{
  float v1, v2, may;

  cout << "Para mostrar el mayor de dos numeros ingrese los digitos: ";
  cin  >> v1 >> v2;
  may=mostrarMay(v1,v2);
  cout << "El mayor de los numeros es: " << may << endl;
  return 0;
}
float mostrarMay(float v1, float v2)
{
  float numMayor;
  if (v1>v2)
  {
    numMayor=v1;
  }
  else
  {
    numMayor=v2;
  }
  return numMayor;
}
