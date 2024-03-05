import tkinter as tk
from tkinter import messagebox

import util.generic as utl
from Interfaz.VentanaLimite import VentanaLimite
from Interfaz.VentanaTransacciones import VentanaTransacciones
from Interfaz.VentanaCategorias import VentanaCategorias
from Interfaz.VentanaConfiguracion import VentanaConfiguración
from Interfaz.VentanaGastoIngreso import VentanaGastoIngreso
from baseDatos.usuario import Usuario
from capaIntermedia.Modelo import Modelo


class VentanaPrincipal:
    def __init__(self, ventana, usuario: Usuario):
        self.ventana = ventana
        self.ventana.title('VentanaPrincipal')
        self.ventana.geometry('800x600')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0) #No permite cambiar el tamaño de la ventana
        utl.centrar_ventana(self.ventana, 800, 600)
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=5)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(1, weight=10)
        self.ventana.grid_rowconfigure(2, weight=1)

        self.usuario = usuario
        logo = utl.leer_imagen("./util/logoBlanco.png", (50, 50))

        # frame_logo 0,0
        frame_logo = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_logo.grid(row=0, column=0, pady=10, padx=10)  # Utilizando grid y sticky para alinear al norte KOTLIN
        # Label para el logo
        label_logo = tk.Label(frame_logo, image=logo, bg='#fcfcfc', anchor="center")
        label_logo.grid(row=0, column=0,  pady=10, padx=10)

        # frame_titulo 0,1
        frame_titulo = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_titulo.grid(row=0, column=1, sticky="NSEW")
        # Label para el texto de bienvenida (Título)
        label_titulo = tk.Label(frame_titulo, text=f"Menú Principal de {self.usuario.nombre}", font=('Helvetica', 18), bg='#fcfcfc', anchor="center")
        label_titulo.grid(row=0, column=1, pady=20, padx=5, sticky="NSEW")

        #frame_vacio 0,2
        frame_vacio = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_vacio.grid(row=0, column=2, pady=20, padx=5)


        #frame_limite 1,0
        frame_establecer_límite = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_establecer_límite.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        # boton_limite
        boton_establecer_limite = tk.Button(frame_establecer_límite, text="Establecer Límite", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.establecerLiminte)
        boton_establecer_limite.pack(fill=tk.X, padx=10, pady=10)
        boton_establecer_limite.bind("<Return>", (lambda event: self.establecerLiminte()))

        #frame_saldo 1,1
        frame_saldo = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_saldo.grid(row=1, column=1, padx=10, pady=10)
        # Label saldo
        label_saldo = tk.Label(frame_saldo, text=f"Saldo actual: {self.usuario.saldo}€", font=('Helvetica', 15), bg='#fcfcfc', anchor="center")
        label_saldo.grid(row=1, column=1, pady=10, padx=10)
            # + usuario.saldo

        #frame_verTransacciones 1,2
        frame_ver_transacciones = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_ver_transacciones.grid(row=1, column=2, padx=10, pady=10)
        # boton_transacciones
        boton_ver_transacciones = tk.Button(frame_ver_transacciones, text="Transacciones", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.verTransacciones)
        boton_ver_transacciones.pack(fill=tk.X, padx=10, pady=10)
        boton_ver_transacciones.bind("<Return>", (lambda event: self.verTransacciones()))

        #frame_verTransacciones 2,0
        frame_categorias = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_categorias.grid(row=2, column=0, padx=10, pady=10)
        # boton_transacciones
        boton_categorias = tk.Button(frame_categorias, text="Categorías", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.categorias)
        boton_categorias.pack(fill=tk.X, padx=10, pady=10)
        boton_categorias.bind("<Return>", (lambda event: self.categorias()))

        #frame_verTransacciones 2,1
        frame_gastoIngreso = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_gastoIngreso.grid(row=2, column=1, padx=10, pady=10)
        # boton_transacciones
        boton_gastoIngreso = tk.Button(frame_gastoIngreso, text="Agregar Gasto/Ingreso", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.gastoIngreso)
        boton_gastoIngreso.pack(fill=tk.X, padx=10, pady=10)
        boton_gastoIngreso.bind("<Return>", (lambda event: self.gastoIngreso()))

        #frame_verTransacciones 2,2
        frame_configuracion = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_configuracion.grid(row=2, column=2, padx=10, pady=10)
        # boton_transacciones
        boton_configuracion = tk.Button(frame_configuracion, text="Configuración", font=('Times', 15), bg='#808080', bd=0, fg="#fff", command=self.configuracion)
        boton_configuracion.pack(fill=tk.X, padx=10, pady=10)
        boton_configuracion.bind("<Return>", (lambda event: self.configuracion()))

    def establecerLiminte(self):
        VentanaLimite()

    def verTransacciones(self):
        self.newWindow = tk.Toplevel(self.ventana)
        self.app = VentanaTransacciones(self.newWindow, self.usuario)


    def categorias(self):
        self.newWindow = tk.Toplevel(self.ventana)
        self.app = VentanaCategorias(self.newWindow, self.usuario)

    def configuracion (self):
        VentanaConfiguración()

    def gastoIngreso(self):
        VentanaGastoIngreso()