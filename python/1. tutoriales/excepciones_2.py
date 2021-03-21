def evaluaEdad(edad):
	if edad <0:
		raise TypeError("No se permiten edades negativas. ")

	elif edad<5:
		return "eres un bebito"

	elif edad<20:
		return "eres muy joven."

	elif edad<40:
		return "eres joven"

	elif edad<65:
		return "Eres maduro"

	elif edad <80:
		return "Ya tas viejito we :("

	elif edad <100:
		return "cuidate pls <3 "
		

print(evaluaEdad(float(input("Ingresa tu edad: "))))