class Persona():
	def __init__(self, nombre, edad, residencia):
		self.nombre = nombre
		self.edad = edad
		self.residencia = residencia

	def descripcion(self):
		print ("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.residencia)

class Empleado(Persona):

	def __init__ (self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):

		super().descripcion() # La funcion super() hace que podamos utilizar métodos de la super clase

		print ("Salario: ", self.salario,"Antiguedad: ", self.antiguedad)

Leomar=Empleado(0,0,"Leomar", 17, "Merida")

Leomar.descripcion()

print(isinstance(Leomar, Persona)) # La funcion insinstance() Verifica que una instancia (Posicion 1 del parentesis)
								   #pertenezca a una clase (Posicion 2 del parentesis)



