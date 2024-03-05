import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from capaIntermedia.Modelo import Modelo


class VentanaCategorias:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()


        label_titulo = tk.Label(self.frame, text="Tus Categorias: ", font=('Helvetica', 15), anchor="e")
        label_titulo.grid(row=0, column=0, pady=10, padx=10)
        cat = Modelo().vercategorias(usuario)
        for i, contenido in enumerate(cat):
            # Crear y agregar etiqueta al frame
            label_tran = tk.Label(self.frame, text=contenido, font=('Helvetica', 15), anchor="e")
            label_tran.grid(row=i+1, column=0, pady=10, padx=10)



        label_titulo = tk.Label(self.frame, text="Crear Categoría: ", font=('Helvetica', 15), anchor="w")
        label_titulo.grid(row=0, column=1, pady=10, padx=10)

        self.cuadro_texto = tk.Entry(self.frame, font=('Helvetica', 14), width=30)
        self.cuadro_texto.grid(row=0, column=2, padx=10, pady=10)


        boton_agregarCategoria = tk.Button(self.frame, text='Agregar Categoria', command=self.insertarcategoria, font=('Helvetica', 15), bg='#3a7ff6', fg='#fff')
        boton_agregarCategoria.grid(row=1, column=2, padx=10, pady=10)
        boton_agregarCategoria.bind("<Return>", (lambda event: self.insertarcategoria()))


    def insertarcategoria(self):
        categoria_escrita = self.cuadro_texto.get()
        categoria_comprobar = Modelo.selectcategorias(self.usuario)

        if categoria_comprobar:
            Modelo().insertcategorias(categoria_escrita,self.usuario)
            messagebox.showinfo(message="La categoría ha sido creada correctamente", title="Mensaje")
            self.ventana.destroy()

        else:
            messagebox.showinfo(message="La categoría ya existe en esta cuenta", title="Mensaje")