from tkinter import *

raiz = Tk()

raiz.config(bg="skyblue")
raiz.config(bd=20)
raiz.config(relief="groove")
raiz.config(cursor="pirate")

miFrame=Frame(raiz, width=500, height=500)
miFrame.config(bg="gray")
miFrame.config(bd=15)
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")
miFrame.pack()

#------------------------------------------------------
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(justify="center")

LabelNombre=Label(miFrame, text="Nombre:", width= 7, height=1)
LabelNombre.config(bg="gray")
LabelNombre.config(bd=5)
LabelNombre.config(relief="groove")
LabelNombre.grid(row=0, column=0)

#-------------------------------------------------------------
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)
cuadroApellido.config(justify="center")

LabelApellido=Label(miFrame, text="Apellido:", width= 7, height=1)
LabelApellido.config(bg="gray")
LabelApellido.config(bd=5)
LabelApellido.config(relief="groove")
LabelApellido.grid(row=1, column=0)

#------------------------------------------------------------
cuadroCedula=Entry(miFrame)
cuadroCedula.grid(row=2, column=1)
cuadroCedula.config(justify="center")

LabelCedula=Label(miFrame, text="Cedula:", width= 7, height=1)
LabelCedula.config(bg="gray")
LabelCedula.config(bd=5)
LabelCedula.config(relief="groove")
LabelCedula.grid(row=2, column=0)

#--------------------------------------------------------------------
cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3, column=1)
cuadroPassword.config(justify="center", show="x")

LabelPassword=Label(miFrame, text="Password:", width= 7, height=1)
LabelPassword.config(bg="gray")
LabelPassword.config(bd=5)
LabelPassword.config(relief="groove")
LabelPassword.grid(row=3, column=0)




raiz.mainloop()