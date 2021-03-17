nombreUsuario=input("Introduce nombre de usuario: ")

print("El nombre en Mayusculas: ", nombreUsuario.upper())#La funcion upper convierte todas las letras en mayusculas
print()
print("El nombre en minusculas: ", nombreUsuario.lower()) #La funcion lower convierte todas las letras en minusculas
print()
print("El nombre es: ", nombreUsuario.capitalize()) #La funcion capitalizce convierte la primera letra en mayuscula
print()
print("----------------------------------------------------------------------------------------------")
print()
edad=input("Introduce la edad: ")
#devuelve un booleano True si solo hay numeros en lo escrito, y False si no.
while (edad.isdigit()==False):
	print("Por favor introduce un valor numerico")

	edad=input("Introduce la edad: ")
	
if (int(edad)<18):

	print("No puede pasar")

else:
	print("Puedes pasar.")