import tkinter as tk
import util.generic as utl

class VentanaLimite:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo = tk.Label(self.frame, text="Establer Límite Total", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=3)

        label_titulo = tk.Label(self.frame, text="Cantidad:", font=('Helvetica', 15), anchor="w")
        label_titulo.grid(row=1, column=0, pady=10, padx=5)

        self.cuadro_limite = tk.Entry(self.frame, font=('Helvetica', 14), width=30)
        self.cuadro_limite.grid(row=1, column=1, pady=10, padx=10)

        label_euros = tk.Label(self.frame, text="€uros", font=('Helvetica', 15), anchor="w")
        label_euros.grid(row=1, column=2, pady=10, padx=5)

        boton_ver_transacciones = tk.Button(self.frame, text="Aplicar Límite", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.realizarLimite)
        boton_ver_transacciones.grid(row=2, column=1,  padx=10, pady=10)
        boton_ver_transacciones.bind("<Return>", (lambda event: self.realizarLimite()))


    def realizarLimite(self):
        pass


