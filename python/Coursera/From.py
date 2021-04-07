file = open ("mbox-short.txt")
count = 0
lista = list()
for line in file:
	if line.startswith("From "):
		lista = line.split(" ")
		print (lista[1])
		count = count + 1

print ("There were ", count ," lines in the file with From as the first word ")