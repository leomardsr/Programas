#import funciones_matematicas #Cuando se utiliza el import debemos utilizar la numenclatura del punto para poder utilizar las funciones del modulo
							  #Es decir: para poder utilizar "sumar" funciones_matematicas.sumar(x,x)

from funciones_matematicas import * #Podemos importar una sola funcion para poderla utilizar sin ningun tipo de restriccion
									#Para poder utilizar todas las funciones de otro modulo escribimos el "*" asterizco para poder utilizarlos todos
									#Sin embargo si el modulo es muy grande el tamaño que ocuparia en memoria RAM seria bastante grande

sumar(7,5)

restar(7,5)

multiplicar(7,5)