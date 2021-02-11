#calculadora=["Bienvenido a la calculadora.", "\n1. Suma", "\n2. Resta","\n3. Multiplicacion", "\n4. Division\\"
#"\n5. Potencia" ]

print ("Bienvenido a la calculadora.")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
print ("5. Potencia")

#print (calculadora[:])

def suma(sumando1,sumando2):
	resultado = sumando1 + sumando2
	return resultado 

def resta(restando1, restando2):
	resultado = restando1- restando2
	return resultado

def mult(factor1, factor2):
	resultado = factor1*factor2
	return resultado

def division (dividendo,divisor ):
	resultado = dividendo/divisor
	return resultado

def potencia (base, exponente):
	resultado = base**exponente
	return resultado

operacion = int (input("Cual de estas operaciones desea realizar?: "))
if operacion==1:
	print ("ingrese los valores que desea sumar: ")
	suma(float (input("Sumando #1: ")), float (input ("Ahora Sumando #2: ")))
	print (suma)

elif operacion == 2:
	print ("Ingrese los valores a Restar: ")
	resta (float (input("Restando #1: ")), float (input ("Ahora el Restando #2: ")))
	resta

elif operacion == 3:
	print ("Ingrese los factores a Multiplicar: ")
	resta (float (input("Factor #1: ")), float (input ("Ahora el Factor #2: ")))
	mult

elif operacion == 4:
	print ("Ingrese los valores a Dividir: ")
	resta (float (input("Dividendo: ")), float (input ("Ahora el Divisor: ")))
	division

elif operacion == 5 :
	print ("Ingrese los valores de la potencia: ")
	resta (float (input("Base: ")), float (input ("Ahora el Exponente: ")))
	potencia
