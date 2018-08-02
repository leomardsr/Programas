//potencias
#include <iostream>
using namespace std;
int main ()
{
    int r,b,e,l=1;
    cout << " Para realizar la operacion del exponente ingrese la base: ";
    cin  >> b;
    cout << endl << " ahora ingrese el exponente: ";
    cin  >> e;
    for (int i=1 ; i<=e ; i++)
    {
        r=r*b;
    }
    cout << " El resultado es: " << r << endl;
    return 0;
}
