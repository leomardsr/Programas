import pickle

class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ", self.enmarcha,
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


coche1=Vehiculos("Ford", "Laser")
coche2= Vehiculos("Fiat", "uno")
coche3=Vehiculos("Tesla", "Model 3")

coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb") #"wb" Significa escritura en codigo binario ("Write Binary")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

print ("FICHERO GUARDADO\n")
print ("Cargando archivo...\n")

fichero_apertura = open ("losCoches", "rb") #"rb" significa lectura de bytes/binaria ("read binary")

misCoches = pickle.load(fichero_apertura)

fichero_apertura.close()

for i in misCoches:
	print(i.estado())


