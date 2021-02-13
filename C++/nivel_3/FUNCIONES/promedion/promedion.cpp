// promedio de n
#include <iostream>
using namespace std;
float r;
float s=0, rs;
float r1;
float v1;
float v2;
float d=0;
int num;
float encontrarPromedio(float x, float y, float z, float r);
float encontrarsum(float x, float y);
int main()
{
  cout << "Para realizar el promedio de n numeros por favor ingrese el numero de cantidades a promediar: ";
  cin  >> num;
  r=encontrarPromedio(v1);
  rs=encontrarSum(v1);
  cout << "La suma de las cantidades es: "  << rs << " ." << endl;
  cout << "Y el promedio de los digitos es: " << r << " ."<< endl;
  return 0;
}
float encontrarPromedio(float v1)
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
float encontrarSum(float v1)
{
  for(int i=1 ; i<=num ; i++)
  {
    s=s+v1;
  }
  return s;
}
