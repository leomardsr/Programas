#include <iostream>
using namespace std;
int main()
{
	int a, resultado,c;
    int s,n;
   	cout<<"Ingrese el numero: ";
   	cin>> a;
    cout<<" ¿Desea ud ver la tabla de multiplicar de "<<a<<" del 1 al 12? [s/n]"<<endl;
    cin>>c;
    if (c==s)
    {  	
        for(int i=0; i<=12; i++)
	    {
		    resultado=a*i;
   		    cout<<a<<"*"<<i<<"="<<resultado<<endl;
	    }
    }
    else
    {
        cout << " Gracias por su visita. Buen dia." <<endl;
    }
    return 0;
}
