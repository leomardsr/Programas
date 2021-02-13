//cajero funciones
#include <iostream>
using namespace std;
float hacerDepo(float a);
float hacerReti(float b);
float Registrar(char  d);
float saldo=100000, cantidad, total1;
int accion, v;
int nrocuenta;
char nombre[15], nomusu[20], clave[20];
int main()
{
  cout << "Bienvenido al Banco 'El Chama'. " << endl;
  cout << "Por Favor ingrese el numero correspondiente a la accion que desea realizar: " << endl;
  cout << "1. Deposito. " << endl;
  cout << "2. Retiro. "   << endl;
  cout << "3. Consulta. " << endl;
  cout << "4. Registrar." << endl;
  cout << "5. Transferencia" << endl;
  cout << "6. Salir. "    << endl;
  cin  >> accion;

  if (accion==1)

  {
    cout << "Por favor ingrese el monto a depositar: ";
    cin  >> cantidad;
    cout << "Su transaccion ha sido completada exitosamente. " << endl;
    cout << " su saldo actual es de: " << hacerDepo(total1) << " Bsf." << endl;
    return 0;
  }

  else if (accion==2)

  {
    cout << "Por favor ingrese el monto a retirar: " << endl;
    cin  >> cantidad;
    if (cantidad>saldo)
    {
      cout << "Lo sentimos, Ud no posee saldo suficiente para realizar esta operacion. " << endl;
      cout << "Buen dia y disculpe las molestias ocasionadas. " << endl;
      return 0;
    }
    else
    {
      cout << "El retiro ha sido aprobado. " << endl;
      cout << "Ud esta apunto de retirar la siguiente cantidad: " << cantidad << " Desea retirar este monto?" << endl;
      cout << "1. Si" << endl;
      cout << "2. No" << endl;
      cin  >> v;
      if(v==1)
      {
        cout << "Retiro realizado correctamente. " << endl;
        cout << "Su saldo actual es de: " << hacerReti(total1) << endl;
        return 0;
      }
      else if (v==2)
      {
        cout << "Transaccion ha sido completada exitosamente. , Gracias por su preferencia, Buen dia." << endl;
        return 0;
      }
    }
  }
  else if(accion==3)
  {
    cout << "El saldo disponible de su cuenta es de: " << saldo << " Bsf. " << endl;
    cout << "Gracias por su preferencia y colaboracion. FELIZ DIA. " << endl;
    return 0;
  }
  else if (accion==4)
  {
    float saldo=0;
    cout << "Nuevamente Bienvenido, para Registrarse en nuestra empresa por favor ingrese su nombre. " << endl;
    cin  >> nombre;
    cout << "Muy bien, ingrese el nombre de usuario que desea utilizar " << endl;
    cin  >> nomusu;
    cout << "Por favor ingrese su contraseña: " << endl;
    cin  >> clave;
    cout << "Su transaccion ha sido completada exitosamente. " << endl;
    cout << "Ud posee un saldo actual de: " << saldo << endl;
    cout << "Desea ud hacer un deposito a su cuenta?. " << endl;
    cout << "1. Si" << endl;
    cout << "2. No" << endl;
    cin  >> v;
    if(v==1)
    {
      cout << "Por favor ingrese el monto a depositar: " << endl;
      cin  >> cantidad;
      total1 = cantidad + saldo;
      cout << "Deposito realizado correctamente, su saldo actual es de: " << total1 << endl;
      cout << "Gracias por su preferencia Sr.(a) " << nombre << endl;
      return 0;
    }
  }
  else if (accion==5)
  {
    cout << "Para realizar la transferencia ingrese el numero de cuenta del destinado: " << endl;
    cin  >> nrocuenta;
    cout << "Bien, ahora ingrese el monto a transferir: " << endl ;
    cin  >> cantidad;
    cout << "Esta usted seguro de transferir " << cantidad << " a " << nrocuenta << " ?. " << endl;
    cout << "1. Si" << endl;
    cout << "2. No" << endl;
    cin  >> v;
    if(v==1)
    {
      if (cantidad>saldo)
      {
        cout << "Ud no posee el saldo suficiente para realizar esta transaccion. " << endl;
        return 0;
      }
      else
      {
        total1= saldo - cantidad;
        cout << "Su transaccion ha sido completada exitosamente. " << endl;
        cout << "Ahora su saldo actual es de: " << total1 << endl;
        cout << "Gracias por su preferencia. FELIZ DIA. " << endl;
        return 0;
      }
    }
  }
  else if (accion==6)
  {
    return 0;
  }
}
float hacerDepo(float total1)
{
  total1 = cantidad + saldo;
  return total1;
}
float hacerReti(float total1)
{
  total1= saldo - cantidad;
  return total1;
}
