//mostrar la ultima letra de una palabra
#include <iostream>
using namespace std;
int main ()
{
  char pb[20];
  int t=0, r2=0;
  cout << "Para mostrar la palabra al revez, ingresela a continuacion: ";
  cin  >> pb;
  for (int i=0 ; pb[i]!='\0'; i++)
  {
    t++;
  }
  for (int i=t-1 ; pb[i]>=0; i--)
  {
    cout << pb[i];
  }
    cout<<endl;


  //cout << pb << "Al revez es : " << pb[r-1] << pb[r-2] << pb[r-3] << endl ;
  return 0;
}
