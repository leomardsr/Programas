//hipotenusa
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
    float resultado,a,b;
    cout<<" para calcular la hipotenusa de el triangulo ingrese el valor de su primer cateto: ";
    cin>>a;
    cout<<" ingrese el valor de su segundo cateto: ";
    cin>>b;
    resultado=sqrt((a*a)+(b*b));
    cout<<" La hipotenusa del triangulo tiene como valor: "<<resultado<<endl;
    return 0;
}
