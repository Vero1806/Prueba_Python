import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
class VentanaCategorias:
    def __init__(self):#, usuario: Usuario):
        self.ventana = tk.Tk()
        self.ventana.title('Ventana Categorias')
        self.ventana.geometry('800x600')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0) #No permite cambiar el tamaño de la ventana
        utl.centrar_ventana(self.ventana, 800, 600)



        self.ventana.mainloop()