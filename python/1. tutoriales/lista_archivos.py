archive=open("listas.txt", "r+")

mylist=["2","3","4","5","6","7","8","9"]

for i in mylist:

	archive.write(i)

archive.seek(0)

print (archive.read())

archive.close()

