from tkinter import *
from tkinter import messagebox

def saludar():
    print("Hola mundo tk")
    messagebox.showinfo("Title","hola "+txtNombre.get())
    
app = Tk()
app.title('Mi primera interfaz gráfica')
app.geometry('600x600')
frame = LabelFrame(app,text='Ventana')
frame.grid(row=0,column=0,columnspan=3,pady=10,padx=10)
#Etiqueta
lbNombre = Label(frame,text='Nombre : ')
lbNombre.grid(row=1,column=0)
#Caja de texto
txtNombre = Entry(frame)
txtNombre.grid(row=1,column=1)
#Boton
btnSaludo = Button(frame,text='Saludar',command=saludar)
btnSaludo.grid(row=1,column=2)
app.mainloop()