class miCarro():
	largo_chasis=250
	ancho_chasis=170
	ruedas=4
	enmarcha=False

	def arrancar(self,arrancamos):
		self.enmarcha=arrancamos

		if(self.enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado."


	def estado(self):
		print ("El carro tiene un largo de ", self.largo_chasis, "cm. A su vez tiene un anco de ", self.ancho_chasis,
			"cm. Y también posee ", self.ruedas," Ruedas.")
		
carro1=miCarro()

#print ("El largo de mi carro es de ", carro1.largo_chasis)
#print ("El Carro tiene ", carro1.ruedas, " Ruedas")
print(carro1.arrancar(True))

carro1.estado()

print("")
print("---------------------A continucacion creamos el segundo objeto-----------------")
print ("")

carro2=miCarro()

#print ("El Largo de mi carro 2 es de ", carro2.largo_chasis)
#print ("El carro 2 tiene ", carro2.ruedas, " ruedas")
print (carro2.arrancar(False))
carro2.estado()

