def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		#for subElemento in elemento:
		yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid ", "Barcelona ", "Bilbao ","Valencia ")

#for i in ciudades_devueltas:
	#print (i)
print (next(ciudades_devueltas))
print (next(ciudades_devueltas))
print (next(ciudades_devueltas))
print (next(ciudades_devueltas))
