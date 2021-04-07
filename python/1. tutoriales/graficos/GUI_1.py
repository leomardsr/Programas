from tkinter import *

raiz = Tk()

raiz.title("Ventana de Prueba")

raiz.resizable(True, True)

raiz.iconbitmap("tecno.ico")

raiz.geometry("500x500")

raiz.config(bg="gray")

raiz.config(cursor="hand2")

raiz.config(relief="sunken")

raiz.config(bd="20")

miFrame=Frame()

miFrame.pack()

miFrame.config(bd=20)

miFrame.config(bg="skyblue") #color de fondo (background)

miFrame.config(width="490",height="490") #dos parametros: ancho y alto en pixeles

miFrame.config(relief="sunken")

miFrame.config(cursor="pirate")

raiz.mainloop() #esta instruccion debe estar siempre al final
