#include <iostream>
using namespace std;
int main ()
{
	float division,valor1,valor2;
	cout<<" ingrese el valor numero 1:  ";
	cin>>valor1;
	cout<<"ingrese el valor2:  ";
	cin>>valor2;
	if(valor2==0)
	{
		cout<<"la division entre '0' no esta definida"<<endl;
	}
	else
	{
		division=valor1/valor2;
		cout<<" El resultado de la division es: "<<division<<endl<<endl;
	}
	return 0 ;
}