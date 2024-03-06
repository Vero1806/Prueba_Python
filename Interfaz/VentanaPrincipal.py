import tkinter as tk
from tkinter import messagebox

import util.generic as utl
from Interfaz.VentanaIngreso import VentanaIngreso
from Interfaz.VentanaLimite import VentanaLimite
from Interfaz.VentanaTransacciones import VentanaTransacciones
from Interfaz.VentanaCategorias import VentanaCategorias
from Interfaz.VentanaConfiguracion import VentanaConfiguracion
from Interfaz.VentanaGasto import VentanaGasto
from baseDatos.usuario import Usuario
from capaIntermedia.Modelo import Modelo


class VentanaPrincipal:
    def __init__(self, ventana, usuario: Usuario):
        self.ventana = ventana
        self.ventana.title('ECO-GASTOS')
        self.ventana.geometry('800x600')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0) #No permite cambiar el tamaño de la ventana
        utl.centrar_ventana(self.ventana, 700, 500)
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=5)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(2, weight=3)
        self.ventana.grid_rowconfigure(3, weight=3)

        self.usuario = usuario

        self.logo = utl.leer_imagen("./util/logoBlanco.png", (100, 100))

        # frame_logo 0,0
        frame_logo = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_logo.grid(row=0, column=0, pady=10, padx=10)  # Utilizando grid y sticky para alinear al norte KOTLIN
        # Label para el logo
        label_logo = tk.Label(frame_logo, image=self.logo, bg='#fcfcfc', anchor="center")
        label_logo.grid(row=0, column=0,  pady=10, padx=10)

        label = tk.Label(frame_logo, text="ECO-GASTOS", font=('Times', 15, 'bold'), fg="#175183", bg='#fcfcfc', anchor="center")
        label.grid(row=1, column=0, pady=10, padx=10)

        # frame_titulo 0,1
        frame_titulo = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_titulo.grid(row=0, column=1, pady=20, padx=20)
        # Label para el texto de bienvenida (Título)
        label_titulo = tk.Label(frame_titulo, text=f"{self.usuario.nombre}", font=('Helvetica', 20), bg='#fcfcfc', anchor="center")
        label_titulo.grid(row=0, column=1, pady=20, padx=20)

        #frame_configuracion 0,2
        frame_configuracion = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_configuracion.grid(row=0, column=2, padx=10, pady=10)
        #boton_configuración
        boton_configuracion = tk.Button(frame_configuracion, text="Configuración", font=('Times', 18), bg='#808080', bd=0, fg="#fff", command=self.configuracion)
        boton_configuracion.pack(fill=tk.X, padx=10, pady=10)
        boton_configuracion.bind("<Return>", (lambda event: self.configuracion()))

        #frame_saldo 1,1
        frame_saldo = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_saldo.grid(row=1, column=1, padx=10, pady=10)
        # Label saldo
        label_saldo = tk.Label(frame_saldo, text=f"Saldo actual: {self.usuario.saldo}€", font=('Helvetica', 15), bg='#fcfcfc', anchor="n")
        label_saldo.grid(row=1, column=1, pady=10, padx=10)

        #frame_limite 2,0
        frame_establecer_límite = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_establecer_límite.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        # boton_limite
        boton_establecer_limite = tk.Button(frame_establecer_límite, text="Establecer Límite", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.establecerLiminte)
        boton_establecer_limite.pack(fill=tk.X, padx=10, pady=10)
        boton_establecer_limite.bind("<Return>", (lambda event: self.establecerLiminte()))

        #frame_refrescar 2,1
        frame_refrescar = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_refrescar.grid(row=2, column=1, padx=10, pady=10)
        #botón refrescar
        boton_refrescar = tk.Button(frame_refrescar, text="Refrescar", font=('Times', 15), anchor="s", bg='#d5d247', bd=0, fg="#fff", command=self.refrescar)
        boton_refrescar.pack(fill=tk.X, padx=10, pady=10)
        boton_refrescar.bind("<Return>", (lambda event: self.refrescar()))

        #frame_verTransacciones 2,2
        frame_ver_transacciones = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_ver_transacciones.grid(row=2, column=2, padx=10, pady=10)
        #boton_transacciones
        boton_ver_transacciones = tk.Button(frame_ver_transacciones, text="Transacciones", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.verTransacciones)
        boton_ver_transacciones.pack(fill=tk.X, padx=10, pady=10)
        boton_ver_transacciones.bind("<Return>", (lambda event: self.verTransacciones()))

        #frame_gasto 3,0
        frame_gasto = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_gasto.grid(row=3, column=0, padx=10, pady=10)
        # boton_gasto
        boton_gasto = tk.Button(frame_gasto, text="Agregar Gasto", font=('Times', 15), bg='red', bd=0, fg="#fff", command=self.gasto)
        boton_gasto.pack(fill=tk.X, padx=10, pady=10)
        boton_gasto.bind("<Return>", (lambda event: self.gasto()))

        #frame_categorias 3,1
        frame_categorias = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_categorias.grid(row=3, column=1, padx=10, pady=10)
        # boton_categorias
        boton_categorias = tk.Button(frame_categorias, text="Categorías", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.categorias)
        boton_categorias.pack(fill=tk.X, padx=10, pady=10)
        boton_categorias.bind("<Return>", (lambda event: self.categorias()))

        #frame_ingreso 3,2
        frame_ingreso= tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_ingreso.grid(row=3, column=2, padx=10, pady=10)
        # boton_ingreso
        boton_ingreso = tk.Button(frame_ingreso, text="Agregar Ingreso", font=('Times', 15), bg='#81ed2c', bd=0, fg="#fff", command=self.ingreso)
        boton_ingreso.pack(fill=tk.X, padx=10, pady=10)
        boton_ingreso.bind("<Return>", (lambda event: self.ingreso()))

    def establecerLiminte(self):
        self.newWindow = tk.Toplevel(self.ventana)
        self.app = VentanaLimite(self.newWindow, self.usuario)

    def verTransacciones(self):
        self.newWindow = tk.Toplevel(self.ventana)
        self.app = VentanaTransacciones(self.newWindow, self.usuario)


    def categorias(self):
        self.newWindow = tk.Toplevel(self.ventana)
        self.app = VentanaCategorias(self.newWindow, self.usuario)

    def configuracion(self):
        self.newWindow = tk.Toplevel(self.ventana)
        self.app = VentanaConfiguracion(self.newWindow, self.usuario)

    def gasto(self):
        self.newWindow = tk.Toplevel(self.ventana)
        self.app = VentanaGasto(self.newWindow, self.usuario)

    def ingreso(self):
        self.newWindow = tk.Toplevel(self.ventana)
        self.app = VentanaIngreso(self.newWindow, self.usuario)

    def refrescar(self):
        esteUsuario = self.usuario
        self.ventana.destroy()
        root = tk.Tk()
        VentanaPrincipal(root, esteUsuario)
        root.mainloop()