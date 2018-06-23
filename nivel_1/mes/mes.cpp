//decir que mes del año es
#include <iostream>
using namespace std;
int main()
{
    float mes,v1;
    cout<<"para determinar que mes indica, ingrese el numero, preferiblemente del 1-12: ";
    cin>>v1;
    if (v1==0)
    {
        cout<<" el cero no es un numero Valido para un mes, ya que se enumeran del 1 al 12"<<endl;
    }
    else if (v1>12)
    {
        cout<<" El numero "<<v1<<" no es valido ya que los meses se enumeran del 1 al 12"<<endl;
    }
    else if (v1==1)
    {
        cout<<" el mes es 'Enero'."<<endl;
    }
    else if (v1==2)
    {
        cout<<" El mes es 'Febrero'."<<endl;
    }
    else if (v1==3)
    {
        cout<<" El mes es 'Marzo'."<<endl;
    }
    else if (v1==4)
    {
        cout<<" El mes es 'Abril'."<<endl;
    }
    else if (v1==5)
    {
        cout<<" El mes es 'Mayo'."<<endl;
    }
    else if (v1==6)
    {
        cout<<" el mes es 'Junio'."<<endl;
    }
    else if (v1==7)
    {
        cout<<" el mes es 'Julio'."<<endl;
    }
    else if (v1==8)
    {
        cout<<" El mes es 'Agosto'."<<endl;
    }
    else if (v1==9)
    {
        cout<<" El mes es 'Septiembre'."<<endl;
    }
    else if (v1==10)
    {
        cout<<" El mes es 'Octubre'."<<endl;
    }
    else if (v1==11)
    {
        cout<<" El mes es 'Noviembre'."<<endl;
    }
    else if (v1==12)
    {
        cout<<"el mes es 'Diciembre'."<<endl;
    }
    return 0;
}















   







