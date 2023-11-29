import tkinter as tk
from tkinter import ttk 

ventana = tk.Tk() #cera una ventana qu hereda todas las propiedades de la libreria
ventana.title("ejmplo de titulo") #tiutulo de la ventana

def funcion_click():
    accion.configure(text="*** hax dado click ***")
    etiqueta.configure(background="red", foreground="white")


etiqueta = tk.Label(ventana, text="hola a todos")
etiqueta.grid(column=0,row=0)



accion = ttk.Button(ventana, text = "jaz click aqui", command=funcion_click)
accion.grid(column=1,row=1)


ventana.mainloop()#con este se abre una ventana