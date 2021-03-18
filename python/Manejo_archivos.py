from io import open

archivo_texto=open("archivo.txt","w")

frase=input("Introduce el texto a escribir: ")

archivo_texto.write(frase)

archivo_texto.close()

print()
print("----------------------------------CAMBIANDO A MODO LECTURA-----------------------------")

archivo_texto=open("archivo.txt","r")

print(archivo_texto.read())

archivo_texto.close()

