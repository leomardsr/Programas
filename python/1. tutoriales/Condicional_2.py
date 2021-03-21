print ("Antes de ingresar a la institucion debe confirmar su edad")
edad = float (input ("Ingrese su Edad: "))
if edad < 18:
	print ("Lo siento, usted no puede acceder al establecimiento debido a su minoria de edad.")
elif edad > 100:
 	print ("lo siento, ha sobrepasado los limites reales. vuelva a intentarlo")
else:
	print ("Sea bienvenido, disfrute de su estadia.")
