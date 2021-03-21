def generaPares(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+1

devuelvenumeros=generaPares(15)

print(devuelvenumeros)

print ("codigo...")

print(devuelvenumeros)

print ("codigo")

print (devuelvenumeros)