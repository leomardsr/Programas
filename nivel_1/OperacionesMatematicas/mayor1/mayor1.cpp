#include <iostream>
using namespace std;
int main()
{
    float major,minor,valor1,valor2;    
    cout<<" Para determinar el Monto mayor Ingrese dos numeros; 1er Numero: ";
    cin>>valor1;
    cout<<" 2do numero: ";
    cin>>valor2;
    if (valor1==valor2)   
    {   
    cout<<valor1<<"  y  "<<valor2<<"  Son iguales."<<endl;
    }
    else
    {
        if (valor1>valor2)
        {
        cout<<valor1<<"  Es Mayor que  "<<valor2<<endl;
        }    
        else
        {
        cout<<valor2<<"  Es mayor que  "<<valor1<<endl;
        }
    }
    return 0;
}
