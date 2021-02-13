print ("Evaluacion de notas")
nota_alumno=input("ingrese la nota del estudiante: ")
def evaluacion(nota):
	valoracion="aprovado"
	if nota < 5:
		valoracion="Reprovado"
	return valoracion

print (evaluacion(int(nota_alumno)))