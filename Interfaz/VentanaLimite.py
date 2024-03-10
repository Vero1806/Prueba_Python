import tkinter as tk
from tkinter import ttk, messagebox, END
from tkinter.messagebox import YESNO

from baseDatos import usuario
from baseDatos.categorias import Categoria
from capaIntermedia.Modelo import Modelo

class VentanaLimite:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.i = 0
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo = tk.Label(self.frame, text="Establer Límite Por Categoría", font=('Helvetica', 20), anchor="center")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=5)

        label_titulo = tk.Label(self.frame, text="Cantidad", font=('Helvetica', 15), anchor="w")
        label_titulo.grid(row=1, column=0, pady=10, padx=5, columnspan=2)

        label_titulo = tk.Label(self.frame, text="Categoría", font=('Helvetica', 15), anchor="w")
        label_titulo.grid(row=1, column=2, pady=10, padx=5)

        self.cuadro_limite = tk.Entry(self.frame, font=('Helvetica', 14), width=15)
        self.cuadro_limite.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

        label_euros = tk.Label(self.frame, text="€uros", font=('Helvetica', 15), anchor="w")
        label_euros.grid(row=2, column=2, pady=10, padx=5)

        self.seleccion = ttk.Combobox(self.frame, font=('Helvetica', 12), width=20)
        self.seleccion['values'] = Modelo().verCategoriasCompleto(usuario)
        self.seleccion.grid(row=2, column=3, padx=10, pady=10)

        boton_aplicarLimite = tk.Button(self.frame, text='Crear Límite', font=('Helvetica', 15), bg='#3a7ff6', fg='#fff', bd=0, command=self.realizarLimite)
        boton_aplicarLimite.grid(row=2, column=4,  padx=10, pady=10)
        boton_aplicarLimite.bind("<Return>", (lambda event: self.realizarLimite()))

        label_titulo = tk.Label(self.frame, text="Tus Limites actuales", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=4, column=3, pady=5, padx=10, columnspan=2)

        tran = Modelo().ver_limite_categoria(usuario)
        for i, contenido in enumerate(tran):
            # Crear y agregar etiqueta al frame
            label_tran = tk.Label(self.frame, text=contenido, font=('Helvetica', 15), anchor="w")
            label_tran.grid(row=i+5, column=3, pady=5, padx=20, columnspan=2)

        #calculadora
        self.boton7 = ttk.Button(self.frame, text="7", command=lambda:self.ingresarValores(7))
        self.boton7.grid(row=4, column=0, padx=5, pady=5)
        self.boton8 = ttk.Button(self.frame, text="8", command=lambda:self.ingresarValores(8))
        self.boton8.grid(row=4, column=1, padx=5, pady=5)
        self.boton9 = ttk.Button(self.frame, text="9", command=lambda:self.ingresarValores(9))
        self.boton9.grid(row=4, column=2, padx=5, pady=5)

        self.boton4 = ttk.Button(self.frame, text="4", command=lambda:self.ingresarValores(4))
        self.boton4.grid(row=5, column=0, padx=5, pady=5)
        self.boton5 = ttk.Button(self.frame, text="5", command=lambda:self.ingresarValores(5))
        self.boton5.grid(row=5, column=1, padx=5, pady=5)
        self.boton6 = ttk.Button(self.frame, text="6", command=lambda:self.ingresarValores(6))
        self.boton6.grid(row=5, column=2, padx=5, pady=5)

        self.boton1 = ttk.Button(self.frame, text="1", command=lambda:self.ingresarValores(1))
        self.boton1.grid(row=6, column=0, padx=5, pady=5)
        self.boton2 = ttk.Button(self.frame, text="2", command=lambda:self.ingresarValores(2))
        self.boton2.grid(row=6, column=1, padx=5, pady=5)
        self.boton3 = ttk.Button(self.frame, text="3", command=lambda:self.ingresarValores(3))
        self.boton3.grid(row=6, column=2, padx=5, pady=5)

        self.botonPunto = ttk.Button(self.frame, text=".", command=lambda:self.ingresarValores("."))
        self.botonPunto.grid(row=7, column=0, padx=5, pady=5)
        self.boton0 = ttk.Button(self.frame, text="0", command=lambda:self.ingresarValores(0))
        self.boton0.grid(row=7, column=1, padx=5, pady=5)
        self.botonBorrar = ttk.Button(self.frame, text=chr(9003), command=self.borrarUltimoNumero)
        self.botonBorrar.grid(row=7, column=2, padx=5, pady=5)

        #self.rowVacia = tk.Label(self.frame, text=" ")
         #self.rowVacia.grid(row=8, column=0, pady=10, padx=10, columnspan=6)


    def realizarLimite(self):
        cantidadLimite = float(self.cuadro_limite.get())

        categoria = self.seleccion.get()
        idyNombre_categoria = categoria.split()
        comprobarId = int(idyNombre_categoria[0])

        idcategorias_del_usuario = Modelo().ver_limite_idcategoria(self.usuario)

        if not comprobarId in idcategorias_del_usuario:
            crearLimite = Modelo().insertar_limite(self.usuario, cantidadLimite, idyNombre_categoria[0])

            if not crearLimite:
                messagebox.showinfo(message="Límite creado correctamente", title="Mensaje")
                self.ventana.destroy()
            else:
                messagebox.showinfo(message="Ha surgido un error al crear el límite", title="Mensaje")

        else:
            pregutarActualizar = messagebox.askyesno(title="Mensaje de actualización", message="Ya tiene un limite creado para esta categoría. ¿Desea actualizarlo?")
            if pregutarActualizar:
                actualizarLimite = Modelo().actualizar_limite(self.usuario, cantidadLimite, idyNombre_categoria[0])

                if not actualizarLimite:
                    messagebox.showinfo(message="Límite actualizado correctamente", title="Mensaje")
                    self.ventana.destroy()
                else:
                    messagebox.showinfo(message="Ha surgido un error al actualizar el límite", title="Mensaje")

    def ingresarValores(self, tecla):
        self.cuadro_limite.insert(self.i, tecla)
        self.i += 1

    def borrarUltimoNumero(self):
        cuadradoEstado = self.cuadro_limite.get()
        if len(cuadradoEstado) > 0:
            cuadradoNuevoEstado = cuadradoEstado[:-1]
            self.cuadro_limite.delete(0, END)
            self.cuadro_limite.insert(0, cuadradoNuevoEstado)