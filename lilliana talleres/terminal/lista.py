import tkinter as tk
from tkinter import ttk 

ventana = tk.Tk()
ventana.title(text = "tirulo we")

numero = tk.StringVar()
seleccionar = ttk.Combobox(ventana, width=12,textvariable=numero)

seleccionar["values"]=(1,2,3,4,5,6,7,8,9)
seleccionar.grid(column=0,row=1)
ventana.mainloop()
