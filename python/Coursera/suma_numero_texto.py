text = open ("assignament_1.txt")
text = text.read()
import re 
lista=[]
f = re.findall("[0-9]+",text)
for i in f:
	i = int(i)
	lista.append(i)
print (sum(lista))