#include <iostream>
using namespace std ;
int main()
{
    int i,num,res,suma,l=1;
    cout<<"Por favor ingrese Cuantos numeros desea sumar"<<endl;
    cin>>num;
    for(i=1 ; i<=num ; i++)
    {
        cout<<"Por favor ingrese el numero "<<endl;
        cin>>res;
        suma=res+l;
        l=suma;  
    }   
     cout<<"El numero total de los numeros a sumar son : "<<num<<endl;
   
     cout<<"El Resultado es : "<<suma<<endl;
   
     return 0;
}
