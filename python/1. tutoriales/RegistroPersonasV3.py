print ("Bienvenido. Para hacer su registro rellene el formulario: ")
print ("")

class Personas():
	nombre = ""
	apellido = ""
	cedula = ""
	telefono = ""
	correo = ""

	def Registro(self):
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



persona1=Personas()
persona1.Registro()


persona2=Personas()
persona2.Registro()


persona3=Personas()
persona3.Registro()


persona4=Personas()
persona4.Registro()


persona5=Personas()
persona5.Registro()

persona1.Impresion()
persona2.Impresion()
persona3.Impresion()
persona4.Impresion()
persona5.Impresion()

