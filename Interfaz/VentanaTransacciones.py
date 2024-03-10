import tkinter as tk
import util.generic as utl
from baseDatos import usuario
from baseDatos.usuario import Usuario
from capaIntermedia.Modelo import Modelo

class VentanaTransacciones:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo = tk.Label(self.frame, text="Historial de Transacciones", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=3)

        tran = Modelo().vertransacciones(usuario)
        for i, elemento in enumerate(tran):
            if elemento[2] > 0.00:
            # Crear y agregar etiqueta al frame
                label_tran = tk.Label(self.frame, text=f"Categoria: {elemento[0]}, Concepto: {elemento[1]}, Cantidad: {elemento[2]}, fecha {elemento[3]}", font=('Helvetica', 15), fg="#006400", anchor="center")
                label_tran.grid(row=i+1, pady=20, padx=20)
            else:
                label_tran = tk.Label(self.frame, text=f"Categoria: {elemento[0]}, Concepto: {elemento[1]}, Cantidad: {elemento[2]}, fecha {elemento[3]}", font=('Helvetica', 15),fg="red", anchor="center")
                label_tran.grid(row=i+1, pady=20, padx=20)