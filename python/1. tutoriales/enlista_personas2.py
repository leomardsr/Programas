print ("Bienvenido. Para hacer su registro rellene el formulario: ")

lista_personas = []

def menu():
	print("Seleccione cual de las opciones desea realizar: ")
	print("1. Registrar")
	print("2. Eliminar")
	print("3. Añadir")
	print("4. Editar")
	print("5. Ubicar")
	

def Listado(person):
		print("")
		lista_personas.append(person)




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
		

	
	def Eliminado(self):
		print ("")

		contador = -1

		for i in lista_personas:

			contador += 1
			
			if contador == 0:
				pass
			
			else: 
				print (contador, ". ",i)



		print ("")
		numero = int(input("Ingrese la posicion de la lista que desea eliminar: "))
		print ("")

		del(lista_personas[numero])

		
	
	def Impresion(*datos):
		print ("")
		for i in lista_personas:
			print (i)

		
persona=Personas()
persona.Registro()
Listado(persona)
#persona.Impresion(lista_personas)
#persona.Impresion()
print (lista_personas)

