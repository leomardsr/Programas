//calcular el valor de una resistencia para un led
#include <iostream>
#include <math.h>
using namespace std;
float EncontrarRes(float x, float y);
float EncontrarVolt(float c, float v);
float r, i, v;
float vf, vl;
float a, b;
int main()
//r= resistencia, i= intencidad de corriente, v=voltaje.
//vf=voltaje de fuente, vl=voltaje del led.
{
  cout << "Para calcular la resistencia correcta para un led, por favor ingrese los siguientes valores: " << endl;
  cout << "Voltaje de la fuente de corriente: ";
  cin  >> vf;
  cout << "Voltaje del led: ";
  cin  >> vl;
  cout << "Intencidad (mA): ";
  cin  >> i;
  a=EncontrarVolt(vf, vl);
  b=EncontrarRes(i, v);
  cout << "la resistencia apta para su bombillo led es de: " << b << " oms." << endl;
  return 0;
}
float EncontrarVolt(float vf, float vl)
{
  v=vf-vl;
  return v;
}
float EncontrarRes(float v, float i)
{
  int e=-10;
  i=pow(i,e);
  r=v/i;
  return r;
}
