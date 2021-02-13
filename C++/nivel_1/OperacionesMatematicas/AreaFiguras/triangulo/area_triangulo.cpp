//calcular el area de un triangulo
#include <iostream>
using namespace std;
int main()
{
	float resultado,base,altura;
	cout<<" Por Favor Ingrese la base del triangulo:  "<<endl;
	cin>> base;
	cout<<"Por favor Ingrese la altura:  "<<endl;
	cin>>altura;
	resultado=(base*altura)/2;
	cout<<"El area del triangulo es:  "<<resultado<<endl;
	return 0;
}
