import pickle
class Persona():

	def __init__(self, nombre, edad, genero):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print ("Se ha creado a una persona nueva con el nombre de ", self.nombre)

	def __str__(self):
		return"{} {} {}". format(self.nombre, self.genero, self.edad)


class ListaPersonas:

	personas=[]

	def __init__(self):

		listaDePersonas=open("ficheroExterno", "ab+")
		listaDePersonas.seek(0)
		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print ("El fichero esta vacío")

		finally:
			listaDePersonas.close()
			del(listaDePersonas)
	def agregarPersonas(self, persona):
		self.personas.append(persona)

	def mostrarPersonas(self):
		for persona in self.personas:
			print (persona)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print ("La informacion del ficher externo es la siguiente: ")
		for p in self.personas:
			print (p)

miLista=ListaPersonas()
p=Persona("Diego", 14, "Masculino")
miLista.agregarPersonas(p)
miLista.guardarPersonasEnFicheroExterno()
miLista.mostrarInfoFicheroExterno()

