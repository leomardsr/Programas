#para crear listas se pone el nombre, al cual se le asignan valores, las listas en vez
#de utilizar parentesis utilizan corchetes
lista = ["yo", "diego", "mama", "papa"]

lista.append("tia")#para agregar en la ultima posicion de la lista un nuevo miembro

lista.insert(0,"prima") #para ingresar miembros en lugares especificos

lista.extend(["leo", "luis"]) #para incluir varios elementos... (concatenar listas)

lista.remove("leo")#para eliminar elementos de la lista, s puede nombrar el elemento, y tambien su posicion

lista.pop()#elimina el ultimo elemento incluido en la lista

print (lista.index("yo")) #para saber el indice de el elemento de la lista

print ("yo" in lista)#dice si el elemento se encuentra en la lista (solo con verdadero o falso)

print (lista[:])

notas = [True, False, 5, "20"] 

lista_total = lista+notas #para sumar listas

print (lista_total[:])