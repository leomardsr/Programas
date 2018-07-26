//factoriales con for
#include <iostream>
using namespace std;
int main()
{
  int v1, res=1;
  cout << "para realizar los calculos factoriales, ingrese el numero: ";
  cin  >> v1;
  if (v1<0)
  {
    cout << "Esta operacion no puede ser realizada. " << endl;
  }
  else
  {
    for(int i=1 ; i<=v1 ; i++)
    {
      res=res*i;
    }
    cout << "El resultado es: " << res << endl;
  }
  return 0;
}
