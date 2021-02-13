//Este programa ha sido diseñado para reconocer el mayor, o el menor monto de 5 numero ingresado por teclado.
#include <iostream>
using namespace std;
int main()
{
    float major,minor,v1,v2,v3,v4,v5;
    cout<<"  Este programa ha sido diseñado para reconocer el mayor monto de 5 numero ingresado por teclado.  para determinar esto, introduzca su primer numero: ";
    cin>>v1;
    cout<<" Ingrese el segundo numero: ";
    cin>>v2;
    cout<<" Ingrese el tercer numero: ";
    cin>>v3;
    cout<<" Ingrese el cuarto numero: ";
    cin>>v4;
    cout<<" Ingrese el quinto y ultimo valor: ";
    cin>>v5;
    if (v1==v2 && v2==v3 && v3==v4 && v4==v5)
    {
        cout<<" Los valores: "<<v1<<", "<<v2<<", "<<v3<<", "<<v4<<" y "<<v5<<" Son iguales"<<endl;
    }
    else
    {
        if (v1>v2 && v1>v3 && v1>v4 && v1>v5)
        {
            cout<<" El monto mayor es: "<<v1<<endl;
        }
        else if (v2>v1 && v2>v3 && v2>v4 && v2>v5)
        {
            cout<<" El monto mayor es: "<<v2<<endl;
        }
        else if (v3>v1 && v3>v2 && v3>v4 && v3>v5)
        {
            cout<<" El monto mayor es: "<<v3<<endl;
        }
        else if (v4>v5 && v4>v3 && v4>v2 && v4>v1)
        {
            cout<<" El monto mayor es: "<<v4<<endl;
        }   
        else if (v5>v4 && v5>v3 && v5>v2 && v5>v1)
        {
            cout<<" El monto mayor es: "<<v5<<endl;
        }
    }
    return 0;
}
        
        
