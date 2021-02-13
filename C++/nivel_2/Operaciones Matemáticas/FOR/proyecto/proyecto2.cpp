#include <iostream>
using namespace std;
int main()
{
	float a, resultado;
   	cout<<"Ingrese el numero: ";
   	cin>> a;
   	for(int i=0; i<=12; i++)
	{
		resultado=a/i;
   		cout<<a<<"/"<<i<<"="<<resultado<<endl;
	}
	return 0;
}
