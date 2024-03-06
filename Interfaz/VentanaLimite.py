import tkinter as tk
from tkinter import ttk
from capaIntermedia.Modelo import Modelo

class VentanaLimite:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo = tk.Label(self.frame, text="Establer Límite Por Categoría", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=3)

        label_titulo = tk.Label(self.frame, text="Cantidad", font=('Helvetica', 15), anchor="w")
        label_titulo.grid(row=1, column=0, pady=10, padx=5)

        label_titulo = tk.Label(self.frame, text="Categoría", font=('Helvetica', 15), anchor="w")
        label_titulo.grid(row=1, column=2, pady=10, padx=5)

        self.cuadro_limite = tk.Entry(self.frame, font=('Helvetica', 14), width=10)
        self.cuadro_limite.grid(row=2, column=0, pady=10, padx=10)

        label_euros = tk.Label(self.frame, text="€uros", font=('Helvetica', 15), anchor="w")
        label_euros.grid(row=2, column=1, pady=10, padx=5)

        self.seleccion = ttk.Combobox(self.frame, font=('Helvetica', 12), width=20)
        self.seleccion['values'] = Modelo().verCategoriasCompleto(usuario)
        self.seleccion.grid(row=2, column=2, padx=10, pady=10)

        boton_aplicarLimite = tk.Button(self.frame, text="Aplicar Límite", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.realizarLimite)
        boton_aplicarLimite.grid(row=2, column=3,  padx=10, pady=10)
        boton_aplicarLimite.bind("<Return>", (lambda event: self.realizarLimite()))


        label_titulo = tk.Label(self.frame, text="Tus Limites actuales", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=4, column=0, pady=10, padx=10, columnspan=3)

        tran = Modelo().ver_limite_categoria(usuario)
        for i, contenido in enumerate(tran):
            # Crear y agregar etiqueta al frame
            label_tran = tk.Label(self.frame, text=contenido, font=('Helvetica', 15), anchor="w")
            label_tran.grid(row=i+5, column=0, pady=10, padx=20, columnspan=3)

    def realizarLimite(self):
        pass
