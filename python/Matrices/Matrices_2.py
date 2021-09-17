from random import * #random es para crear cualquier caracter, sea int float o str
filas = int(input("Numero de filas: ")) 
columnas = int(input("numero de columnas: "))
matriz = [[randint(1,30) for i in range(filas)] for c in range(columnas)]

for p in matriz:
	print (p)