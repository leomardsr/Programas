print ("Bienvenido. Para hacer su registro rellene el formulario: ")

def elementos():
	pass


def menu():
	print("Seleccione cual de las opciones desea realizar: ")
	print("1. Registrar")
	print("2. Eliminar")
	print("3. Añadir")
	print("4. Editar")
	print("5. Ubicar")
	pass

	"""if opcion<1 or opcion>5 or opcion==str():
		return "Cantidad inválida. Introduzca uno de los numeros que se indican."

	elif opcion == 1:"""

lista_personas = []
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
		

	def Listado(self):
		print("")
		lista_personas.append(self.nombre)
		lista_personas.append(self.apellido)
		lista_personas.append(self.cedula)
		lista_personas.append(self.telefono)
		lista_personas.append(self.correo)
		
	
	def Impresion(self):
		
		print("")
		print("Personas registradas: ")
		print (lista_personas)
		print("")

persona=Personas()
persona.Registro()
persona.Listado()
persona.Impresion()