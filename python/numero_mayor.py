numero_mayor = 0
numero_menor = None
numero = None
intentos = 0
yo = True

while yo == True:
	numero = (input("Ingrese un numero: "))
	if numero!="done":
		print ("Si desea terminar con el programa escriba 'done'")
	# print ("Si desea terminar con el programa escriba 'done'")
	if numero=="done":
		break;
	intentos+=1
	try:
		numero=int(numero)
	except: 
		print ("El Caracter que acaba de ingresar es incorrecto. Introduce solo numeros: ")
		continue;

	if numero > numero_mayor:
		numero_mayor=numero

	elif numero_menor is None:
		numero_menor=numero

	elif numero < numero_menor:
		numero_menor=numero
	

print ("")
print ("El numero mayor es: ", numero_mayor, ". Y el numero menor: ", numero_menor)
print ("")
print ("Intentos: ", intentos)

