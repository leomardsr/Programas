#include <iostream>
using namespace std;
int main()
{
    float resultado,valor1,valor2,valor3,valor4,valor5;
    cout<<"Ingrese el primer Monto: ";
    cin>>valor1;
    cout<<"ingrese el segundo Monto:  ";
    cin>>valor2;
    cout<<"Ingrese el Tercer Monto:  ";
    cin>>valor3;
    cout<<"Ingrese el Cuarto Monto:  ";
    cin>>valor4;
    cout<<"Ingrese el Quinto Valor para sacar el promedio de los montos:  ";
    cin>>valor5;
    resultado=(valor1+valor2+valor3+valor4+valor5)/5;    
    cout<<"Los valores ingresadosTienen como promedio:"<<endl<<resultado<<endl;
    return 0;
}

