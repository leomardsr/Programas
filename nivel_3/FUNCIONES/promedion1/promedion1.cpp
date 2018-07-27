// promedio de n
#include <iostream>
using namespace std;
float r;
float s, rs; 
float r1;
float v1;
float d=0;
int num;
float encontrarPromedio(float x);
int main()
{
  cout << "Para realizar el promedio de n numeros por favor ingrese el numero de cantidades a promediar: ";
  cin  >> num;
  r=encontrarPromedio(v1);
  cout << "La suma de las cantidades es: "  << s << " ." << endl;
  cout << "Y el promedio de los digitos es: " << r << " ."<< endl;
  return 0;
}
float encontrarPromedio(float v1, float d)
{
  int i;
  for(i=1 ; i<=num ; i++)
  {
      cout<<"Por favor ingrese el numero: "<<endl;
      cin>>v1;
      d=d+v1;
  }
  r1=d/num;
  return r1;
}
