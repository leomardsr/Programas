numero_mayor = 0
numero_menor = None
numero_menor2 = 0
numero = None
numero2 = None
intentos = 0
yo = True

while yo == True:	
	print ("Si desea terminar con el programa escriba 'done'")
	if numero=="done":
		break;
	intentos+=1
	try:
		numero = (input("Ingrese un numero: ")
		
	except: 
		print ("El valor que ha ingresado es un termino incorrecto")
		numero=int(numero)

		if numero > numero_mayor:
			numero_mayor=numero

		elif numero_menor is None:
			numero_menor=numero

		elif numero < numero_menor:
			numero_menor=numero
	


print ("El numero mayor es: ", numero_mayor, ". Y el numero menor: ", numero_menor)
# print ("Intentos: ", intentos)

