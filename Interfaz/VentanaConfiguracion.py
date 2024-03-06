import tkinter as tk
import util.generic as utl

class VentanaConfiguracion:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_nombre = tk.Label(self.frame, text="Configuración", font=('Helvetica', 20), anchor="w")
        label_nombre.grid(row=0, column=0, pady=10, padx=10, columnspan= 2)

        label_nombre = tk.Label(self.frame, text="Nombre Usuario:", font=('Helvetica', 12), anchor="w")
        label_nombre.grid(row=1, column=0, pady=10, padx=10)

        label_escribeNombre = tk.Label(self.frame, text=f"{usuario.nombre} {usuario.apellidos}", font=('Helvetica', 12), anchor="w")
        label_escribeNombre.grid(row=1, column=1, pady=10, padx=10)

        boton_contrasenna = tk.Button(self.frame, text="Cambiar Contraseña", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.cambiarContrasenna)
        boton_contrasenna.grid(row=2, column=0, padx=10, pady=10)
        boton_contrasenna.bind("<Return>", (lambda event: self.cambiarContrasenna()))

        boton_reiniciar = tk.Button(self.frame, text="Cerrar Sesión", font=('Times', 15), bg='#808080', bd=0, fg="#fff", command=self.reiniciar)
        boton_reiniciar.grid(row=2, column=1, padx=10, pady=10)
        boton_reiniciar.bind("<Return>", (lambda event: self.reiniciar()))

    def cambiarContrasenna(self):
        pass
    def reiniciar(self):
        self.ventana.destroy()

        #from main import VentanaLogin
        #VentanaLogin()

