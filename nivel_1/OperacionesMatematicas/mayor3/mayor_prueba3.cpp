//Este programa ha sido diseñado para reconocer el mayor, o el menor monto de 3 numero ingresado por teclado.
#include <iostream>
using namespace std;
int main()
{
    float major,minor,v1,v2,v3;
    cout<<"  Este programa ha sido diseñado para reconocer el mayor o el menor monto de 5 numero ingresado por teclado.  para determinar esto, introduzca su primer numero: ";
    cin>>v1;
    cout<<" Ingrese el segundo numero: ";
    cin>>v2;
    cout<<" Ingrese el ultimo numero por favor: ";
    cin>>v3;
    if (v1==v2 && v2==v3)
    {
        cout<<" Los valores: "<<v1<<", "<<v2<<" y "<<v3<<" Son iguales"<<endl;
    }
    else
    {
        if (v1>v2 && v2>v3)
        {
            cout<<" El monto mayor es: "<<v1<<endl;
        }
        else if (v1<v2 && v2<v3)
        {
            cout<<" El monto menor de los digitos es: "<<v1<<endl;
        }
        else if (v2>v1 && v1>v3)
        {
            cout<<" El monto mayor es: "<<v2<<endl;
        }
        else if (v2<v1 && v1<v3)
        {
            cout<<" El monto menor de los digitos es: "<<v2<<endl;
        }
        else if (v3>v1 && v1>v2)
        {
            cout<<" El monto mayor es: "<<v3;
        }
        else if (v3<v1 && v1<v2)
        {
            cout<<" El monto menor de los digitos es: "<<v3<<endl;
        }
    }
    return 0;
}
        
        






