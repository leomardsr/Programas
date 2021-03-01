def generapares(limite):

	num=1

	miLista=[]

	while num<limite:

		miLista.append(num*2) 

		num=+1

	return miLista

# Limite=int(input("Intruduce la cantidad de numeros pares que deseas mostrar: "))
print(generapares(10))