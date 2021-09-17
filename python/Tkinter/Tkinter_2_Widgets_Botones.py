from tkinter import *

root = Tk()

root.title("Mi primera ventana wee") #con el metodo "title" agregamos el título a la ventana
root.geometry("300x100") #Con el metodo "geometry" asignamos tamaño específico a la ventana (desde un inicio) en pixeles

etiqueta = Label(root, text = " Practicing with Tkinter ") #Etiqueta con su respectivo texto
boton1 = Button(root, text = "Minimizar", command = root.iconify, bg ="green") # Este comando es para minimizar la ventana cuando se presione el boton
#para mostrar el boton es necesario utilizar el metodo "pack"
#Podemos ubicar los botones con el punto pack con "side" = left/right/center
etiqueta.pack()
boton1.pack(side=LEFT)

def imprimir():
	etiqueta1 = Label(root, text = "Suscrito")
	etiqueta1.pack()

boton2 = Button(root, text = "Suscribirse", command = imprimir, bg = "red")
boton2.pack(side=RIGHT)

root.mainloop()
