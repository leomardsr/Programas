#include <iostream>
using namespace std;
int main()
{
	float valor1;
	cout<<"Ingrese el valor para determinar si el monto es positivo o negativo   "<<endl;
	cin>>valor1;
	if (valor1>=0)
	{
		cout<<valor1<<"  ¡Es un numero positivo!"<<endl;
	}
	else
	{
		cout<<valor1<<"  ¡Es negativo!"<<endl;
	}
	return 0;
}
	
