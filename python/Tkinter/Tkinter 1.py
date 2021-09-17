from tkinter import *

root = Tk() #Creamos un objeto de Tk

texto = Label(root, text="Hola mundo") #Asignamos a una variable la etiqueta (label) y como parámetros introducimos
# -donde va a esta ubicada (en que objeto) y y para el segundo introducimos el contenido, en este caso texto

texto.pack() # Va a posicionar nuestra etiqueta en una posición específica

root.mainloop() #Es para crear un bucle donde se muestre permanentemente la ventana de la interfaz
