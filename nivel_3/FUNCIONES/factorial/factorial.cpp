//factorial, for y funciones
#include <iostream>
using namespace std;
int hacerFac(int x, int y);
int main()
{
  int res;
  int n, r=1, f;
  cout << "Para realizar el calculo factorial de un numero, primero ingrese el numero a factorizar: ";
  cin  >> n;
  f=hacerFac(n, res);
  cout << "El resultado es: " << f << endl;
  return 0;
}
int hacerFac(int n, int res)
{
  for(int i=1 ; i<=n ; i++)
  {
    res=res*i;
  }
  return res;
}
