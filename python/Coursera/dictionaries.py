cities = {"Merida " : " Merida"  ,  "Dto Capital "  :  " Caracas "  ,  "Delta Amacuro "  :  " Tucupita "}

print ("KEY   |   VALUES")
for a,b in cities.items(): #items es un metodo para dar claves y valores de los diccionarios 
	print (a,b)
print("------------------------Changing----------------")

print ("Keys:",list (cities.keys()))
# keys() es un metodo para mostrar las claves
# En este caso se almacena en una lista todas las claves del diccionario, y cada una ocupa una 
# posicion en la lista

print ("Values:",list (cities.values()))
# values() es un metodo para mostrar valores
# En este otro, se almacena en una lista todos los valores del diccionario
# y cada uno ocupa un espacio en la lista

print ("Items:",list (cities.items()))
# items() es un metodo para mostrar las Claves con sus respectivos valores
# Para este caso se almacena en una lista la clave con su respectivo valor
# y cada clave con su valor ocupa un espacio dentro de la lista

#Para mostrarlo contaremos los elementos que hay en esta ultima lista
print (len(list(cities.items())))