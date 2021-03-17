a = True
helado = 0.45



def Precio_bolivares(dolarPrecio):
	precio_dolar=dolarPrecio
	print ("")
	precio_helado = precio_dolar * helado
	print ("El precio actual de c/u Helado es de: ", precio_helado, "Bs.S ")
	print ("")
	print("")
	return precio_helado


dolar=open("leomar.txt")
dolarPrecio=dolar.read() 
dolarPrecio=float(dolarPrecio)
precio_helado=Precio_bolivares(dolarPrecio)

while a:

	try: 
		Precio_bolivares(dolarPrecio)

	except:
		print("VALOR INCORRECTO")

	print ("")
	e = input("Para comprar mas de un helado escriba 'y'   |    Para cerrar el programa escriba 'q': ")

	if e == "q":
		break

	elif e == "y":

		print()
		numero = float(input("Ingrese la cantidad de helados que desea comprar: "))
		totalBS= numero*precio_helado
		print ("")
		print("---------------------------------------------------------------------------------------------------------------")
		print("")
		print ("El total de bolivares es de: ", totalBS, "bs. Por la compra de ", numero, " Helados.")
		print("-")
		print("---------------------------------------------------------------------------------------------------------------")
	else:
		continue;

