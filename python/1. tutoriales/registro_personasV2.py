print ("Bienvenido. Para hacer su registro rellene el formulario: ")
print ("")

class Personas():

	def Almacenamiento(self):
	
		nombre = ""
		apellido = ""
		cedula = ""
		telefono = ""
		correo = ""

	def Registro(self):
		nombre = input ( "Nombres: " )
		apellido = input ("Apellidos: ")
		cedula = input ("Cedula: ")
		telefono = input ("Telefono:")
		correo = input ("Correo: ")
		pass

	def Impresion(self):
		
		#print("Persona registrada: ")
		#print("")
		print ("Nombres: ", self.nombre, "\nApellidos: ", self.apellido, "\nCedula: ", self.cedula, "\nTelefono: ",
			self.telefono, "\nCorreo: ", self.correo)
		print("")


print("Persona #1: ")


persona1 = Personas()
#Registro1 = Personas.Registro(persona1)
persona1.nombre = input ( "Nombres: " )
persona1.apellido = input ("Apellidos: ")
persona1.cedula = input ("Cedula: ")
persona1.telefono = input ("Telefono: ")
persona1.correo = input ("Correo: ")

print("")
print("Persona #2: ")


persona2 = Personas()
persona2.nombre = input ( "Nombres: " )
persona2.apellido = input ("Apellidos: ")
persona2.cedula = input ("Cedula: ")
persona2.telefono = input ("Telefono: ")
persona2.correo = input ("Correo: ")

print("")
print("Persona #3: ")


persona3 = Personas()
persona3.nombre = input ( "Nombres: " )
persona3.apellido = input ("Apellidos: ")
persona3.cedula = input ("Cedula: ")
persona3.telefono = input ("Telefono: ")
persona3.correo = input ("Correo: ")

print("")
print("Persona #4: ")


persona4 = Personas()
persona4.nombre = input ( "Nombres: " )
persona4.apellido = input ("Apellidos: ")
persona4.cedula = input ("Cedula: ")
persona4.telefono = input ("Telefono: ")
persona4.correo = input ("Correo: ")

print("")
print("Persona #5: ")


persona5 = Personas()
persona5.nombre = input ( "Nombres: " )
persona5.apellido = input ("Apellidos: ")
persona5.cedula = input ("Cedula: ")
persona5.telefono = input ("Telefono: ")
persona5.correo = input ("Correo: ")






print ("")
print ("---------------------------------------------Personas registradas:----------------------------------------")
print ("")

print ("Persona #1: ")
impresion1=Personas.Impresion(persona1)

print("Persona #2: ")
impresion2=Personas.Impresion(persona2)

print("Persona #3: ")
impresion3=Personas.Impresion(persona3)

print("Persona #4: ")
impresion4=Personas.Impresion(persona4)

print("Persona #5: ")
impresion5=Personas.Impresion(persona5)


