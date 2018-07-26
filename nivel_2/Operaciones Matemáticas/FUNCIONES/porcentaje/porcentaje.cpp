//porcentaje normal
#include <iostream>
using namespace std;
int main()
{
  float pc, ptd,res;
  //pc=poncentaje; ptd=porcentado; res=resultado
  cout << "Si desea realizar el porcentaje de 'n' numero por favor ingrese el porcentaje: ";
  cin  >> pc;
  cout <<"Ahora ingrese el monto a resolver: ";
  cin  >> ptd;
  res=((pc*ptd)/100);
  cout << "El porcentaje de " << ptd << " es: " << res << endl;
  return 0;
}
