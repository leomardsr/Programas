#para este 3er ejercicio de condicionales se verá el "and" y el "or"
#para "and" podremos utliziar la traduccion (para entender): "y si ademas"
#para "or" podemos entenderlo como un "o si no"
print ("Programa de Becas 2021")
print ("Si quieres postular para una beca en este periodo escolar 2021-2022 completa el siguiente formulario: ")
distancia_escuela = float (input ("Ingresa la distancia que hay entre tu casa y la escuela (en km): "))
print (distancia_escuela)

numero_hermanos = int(input("Introduce el numero de hermanos que tienes (sin contarte a ti: "))
print (numero_hermanos)

salario_familiar = float(input("Ingresa el salario bruto familiar (en dolares): "))
print (salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 30000:
	print ("Tienes derecho a beca")

else:
	print ("No tienes derecho a beca")
