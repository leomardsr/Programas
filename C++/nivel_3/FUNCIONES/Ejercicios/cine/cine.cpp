//cine menu
#include <iostream>
using namespace std;
int main()
{
  int edad, personas, entrada=100, pelicula;
  cout << " Bienvenido al cine 'Merideño'. "<< endl;
  cout << "Hoy tenemos en taquilla las siguientes peliculas: " << endl;
  cout << " 1.Ready player one "  <<endl;
  cout << " 2.Fast and Furius 8 " <<endl;
  cout << " 3.Los increibles 2 "  <<endl;
  cout << "La entrada de las peliculas tienen como precio 100 Bsf. " << endl;
  cout << "Para los Estudiantes la entrada tiene un descuento del 50%. " << endl;
  cout << "Para los adultos mayores (3ra edad) Hay un descuento de 75%. " << endl;
  cout << "Por favor ingrese el numero de su pelicula favorita: ";
  cin  >> pelicula;
  if (pelicula>3)
  {
    cout << "El numero " << pelicula << " no esta disponible en taquilla en este momento. " << endl ;
    cout << "Por favor vuelva luego."<< endl;
  }
  else
  {
    cout << "Genial! Excelente eleccion...!" << endl;
    cout << "Por favor ingrese el numero correspondiente a su edad para realizar el cobro de su entrada: " << endl;
    cout << " 1. Estudiante " << endl ;
    cout << " 2. Tercera Edad " << endl;
    cout << " 3. Mayor de Edad " << endl;
    cin  >> edad;
    if (edad>3)
    {
      cout << "Lo sentimos, esta opcion no esta disponible en este momento. " << endl ;
    }
    else if (edad==1)
    {
      cout << "Asombroso ud tiene un descuento de 50%. eso quiere decir, que el valor de su entrada es de 50 Bsf. " << endl;
      cout << "Gracias por su preferencia. Disfrute su pelicula. Buen dia y Pronto regreso. " << endl;
    }
    else if (edad==2)
    {
      cout << "Asombroso ud tiene un descuento de 75%. eso quiere decir, que el valor de su entrada es de 25 Bsf. " << endl;
      cout << "Gracias por su preferencia. Disfrute su pelicula. Buen dia y Pronto regreso. " << endl;
    }
    else if (edad==3)
    {
      cout << "Asombroso. Eso quiere decir que el valor de su entrada es de: 100 Bsf. " << endl;
      cout << "Gracias por su preferencia. Disfrute su pelicula. Buen dia y Pronto regreso. " << endl;
    }
  }
  cout << "Menu creado por 'Leomar Salazar'" << endl;
  return 0;
}
