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
