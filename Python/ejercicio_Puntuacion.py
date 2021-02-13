print ("ingrese la puntuacion a evaluar ( del 0.0 al 1.0 ) : ")

puntuacion = float(input())

if puntuacion < 0 or puntuacion > 1:
	print ("Puntuacion incorrecta. ")

elif puntuacion >= 0.9:
	print ("A")

elif puntuacion >= 0.8:
	print ("B")

elif puntuacion >= 0.7:
	print ("C")

elif puntuacion >= 0.6:
	print ("D")

else:
	print ("F")