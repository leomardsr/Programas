class miCarro():
	largo_chasis=250
	ancho_chasis=170
	ruedas=4
	enmarcha=False

	def arrancar(self,arrancamos):
		self.enmarcha=arrancamos

		if (self.enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.enmarcha and chequeo):
			return "El coche esta en marcha"

		elif (self.enmarcha and chequeo == False):
			return "Algo ha ido mal en el chequeo. No podemos arrancar"

		else:
			return "El coche esta parado."


	def estado(self):
		print ("El carro tiene un largo de ", self.largo_chasis, "cm. A su vez tiene un anco de ", self.ancho_chasis,
			"cm. Y también posee ", self.ruedas," Ruedas.")

	def __chequeo_interno(self):
		print ("Realizando chequeo interno.")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False


		sss
carro1=miCarro()

print(carro1.arrancar(True))

carro1.estado()

print("")
print("---------------------A continucacion creamos el segundo objeto-----------------")
print ("")

carro2=miCarro()

print (carro2.arrancar(True))

carro2.estado()

