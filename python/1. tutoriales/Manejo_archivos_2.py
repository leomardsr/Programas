from io import open

archivo_texto=open("archivo.txt","r+") #Lectura y escritura

archivo_texto.seek( len(archivo_texto.readline()))

archivo_texto.write("Comienzo del texto")
