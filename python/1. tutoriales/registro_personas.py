#nombre,apellido,cedula,telefono,correo
libreta_de_datos={"Nombre" : None, "Apellido" : None, "Cedula" : None , "Telefono" :None, "Correo":None}

class datos_personas():
	nombre=None
	apellido=None
	ci=None
	telefono=0
	correo=None

	
	def registro(self):
		#try:
		libreta_de_datos["Nombre"] =input("Ingrese su nombre: ")
		nombre.upper()
		#except:
		#	print ("El Valor ingresado es incorrecto. Debe introducir solo letras.")
		#	pass

		try:
			libreta_de_datos["Apellido"]=input("Introduce tu apellido: ")
			apellido.upper()
		except:
			print ("El Valor ingresado es incorrecto. Debe introducir solo letras.")
			pass

		try:
			libreta_de_datos["Cedula"] =int(input("Ingresa tu numer de Cédula: "))
		except:
			print ("El Valor ingresado es incorrecto. Debe introducir solo numeros.")
			pass

		try:
			libreta_de_datos["Telefono"] =int(input("Introduce tu numero telefonico: "))
		except:
			print ("El Valor ingresado es incorrecto. Debe introducir solo numeros.")
			pass


		libreta_de_datos["Correo"] =input("Ingresa tu correo electrónico: ")

print("Bienvenido al registro. Para registrarse escriba 'Registro'")

accion=input()
accion.lower()

accion2=False
intentos=0

#while accion2==False and intentos<3:

	#if accion=="registro":
	#	accion2=True
	#	break;

	#else:
	#	accion2=False
	#	print ("Valor incorrecto, escriba 'registro' ")
	#	continue
	#intentos=+1
persona1=datos_personas()
persona1.registro()
datos_personas().libreta_de_datos																		




