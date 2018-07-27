//menu de hotel
#include <iostream>
using namespace std;
int MenuHotel(int x, int y, int z, int a);
int t;
int h;
int total;
int hab;
int est;
int rest;
int main()
{
  cout << " Hola, Bienvenido al hotel 'Soberano'." << endl;
  cout << "Hoy tenemos 3 tipos de Habitaciones disponibles, cada una con diferentes precios. " << endl;
  cout << "1. Habitacion 1 Estrella. " << endl;
  cout << "2. Habitacion 3 Estrellas. " << endl;
  cout << "3. Habitacion 5 Estrellas. " << endl;
  cout << " Segun el numero de Estrellas los precios varian. " << endl;
  t=MenuHotel(hab, t, total, est);
  return 0;
}
int MenuHotel(int hab, int t, int total, int est)
{
  int restau;
  int sre;
  cout << "Por favor ingrese el numero correspondiente a la habitacion deseada: " << endl;
  cin  >> hab;
  if (hab==1)
  {
    int est=2000000;
    int sre=2000000;
    cout << endl;
    cout << "-------------------------------------------------------------------------------------------------------------------------" << endl;
    cout << endl;
    cout << "Genial, ud a elegido la habitacion de una estrella. " << endl;
    cout << "Ud tiene como beneficios: " << endl;
    cout << "* 1 Cama y Sabanas. " << endl;
    cout << "* 1 Cocina (2 hornillas). " << endl;
    cout << "* Servicio telefonico. " << endl;
    cout << "El precio de alquiler por noche en esta habitacion es de: " << est << " Bsf. " << endl;
    cout << "Desea usted servicio de restaurant?." <<endl;
    cout << " 1. Si " << endl;
    cout << " 2. No"<< endl;
    cin  >> restau;
    if (restau==1)
    {
      cout << "Excelente eleccion. Esto agrega a su cuenta + 2.000.000 Bsf. "<< endl;
      total=est+sre;
      cout << "Eso quiere decir que el precio actual de su estancia es de: " << total << endl;
      cout << "Desea comprar el servicio del restaurant?. "<< endl;
      cout << "Seleccione el numero correspondiente a su eleccion: " << endl;
      cout << "1. Si." << endl;
      cout << "2. No." << endl;
      cin  >> h;
      if (h==1)
      {
        cout << "Excelente, Entonces su monto a pagar sera de: " << total << " Bsf." << endl;
        cout << "Gracias por su visita... Buena estancia y pronto regreso. " << endl;
        return total;
      }
      else if (h==2)
      {
        total=total-sre;
        cout << "Excelente, Entonces su monto a pagar sera de: " << total << " Bsf." << endl;
        cout << "Gracias por su visita... Buena estancia y pronto regreso. " << endl;
        return total;
      }
    }
    else if (restau==2)
    {
      cout << "Excelente. El precio actual de su alquiler es de: " << est << " Bsf. " << endl;
      cout << "Gracias por su visita... Buena estancia y pronto regreso. " << endl;
      return 0;
    }
  }
  else if (hab==2)
  {
    int est=5000000;
    int sre=1000000;
    cout << endl;
    cout << "--------------------------------------------------------------------------" << endl;
    cout << endl;
    cout << "Genial usted ha elegido la habitacion 3 Estrellas. " << endl;
    cout << "Ud posee como beneficios: " << endl;
    cout << "* 2 Camas, Sabanas y Cobijas. " << endl;
    cout << "* Cocina (4 hornillas). " << endl;
    cout << "* Servicio telefonico. " << endl;
    cout << "* Servicio Wifi. " << endl;
    cout << "* 1 televisor. " << endl;
    cout << "El precio de el alquiler de esta habitacion es de: " << est << " Bsf. " << endl;
    cout << "Desea ud el servicio de restaurant?. " << endl;
    cout << "Seleccione el numero correspondiente a su eleccion: " << endl;
    cout << "1. Si" << endl;
    cout << "2. No" << endl;
    cin  >> restau;
    if (restau==1)
    {
      cout << "Excelente eleccion. El precio del servicio de restaurant añade a su cuenta: ";
      cout << sre << " Bsf." << endl;
      total=est+sre;
      cout << "Eso quiere decir que el precio total de su estadia es de: " << total << " Bsf. " << endl;
      cout << "Desea comprar el servicio del restaurant?. "<< endl;
      cout << "Seleccione el numero correspondiente a su eleccion: " << endl;
      cout << "1. Si." << endl;
      cout << "2. No." << endl;
      cin  >> h;
      if (h==1)
      {
        cout << "Excelente, Entonces su monto a pagar sera de: " << total << " Bsf." << endl;
        cout << "Gracias por su visita... Buena estancia y pronto regreso. " << endl;
        return total;
      }
      else if (h==2)
      {
        total=total-sre;
        cout << "Excelente, Entonces su monto a pagar sera de: " << total << " Bsf." << endl;
        cout << "Gracias por su visita... Buena estancia y pronto regreso. " << endl;
        return total;
      }
      cout << "Gracias por su visita. Buen dia y Pronto regreso. " << endl;
      return total;
    }
    else if (restau==2)
    {
      cout << "Genial. Eso quiere decir que el precio actual de su estadia es de: " << est << " Bsf." << endl ;
      cout << "Gracias por su visita. Buen dia y pronto regreso. " << endl;
      return 0;
    }
  }
  else if (hab==3)
  {
    int est=20000000;
    int sre=0;
    cout << endl;
    cout << "--------------------------------------------------------------------------" << endl;
    cout << endl;
    cout << "Super!. Usted ha elegido la Habitacion  estrellas!!" << endl;
    cout << "Ud posee TODOS los beneficios posibles de este hotel... ";
    cout << "  Entre los mas destacados se encuentran: " << endl;
    cout << "* 2 Camas de lujo. " << endl;
    cout << "* Picina. " << endl;
    cout << "* Televisor Pantalla plana 62 pulgadas con consola 'PlayStation 4'" << endl;
    cout << "* Servicio completo. " << endl;
    cout << "* Aire Acondicionado. " << endl;
    cout << "* Calefaccion. " << endl;
    cout << "* Servicio de restaurant gratuito. " << endl;
    cout << "Entre muchas Otras. " << endl;
    cout << "El precio de esta habitacion es de: "<< est << " Bsf. " << endl;
    cout << endl;
    cout << "Gracias por su preferencia. Buen dia y pronto regreso. " << endl;
    return est;
  }
}
