#include <iostream>
using namespace std;
int main()
{
    float resultado,valor1,valor2,valor3,valor4,valor5,valor6,valor7,valor8;
    cout<<"Ingrese el Primer Monto: ";
    cin>>valor1;
    cout<<"ingrese el Segundo Monto:  ";
    cin>>valor2;
    cout<<"Ingrese el Tercer Monto:  ";
    cin>>valor3;
    cout<<"Ingrese el Cuarto Monto:  ";
    cin>>valor4;
    cout<<"Ingrese el Quinto Monto:  ";
    cin>>valor5;
    cout<<"ingrese el Sexto Monto:  ";
    cin>>valor6;
    cout<<"ingrese el Septimo Monto:  ";
    cin>>valor7;
    cout<<"ingrese el octavo Monto para sacar el promedio de ellos:  ";
    cin>>valor8;
    resultado=(valor1+valor2+valor3+valor4+valor5+valor6+valor7+valor8)/8;    
    cout<<"Los valores ingresadosTienen como promedio:"<<endl<<resultado<<endl;
    return 0;
}

