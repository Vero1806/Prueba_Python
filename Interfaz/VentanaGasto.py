import tkinter as tk
from tkinter import ttk, messagebox
from capaIntermedia.Modelo import Modelo

class VentanaGasto:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo= tk.Label(self.frame, text="Gasto", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=4)

        label_tituloPequeño= tk.Label(self.frame, text="Nuevo Gasto: ", font=('Helvetica', 15), anchor="w")
        label_tituloPequeño.grid(row=2, column=0, pady=10, padx=10)

        label_concepto = tk.Label(self.frame, text="Concepto: ", font=('Helvetica', 15), anchor="w")
        label_concepto.grid(row=1, column=1, pady=10, padx=10)

        label_cantidad = tk.Label(self.frame, text="Cantidad: ", font=('Helvetica', 15), anchor="w")
        label_cantidad.grid(row=1, column=2, pady=10, padx=10)

        label_cantegoria = tk.Label(self.frame, text="Categoria: ", font=('Helvetica', 15), anchor="w")
        label_cantegoria.grid(row=1, column=3, pady=10, padx=10)

        self.cuadro_concepto = tk.Entry(self.frame, font=('Helvetica', 12), width=20)
        self.cuadro_concepto.grid(row=2, column=1, padx=10, pady=10)

        self.cuadro_cantidad = tk.Entry(self.frame, font=('Helvetica', 12), width=20)
        self.cuadro_cantidad.grid(row=2, column=2, padx=10, pady=10)

        self.seleccion = ttk.Combobox(self.frame, font=('Helvetica', 12), width=20)
        self.seleccion['values'] = Modelo().verCategoriasCompleto(usuario)
        self.seleccion.grid(row=2, column=3, padx=10, pady=10)

        self.boton_gasto = tk.Button(self.frame, text="Realizar Gasto", font=('Helvetical', 15), bg='red', bd=0, fg="#fff", command=self.realizarGasto)
        self.boton_gasto.grid(row=3, column=3, padx=10, pady=10)
        self.boton_gasto.bind("<Return>", (lambda event: self.realizarGasto()))


    def realizarGasto(self):
        concepto = self.cuadro_concepto.get()
        cantidad = self.cuadro_cantidad.get()
        nombre_categoria = self.seleccion.get()
        idyNombre_categoria = nombre_categoria.split()
        
        gastoRealizado = Modelo().insertar_gasto_ingreso(self.usuario, idyNombre_categoria[0], concepto, -float(cantidad))

        if not gastoRealizado:
            messagebox.showinfo(message="Gasto realizada correctamente", title="Mensaje")
            self.ventana.destroy()
        else:
            messagebox.showinfo(message="Ha surgido un error al realizar el gasto", title="Mensaje")
    