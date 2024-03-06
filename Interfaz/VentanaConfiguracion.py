import tkinter as tk
from tkinter import messagebox

class VentanaConfiguracion:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        label_titulo = tk.Label(self.frame, text="Configuración", font=('Helvetica', 20), anchor="w")
        label_titulo.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        label_nombre = tk.Label(self.frame, text="Nombre Usuario:", font=('Helvetica', 12), anchor="w")
        label_nombre.grid(row=1, column=0, pady=10, padx=10)

        label_escribeNombre = tk.Label(self.frame, text=f"{usuario.nombre} {usuario.apellidos}", font=('Helvetica', 12), anchor="w")
        label_escribeNombre.grid(row=1, column=1, pady=10, padx=10)

        label_tituloContra = tk.Label(self.frame, text="Cambiar Contraseña", font=('Helvetica', 15), anchor="w")
        label_tituloContra.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

        label_ContraActual = tk.Label(self.frame, text="Contraseña Actual: ", font=('Helvetica', 12), anchor="w")
        label_ContraActual.grid(row=3, column=0, pady=10, padx=0)

        label_ContraNueva = tk.Label(self.frame, text="Nueva Contraseña: ", font=('Helvetica', 12), anchor="w")
        label_ContraNueva.grid(row=4, column=0, pady=10, padx=0)

        label_ContraNueva2 = tk.Label(self.frame, text="Repetir Nueva Contraseña: ", font=('Helvetica', 12), anchor="w")
        label_ContraNueva2.grid(row=5, column=0, pady=10, padx=0)

        self.cuadro_ContraActual = tk.Entry(self.frame, font=('Helvetica', 12), width=20)
        self.cuadro_ContraActual.grid(row=3, column=1, padx=0, pady=10)
        self.cuadro_ContraActual.config(show="*")

        self.cuadro_ContraNueva = tk.Entry(self.frame, font=('Helvetica', 12), width=20)
        self.cuadro_ContraNueva.grid(row=4, column=1, padx=0, pady=10)
        self.cuadro_ContraNueva.config(show="*")

        self.cuadro_ContraNueva2 = tk.Entry(self.frame, font=('Helvetica', 12), width=20)
        self.cuadro_ContraNueva2.grid(row=5, column=1, padx=0, pady=10, columnspan=2)
        self.cuadro_ContraNueva2.config(show="*")

        boton_contrasenna = tk.Button(self.frame, text="Actualizar Contraseña", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.cambiarContrasenna)
        boton_contrasenna.grid(row=6, column=0, padx=10, pady=10)
        boton_contrasenna.bind("<Return>", (lambda event: self.cambiarContrasenna()))

        #boton_reiniciar = tk.Button(self.frame, text="Cerrar Sesión", font=('Times', 15), bg='#808080', bd=0, fg="#fff", command=self.reiniciar)
        #boton_reiniciar.grid(row=5, column=2, padx=10, pady=10)
        #boton_reiniciar.bind("<Return>", (lambda event: self.reiniciar()))

    def cambiarContrasenna(self):
        ContraActual = self.cuadro_ContraActual.get()
        ContraNueva = self.cuadro_ContraNueva.get()
        ContraNueva2 = self.cuadro_ContraNueva2.get()

        if ContraActual != self.usuario.contrasenna:
            messagebox.showinfo(message="La contraseña actual no es correcta", title="Mensaje")
        else:
            if ContraActual == ContraNueva:
                messagebox.showinfo(message="La contraseña actual coincide con la nueva contraseña", title="Mensaje")
            elif ContraNueva != ContraNueva2:
                messagebox.showinfo(message="La nueva contraseña no coincide", title="Mensaje")
            else:
                pass


    #def reiniciar(self):
        #messagebox.showinfo(message="Hasta la próxima", title="Mensaje")
        #self.ventana.destroy()
        #No funciona por la forma de trabajar de Tkinter así que esto cierra la app
        #from main import VentanaLogin
        #VentanaLogin()

