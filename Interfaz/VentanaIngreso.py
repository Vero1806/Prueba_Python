import tkinter as tk
from tkinter import ttk, messagebox

from capaIntermedia.Modelo import Modelo


class VentanaIngreso:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo= tk.Label(self.frame, text="Ingreso", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=6)

        label_tituloPequeño= tk.Label(self.frame, text="Nuevo Ingreso: ", font=('Helvetica', 15), anchor="w")
        label_tituloPequeño.grid(row=2, column=0, pady=10, padx=10)

        label_concepto = tk.Label(self.frame, text="Concepto: ", font=('Helvetica', 15), anchor="w")
        label_concepto.grid(row=1, column=1, pady=10, padx=10)

        label_cantidad = tk.Label(self.frame, text="Cantidad: ", font=('Helvetica', 15), anchor="w")
        label_cantidad.grid(row=1, column=2, pady=10, padx=10, columnspan=3)

        label_cantegoria = tk.Label(self.frame, text="Categoria: ", font=('Helvetica', 15), anchor="w")
        label_cantegoria.grid(row=1, column=5, pady=10, padx=10)

        self.cuadro_concepto = tk.Entry(self.frame, font=('Helvetica', 12), width=20)
        self.cuadro_concepto.grid(row=2, column=1, padx=10, pady=10)

        self.cuadro_cantidad = tk.Entry(self.frame, font=('Helvetica', 12), width=20)
        self.cuadro_cantidad.grid(row=2, column=2, padx=10, pady=10, columnspan=3)

        self.seleccion = ttk.Combobox(self.frame, font=('Helvetica', 12), width=20)
        self.seleccion['values'] = Modelo().verCategoriasCompleto(usuario)
        self.seleccion.grid(row=2, column=5, padx=10, pady=10)

        self.boton_ingreso = tk.Button(self.frame, text='Realizar Ingreso', font=('Helvetica', 15), bg='#006400', fg='#fff', bd=0, command=self.realizarIngreso)
        self.boton_ingreso.grid(row=3, column=5, padx=10, pady=10)
        self.boton_ingreso.bind("<Return>", (lambda event: self.realizarIngreso()))

        #calculadora
        boton7 = ttk.Button(self.frame, text="7")
        boton7.grid(row=4, column=2, padx=5, pady=5)
        boton8 = ttk.Button(self.frame, text="8")
        boton8.grid(row=4, column=3, padx=5, pady=5)
        boton9 = ttk.Button(self.frame, text="9")
        boton9.grid(row=4, column=4, padx=5, pady=5)
        boton4 = ttk.Button(self.frame, text="4")
        boton4.grid(row=5, column=2, padx=5, pady=5)
        boton5 = ttk.Button(self.frame, text="5")
        boton5.grid(row=5, column=3, padx=5, pady=5)
        boton6 = ttk.Button(self.frame, text="6")
        boton6.grid(row=5, column=4, padx=5, pady=5)
        boton1 = ttk.Button(self.frame, text="1")
        boton1.grid(row=6, column=2, padx=5, pady=5)
        boton2 = ttk.Button(self.frame, text="2")
        boton2.grid(row=6, column=3, padx=5, pady=5)
        boton3 = ttk.Button(self.frame, text="3")
        boton3.grid(row=6, column=4, padx=5, pady=5)
        botonPunto = ttk.Button(self.frame, text=".")
        botonPunto.grid(row=7, column=2, padx=5, pady=5)
        boton0 = ttk.Button(self.frame, text="0")
        boton0.grid(row=7, column=3, padx=5, pady=5)
        botonBorrar = ttk.Button(self.frame, text=chr(9003))
        botonBorrar.grid(row=7, column=4, padx=5, pady=5)

        rowVacia = tk.Label(self.frame, text=" ")
        rowVacia.grid(row=8, column=0, pady=10, padx=10, columnspan=6)

    def realizarIngreso(self):
        concepto = self.cuadro_concepto.get()
        cantidad = self.cuadro_cantidad.get()
        nombre_categoria = self.seleccion.get()
        idyNombre_categoria = nombre_categoria.split()

        gastoRealizado = Modelo().insertar_transaccion(self.usuario, idyNombre_categoria[0], concepto, float(cantidad))

        if not gastoRealizado:
            messagebox.showinfo(message="Ingreso realizado correctamente", title="Mensaje")
            self.ventana.destroy()
        else:
            messagebox.showinfo(message="Ha surgido un error al realizar el ingreso", title="Mensaje")