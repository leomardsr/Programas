edad=int(input("introduce tu edad por favor: "))

while edad < 1 or edad > 100:
	print("has introducido una edad incorrecta. Vuelve a intentarlo.")
	edad=int(input("introduce tu edad por favor: "))

print ("Gracias por colaborar, puedes pasar.")
print ("Edad del aspirante: " + str(edad))
