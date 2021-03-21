palabra=input("Ingrese una palabra: ")
intento=0

while intento<1:

	contador=0

	if palabra=="done":
		break;

	for i in palabra:

		if i==" ":
			continue
		else:
			contador+=1

	print (" La cantidad de letras que tiene la palabra: '" + palabra + "' es: " + str(contador))
	print (" Si desea que el programa llegue a su final escriba 'done'.")

print("")

print("Cuenta Letras by: Leomar Salazar.")