import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def seleccion(seleccionar):
	print (seleccionar)

ttk.Button(root, text = "Python", command = lambda: seleccion("Python")).pack()
ttk.Button(root, text = "JavaScript", command = lambda: seleccion("JavaScript")).pack()
ttk.Button(root, text = "C++", command = lambda: seleccion("C++")).pack()

root.mainloop()