#para este 4to ejercicio veremos el "in" como condicional para evaluar varias opciones al mismo tiempo, podiendo cumplirse una de todas ellas.
#a demas 2 funciones: "upper()" la cual transforma el texto ingresado por teclado a mayusculas
#y "lower()" que transforma el texto ingresado por teclado a minusculas.
print ("Cursos Online Leogo")
print ("¿Cual de estos cursos gustaria realizar:?")

print ("Diseño de paginas web")
print ("Mantenimiento de celulares")
print ("Programacion C++")
print ("Programacion Python")

opcion_elejida = input()

curso = opcion_elejida.lower()

if curso in ("diseño de paginas web", "mantenimiento de celulares", "programacion c++", "programacion python"):
	print ("Curso a realizar: " + curso )

else:
	print ("Curso no contemplado.")