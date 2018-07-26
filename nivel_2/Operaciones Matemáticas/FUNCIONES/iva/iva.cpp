//IVA
#include <iostream>
using namespace std;
int main()
{
  float r, r1, pc, ptd;
  cout << "Para determinar el I.V.A de un producto, por favor ingrese el porcentaje del iva: ";
  cin  >> pc;
  cout <<" Ahora por favor ingrese el precio del producto: ";
  cin  >> ptd;
  r=((pc*ptd)/100);
  cout << "El I.V.A del producto es de: " << r << endl;
  r1=r+ptd;
  cout << "Y el precio total del producto es de: " << r1 << "Bsf." << endl;
  cout << "Gracias por su visita... Buen dia y pronto regreso." << endl;
  return 0;
}
