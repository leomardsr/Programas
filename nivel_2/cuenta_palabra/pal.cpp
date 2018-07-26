//contar tamaño de la palabra
#include <iostream>
using namespace std;
int main ()
{
    char palabra[20];
    int r=0;
    cout << "Para contar el tamaño de la palabra ingresela a continuacion: ";
    cin  >> palabra;
    for (int i=0 ; palabra[i]!='\0'; i++)
    {
      r++;
    }
    cout << r << endl;
    return 0;
}
