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
        return "Cantidad inválida. Introduzca uno de los\
        numeros que se indican."

    elif opcion == 1:"""


lista_personas = []


class Personas():
<<<<<<< HEAD
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
		lista_personas.append("")
		lista_personas.append(self.nombre)
		lista_personas.append(self.apellido)
		lista_personas.append(self.cedula)
		lista_personas.append(self.telefono)
		lista_personas.append(self.correo)

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
persona.Listado()
#persona.Impresion(lista_personas)
persona.Eliminado()
persona.Impresion()





	#print("")
	#print("Personas registradas: ")
	#print(lista_personas)"""

=======
    nombre = ""
    apellido = ""
    cedula = ""
    telefono = ""
    correo = ""

    def Registro(self):
        print("")
        self.nombre = input("Nombres: ")
        self.apellido = input("Apellidos: ")
        self.cedula = input("Cedula: ")
        self.telefono = input("Telefono:")
        self.correo = input("Correo: ")

    def Listado(self):
        print("")
        lista_personas.append("---------")
        lista_personas.append(self.nombre)
        lista_personas.append(self.apellido)
        lista_personas.append(self.cedula)
        lista_personas.append(self.telefono)
        lista_personas.append(self.correo)

    def Impresion(elemento):
        print("")
        print("Personas registradas: ")
        for i in lista_personas:
            yield i
            print(i)


persona = Personas()
persona.Registro()
persona.Listado()
persona.Impresion()
>>>>>>> d4d27c2ee77f437bd77174397bae8ec745e13b14
