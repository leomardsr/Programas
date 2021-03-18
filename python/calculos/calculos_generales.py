import math

def sumar(num1,num2):
  	print("El resultado de: ",num1, " + ", num2," Es de: ", num1+num2)

def restar(num1,num2):
	print("El resultado de: ",num1, " - ", num2," Es de: ", num1-num2)

def multiplicar(num1,num2):
	print("El resultado de: ",num1, " * ", num2," Es de: ", num1*num2)

def dividir(num1,num2):
	print("El resultado de: ",num1, " / ", num2," Es de: ", num1/num2)

def exponente(base, exponente):
	print("El resultado de: ",base, "^", exponente," Es de: ", base**exponente)

def redondear(numero):
	print(numero, " Redondeado es: ", round(numero))

def hipotenusa(cateto1,cateto2):
	a=cateto1**2
	b=cateto2**2
	c=math.sqrt(a+b)	
	print("La hipotenusa del triangulo rectangulo cateto1: ", cateto1, " y cateto2: ", cateto2,
		" es = ",c)

