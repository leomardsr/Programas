print ("Bienvenido. Para hacer su registro rellene el formulario: ")
#print ("")

a=True

class Personas():
	nombre = ""
	apellido = ""
	cedula = ""
	telefono = ""
	correo = ""

	def Registro(self):
		print("")
		self.nombre = input ( "Nombres: " )
		self.apellido = input ("Apellidos: ")
		self.cedula = input ("Cedula: ")
		self.telefono = input ("Telefono:")
		self.correo = input ("Correo: ")
		

	def Impresion(self):
		
		print("")
		print("Persona registrada: ")
		print ("Nombres: ", self.nombre, "\nApellidos: ", self.apellido, "\nCedula: ", self.cedula, "\nTelefono: ",
			self.telefono, "\nCorreo: ", self.correo)
		print("")


while a:

	person=Personas()
	person.Registro()
	person.Impresion()
	print("\nDesea registrar a alguien mas?")
	try:
		b=str(input("Sí su respuesta es 'Si' escriba 'yes', sino escriba 'no' "))
	except:
		print ("Respuesta invalida. el programa ha finalizado")

	b.lower()

	if b == "yes":
		a=True
		continue

	elif b == "no":
		print ("Perfecto, su registro ha sido exitoso. \nEl programa ha FINALIZADO.")
		break;

	else:
		print("El Caracter ingresado es incorrecto. programa FINALIZADO.")
		break;

print("-----------------------------------------------------------------------------------------------------------")