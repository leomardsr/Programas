print ("Bienvenido. Para hacer su registro rellene el formulario: ")
print ("")

class Personas():

	def Almacenamiento(self):
	
		self.nombre = ""
		self.apellido = ""
		self.cedula = ""
		self.telefono = ""
		self.correo = ""

	def Registro(self):
		nombre = input ( "Nombres: " )
		apellido = input ("Apellidos: ")
		cedula = input ("Cedula: ")
		telefono = input ("Telefono:")
		correo = input ("Correo: ")
		

	def Impresion(self):
		
		#print("Persona registrada: ")
		#print("")
		print ("Nombres: ", self.nombre, "\nApellidos: ", self.apellido, "\nCedula: ", self.cedula, "\nTelefono: ",
			self.telefono, "\nCorreo: ", self.correo)
		print("")


print("Persona #1: ")


persona1 = Personas()
Registro1 = Personas.Registro(persona1)

print ("Persona #1: ")
impresion1=Personas.Impresion(persona1)
