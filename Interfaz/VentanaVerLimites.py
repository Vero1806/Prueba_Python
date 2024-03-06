import tkinter as tk

from capaIntermedia.Modelo import Modelo


class VentanaVerLimites:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo = tk.Label(self.frame, text="Tus Limites actuales", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=3)

        tran = Modelo().ver_limite_categoria(usuario)
        for i, contenido in enumerate(tran):
            # Crear y agregar etiqueta al frame
            label_tran = tk.Label(self.frame, text=contenido, font=('Helvetica', 15), anchor="center")
            label_tran.grid(row=i+1, pady=20, padx=20)
