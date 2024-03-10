import tkinter as tk
from tkinter import ttk, messagebox, END

from capaIntermedia.Modelo import Modelo

class VentanaGasto:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.i = 0
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo= tk.Label(self.frame, text="Gasto", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=6)

        label_tituloPequeño= tk.Label(self.frame, text="Nuevo Gasto: ", font=('Helvetica', 15), anchor="w")
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

        self.boton_gasto = tk.Button(self.frame, text='Realizar Gasto', font=('Helvetica', 15), bg='red', bd=0, fg='#fff', command=self.realizarGasto)
        self.boton_gasto.grid(row=3, column=5, padx=10, pady=10)
        self.boton_gasto.bind("<Return>", (lambda event: self.realizarGasto()))

        #calculadora
        self.boton7 = ttk.Button(self.frame, text="7", command=lambda:self.ingresarValores(7))
        self.boton7.grid(row=4, column=2, padx=5, pady=5)
        self.boton8 = ttk.Button(self.frame, text="8", command=lambda:self.ingresarValores(8))
        self.boton8.grid(row=4, column=3, padx=5, pady=5)
        self.boton9 = ttk.Button(self.frame, text="9", command=lambda:self.ingresarValores(9))
        self.boton9.grid(row=4, column=4, padx=5, pady=5)

        self.boton4 = ttk.Button(self.frame, text="4", command=lambda:self.ingresarValores(4))
        self.boton4.grid(row=5, column=2, padx=5, pady=5)
        self.boton5 = ttk.Button(self.frame, text="5", command=lambda:self.ingresarValores(5))
        self.boton5.grid(row=5, column=3, padx=5, pady=5)
        self.boton6 = ttk.Button(self.frame, text="6", command=lambda:self.ingresarValores(6))
        self.boton6.grid(row=5, column=4, padx=5, pady=5)

        self.boton1 = ttk.Button(self.frame, text="1", command=lambda:self.ingresarValores(1))
        self.boton1.grid(row=6, column=2, padx=5, pady=5)
        self.boton2 = ttk.Button(self.frame, text="2", command=lambda:self.ingresarValores(2))
        self.boton2.grid(row=6, column=3, padx=5, pady=5)
        self.boton3 = ttk.Button(self.frame, text="3", command=lambda:self.ingresarValores(3))
        self.boton3.grid(row=6, column=4, padx=5, pady=5)

        self.botonPunto = ttk.Button(self.frame, text=".", command=lambda:self.ingresarValores("."))
        self.botonPunto.grid(row=7, column=2, padx=5, pady=5)
        self.boton0 = ttk.Button(self.frame, text="0", command=lambda:self.ingresarValores(0))
        self.boton0.grid(row=7, column=3, padx=5, pady=5)
        self.botonBorrar = ttk.Button(self.frame, text=chr(9003), command=self.borrarUltimoNumero)
        self.botonBorrar.grid(row=7, column=4, padx=5, pady=5)

        self.rowVacia = tk.Label(self.frame, text=" ")
        self.rowVacia.grid(row=8, column=0, pady=10, padx=10, columnspan=6)

    def realizarGasto(self):
        concepto = self.cuadro_concepto.get()
        cantidad = self.cuadro_cantidad.get()
        nombre_categoria = self.seleccion.get()
        idyNombre_categoria = nombre_categoria.split()
        categorias_suma_limtes = Modelo().gestionar_categoria_gasto_limite(self.usuario)
        listaNombreCategoria = []
        listaSuma = []
        listaLiminte = []
        for i, contenido in enumerate(categorias_suma_limtes):
            listaNombreCategoria.append(contenido[0])
            listaSuma.append(contenido[1])
            listaLiminte.append(contenido[2])

        if idyNombre_categoria[1] in listaNombreCategoria:
            indice = listaNombreCategoria.index(idyNombre_categoria[1])
            if (float(listaSuma[indice])+float(cantidad)) > listaLiminte[indice]:
                pregutarGastoSuperado = messagebox.askyesno(title="Mensaje", message=f"Has superado tu límite de {listaNombreCategoria[indice]}. ¿Desea hacer el gasto de todos modos?")
                if pregutarGastoSuperado:
                    gastoRealizado = Modelo().insertar_transaccion(self.usuario, idyNombre_categoria[0], concepto, -float(cantidad))
                    if not gastoRealizado:
                        messagebox.showinfo(message="Gasto realizado correctamente", title="Mensaje")
                        self.ventana.destroy()
                    else:
                        messagebox.showinfo(message="Ha surgido un error al realizar el gasto", title="Mensaje")
                else:
                    messagebox.showinfo(message="El gasto no ha sido registrado", title="Mensaje")
            else:
                gastoRealizado = Modelo().insertar_transaccion(self.usuario, idyNombre_categoria[0], concepto, -float(cantidad))

                if not gastoRealizado:
                    messagebox.showinfo(message="Gasto realizado correctamente", title="Mensaje")
                    self.ventana.destroy()
                else:
                    messagebox.showinfo(message="Ha surgido un error al realizar el gasto", title="Mensaje")
        else:
            gastoRealizado = Modelo().insertar_transaccion(self.usuario, idyNombre_categoria[0], concepto, -float(cantidad))

            if not gastoRealizado:
                messagebox.showinfo(message="Gasto realizado correctamente", title="Mensaje")
                self.ventana.destroy()
            else:
                messagebox.showinfo(message="Ha surgido un error al realizar el gasto", title="Mensaje")

    def ingresarValores(self, tecla):
        self.cuadro_cantidad.insert(self.i, tecla)
        self.i += 1

    def borrarUltimoNumero(self):
        cuadradoCantidadEstado = self.cuadro_cantidad.get()
        if len(cuadradoCantidadEstado) > 0:
            cuadradoCantidadNuevoEstado = cuadradoCantidadEstado[:-1]
            self.cuadro_cantidad.delete(0, END)
            self.cuadro_cantidad.insert(0, cuadradoCantidadNuevoEstado)