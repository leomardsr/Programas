precio = open("leomar.txt")
precio = precio.read()
precioDolar = float(precio)

class helado():
	def __init__ (self):

		self.sabor = None
		self.cantidad = 0
		self.helado_dolar = 0.45
		self.precioBolivares = self.helado_dolar*precioDolar 


	def Precios(self):
		print ("El precio c/u de helados es de: ")
		print ()
		print ("Bolivares: ", self.precioBolivares)
		print ()
		print ("Dolares: ", self.helado_dolar)
		print()
		print("---------------------------------------------------------------------")


	def calculo(self,numero):
		self.cantidad_hela2=numero
		self.montoBolivares=numero*self.precioBolivares
		self.montoDolares=numero*self.helado_dolar

		print ("El monto total de ", self.cantidad_hela2, " Helados es de: ")
		print ("Bolivares: ", self.montoBolivares )
		print ("")
		print ("Dolares: ", self.montoDolares)
		print()
		print("---------------------------------------------------------------------")

helados=[]

def inventario():

	print()
	ice_cream=helado()
	ice_cream.sabor=input("Sabor del helado: ")
	ice_cream.cantidad=int(input("Cantidad de helados: "))
	ice_cream.append(helado)
	print()

def show():
	print ()
	print ("Sabor  |  Disponibles  |  Precio Bs.S  |  Precio $  |")
	for i in helados:
		print (ice_cream.sabor, "  |  ", ice_cream.cantidad, "  |  ", ice_cream.precioBolivares,
			 "  |  ",ice_cream.helado_dolar, "  |  ")


def menu():


	a=True
	while a:
		print("--------------------HELADOS DIEGO DE LA VEGA-------------------------")
		print("1. Mostrar precios")
		print("2. Calcular Varios Helados")
		print("3. Inventario")
		print("4. Finalizar el programa")
		print()
		op = input("Escribe el numero de la opcion a realizar: ")


		if op == "" or op =="1":
			helado.Precios()


		elif op == "2":
			numero = int(input("Ingrese la cantidad de helados que desea llevar: "))
			helado.calculo(numero)

		elif op == "3":
			inventario()	
		
		elif op == "4":
			a=False


		else:
			print()
			print(" ________________________________")
			print("|                                |")
			print("|                                |")
			print("|        OPCION INVALIDA         |")
			print("|                                |")
			print("|________________________________|")
			print()
			print()



helado=helado()
menu()


