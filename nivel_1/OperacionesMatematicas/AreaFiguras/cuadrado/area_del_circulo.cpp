//calcular el area de un crculo
#include <iostream>
using namespace std;
int main()
{
	float resultado,radio,pi=3.14;
    cout<<" ingrese el radio del circulo: ";
    cin>>radio;
    resultado=radio*radio*pi;
    cout<<" El area del circulo es: "<<resultado<<endl;
    return 0;
}
