#include <iostream>
using namespace std;
int main()
{
    int SI,opc;
    float din,dan,S;
    SI=1000;
    cout << "Bienvenido a su cajero virtual." << endl;
    cout << "Seleccione una opcion:" << endl << endl;
    cout << "1. Deposito." << endl;
    cout << "2. Retiro." << endl;
    cout << "3. Saldo Disponible." << endl;
    cout << "4. Salir." << endl;
    cout << "Usted ha marcado: ";
    cin >> opc;
    if(opc==1)
    {
        cout << "Bien, escriba el dinero que desee introducir: ";
        cin >> din;
        S = SI + din;
        cout << "Ingreso realizado correctamente. Su saldo actual es de " << S << endl;

    }else if(opc==2)
    {
        cout << "Ahora, teclee la cantidad de capital que desea retirar: ";
        cin >> dan;
        if(dan>SI)
        {
            cout << "Error. No dispone de tanto sueldo." << endl;
        }else
        {
            S = SI - dan;
            cout << "Reintegro realizado correctamente. Su saldo actual es de " << S << endl;
        }

    }else if(opc==3)
    {
        cout << "Su saldo actual es de " << SI << endl;

    }else if(opc==0)
    {
        cout << "Gracias por utilizar este programa." << endl << endl;
    }else
    {
        cout << "Disculpe, se ha equivocado al marcar." << endl << endl;
    }
    return 0;
}
