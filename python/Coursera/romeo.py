fileOpen=open("romeo.txt","r")
text=fileOpen.read()
lista_Palabras = text.split()
lista = list()

for line in lista_Palabras:
	if line in lista:
		continue
	lista.append(line)

lista.sort()

print (lista)

