
print("---------------------Heladeria El YOYO-------------------------")

dollar = open("dolar.txt", "r")
dollar_price = float(dollar.read())
dollar.close()

IceCream = []

amount = 0
price = 0.45
flavor = ""
Bs_Price = price*dollar_price

class Ice_Cream():

	def __init__(self):

		self.amount = amount
		self.flavor = flavor
		self.price = price
		self.Bs_Price = price*dollar_price

	def prices(self):
		print()
		print("C/U Helado tiene un precio de: ")
		print("\nBolivares: " , self.Bs_Price)
		print("\nDolares: ", self.price)
		print("__________________________________________________________________________________________")

	def calculate(self):
		number =int(input("\nIntroduce la cantidad de helados que desea llevar: "))
		total_price = self.price*number
		total_bs_price = self.Bs_Price*number
		print ("Para ",number," de helados, el precio total es de: ") 
		print ("\nBolivares: ", total_bs_price)
		print ("\nDolares: ", total_price)
		print ("__________________________________________________________________________________________")



def menu():
	print()
	a = True
	while a:

		print("Menu: ")
		print("\t1. Precios")
		print("\t2. Calcular")
		print("\t3. Inventario")
		print("\t4. Editar")
		print("\t5. // Finalizar Programa //\n")
		option = input("Elija una opcion: ")
		option = option.strip()

		if option == "" or option == "1":
			helado.prices()

		elif option == "2":
			helado.calculate()

		elif option == "3":
			inventary()

		elif option == "4":
			print ("¿Que desea editar?: ")
			print ("\t1. Precio Dolar. ")
			print ("\t2. Inventario. ")
			print ("\t3. // VOLVER AL MENU ANTERIOR //")
			op = input("Eljie una opcion: ")

			if op == "" or op == "1":
				Dollar_Edith()

			elif op == "2":
				inventary()

			else:
				continue


		elif option == "5":
			break

		else:

			print (" __________________________")
			print ("|                          |")
			print ("|     OPCION INVALIDA      |")
			print ("|__________________________|")
			print ("")




def inventary():
	q=True

	while q:

		print ("Menu Inventario: ")
		print ("\t1. Mostrar inventario.")
		print ("\t2. Añadir al inventario.")
		print ("\t3. Eliminar elemento del inventario.")
		print ("\t4. Editar inventario.")
		print ("\t0. // Volver al menu anterior. //\n")
		in_op = input ("Elija una opcion: ")
		in_op = in_op.strip()


		if in_op== "" or in_op=="1":
			show()


		elif in_op == "2":
			w=True
			while w:
	
				print ()
				helado_inventario = Ice_Cream()
				helado_inventario.amount = int(input("Ingrese la cantidad de helados que hay: "))
				helado_inventario.flavor = input("Ingrese el sabor del helado: ")
				IceCream.append(helado_inventario)
				print()
				show()
				op = input("Para Añadir, Editar o Eliminar alguno escriba '0' : ")
				if op == "0":
					w=False

				else:
					w=True

		elif in_op == "3":
			show()
			position = int(input("Elije el elemento que deseas eliminar: "))-1
			IceCream.pop(position)
			show()

		elif in_op== "4":
			position = int(input("Elije el elemento que deseas editar: "))-1
			print ()
			helado_inventario = Ice_Cream()
			helado_inventario.amount = int(input("Ingrese la cantidad de helados que hay: "))
			helado_inventario.flavor = input("Ingrese el sabor del helado: ")
			IceCream.pop(position)
			IceCream.insert(position,helado_inventario)
			print("\nInventario Actualizado: ")
			show()

		elif in_op == "0":
			q=False

		else:
			inventary()



def show():
	
	print ()
	print ("|  H. Disp  |  H. Sabor  |  H. Precio $  | H. Precio BS. ")
	for helado in IceCream:
		print ("|  ", helado.amount, "  |  ", helado.flavor, "  |  ", helado.price, "  |  ", helado.Bs_Price)
	print ()
	print ("__________________________________________________________________________________________")

def Dollar_Edith():
	print ("El precio actual del dolar es de: ", dollar_price , "\n")
	dollar=open("dolar.txt","w")
	dollar_price=float(input("Introduce el nuevo precio del dolar: "))
	dollar.write(dollar_price)
	dollar.close()
	print ("\nPrecio del Dolar actualizado: ", dollar_price, "\n")

helado = Ice_Cream() 

menu()