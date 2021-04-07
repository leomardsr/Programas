from tkinter import *

root= Tk()
root.title("GUI II")

miframe= Frame(root, width=500, height=400)
miframe.config(bg="gray")
miframe.config(bd=20)
miframe.config(relief="groove")
miframe.pack()

Label(miframe, text="Leomar Salazar", fg="blue", font=("Comic Sans MS", 18)).place(x=145, y= 160)

miImagen=PhotoImage(file="logo.png")
miLabel2=Label(miframe, image=miImagen) 
miLabel2.place(x=0, y=0)

root.mainloop()