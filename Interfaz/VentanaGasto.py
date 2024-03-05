import tkinter as tk
from tkinter import ttk, messagebox

class VentanaGasto:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo = tk.Label(self.frame, text="Gasto", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=4)


        label_concepto = tk.Label(self.frame, text="Concepto: ", font=('Helvetica', 12), anchor="w")
        label_concepto.grid(row=1, column=1, pady=10, padx=10)

        label_cantidad = tk.Label(self.frame, text="Cantidad: ", font=('Helvetica', 12), anchor="w")
        label_cantidad.grid(row=1, column=2, pady=10, padx=10)

        label_titulo = tk.Label(self.frame, text="Nuevo Gasto: ", font=('Helvetica', 15), anchor="w")
        label_titulo.grid(row=2, column=0, pady=10, padx=10)

        self.cuadro_concepto = tk.Entry(self.frame, font=('Helvetica', 14), width=30)
        self.cuadro_concepto.grid(row=2, column=1, padx=10, pady=10)

        label_cantegoria = tk.Label(self.frame, text="Categoria: ", font=('Helvetica', 12), anchor="w")
        label_cantegoria.grid(row=1, column=3, pady=10, padx=10)


        self.cuadro_cantidad = tk.Entry(self.frame, font=('Helvetica', 14), width=30)
        self.cuadro_cantidad.grid(row=2, column=2, padx=10, pady=10)

        self.seleccion = ttk.Combobox(self.frame, values = ["Alimentación", "Hogar", "Ocio"]) #Modificar para meter el array de nobres de categorias
        self.seleccion.grid(row=2, column=3, padx=10, pady=10)

        self.boton_gasto = tk.Button(self.frame, text="Realizar Gasto", font=('Helvetical', 15), bg='red', bd=0, fg="#fff", command=self.realizarGasto)
        self.boton_gasto.grid(row=3, column=3, padx=10, pady=10)
        self.boton_gasto.bind("<Return>", (lambda event: self.realizarGasto()))


    def realizarGasto(self):
        pass