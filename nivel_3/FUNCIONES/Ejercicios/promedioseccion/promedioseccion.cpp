#include <iostream>
using namespace std;
float hacerOperacion(float a, float b, float c);
int num=10, est=0, div1=3, div2=10;
float v1, v2, v3;
float res=0, res1=0;

int main()
{
  cout << "Bienvenido a la calculadora de promedio del L.B.L. " << endl;
  cout << "Este programa es para calcular el promedio de 3 notas de 10 estudiantes y el promedio de la seccion. " << endl;
  cout << hacerOperacion(v1, v2, v3) << endl;
  return 0;
}
float hacerOperacion(float v1, float v2, float v3)
{
  for (int i=1; i<=num; i++)
  {
    est=est+1;
    cout << "Ingrese las notas del estudiante " << est << ". " << endl;
    cout << "Nota 1: ";
    cin  >> v1;
    cout << "Nota 2: ";
    cin  >> v2;
    cout << "Nota 3: ";
    cin  >> v3;
    res1=((v1+v2+v3)/div1);
    cout << "El promedio del estudiante nro: " << est << " Es: " << res1 << endl;
    if (res1<10)
    {
      cout << "Este estudiante NO aprobo. " << endl;
      cout << endl << "----------------------------------------------------------------------------------" << endl;
      cout << endl;
    }
    else
    {
      cout << "Felicidades. Este estudiante SI aprobo. " << endl;
      cout << endl << "----------------------------------------------------------------------------------" << endl;
      cout << endl;
    }
    res=res1+res;
  }
  res=res/num;
  cout << "El promedio de la seccion es de: " << res << endl;
  cout << "PROGRAMA CREADO POR LEOMAR SALAZAR. ";
}
