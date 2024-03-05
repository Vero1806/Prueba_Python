import tkinter as tk
from tkinter import ttk

class VentanaIngreso:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo = tk.Label(self.frame, text="Ingreso", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=3)

        label_concepto = tk.Label(self.frame, text="Concepto: ", font=('Helvetica', 12), anchor="w")
        label_concepto.grid(row=1, column=1, pady=10, padx=10)

        label_cantidad = tk.Label(self.frame, text="Cantidad: ", font=('Helvetica', 12), anchor="w")
        label_cantidad.grid(row=1, column=2, pady=10, padx=10)

        label_titulo = tk.Label(self.frame, text="Nuevo Ingreso: ", font=('Helvetica', 15), anchor="w")
        label_titulo.grid(row=2, column=0, pady=10, padx=10)

        self.cuadro_concepto = tk.Entry(self.frame, font=('Helvetica', 14), width=30)
        self.cuadro_concepto.grid(row=2, column=1, padx=10, pady=10)

        self.cuadro_cantidad = tk.Entry(self.frame, font=('Helvetica', 14), width=30)
        self.cuadro_cantidad.grid(row=2, column=2, padx=10, pady=10)

        self.boton_ingreso = tk.Button(self.frame, text="Realizar Ingreso", font=('Helvetical', 15), bg='#81ed2c', bd=0, fg="#fff", command=self.realizarIngreso)
        self.boton_ingreso.grid(row=3, column=2, padx=10, pady=10)
        self.boton_ingreso.bind("<Return>", (lambda event: self.realizarIngreso()))


    def realizarIngreso(self):
        pass