import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from Interfaz.VentanasRegistro import VentanaRegistro
from capaIntermedia.Modelo import Modelo
from baseDatos.usuario import Usuario
class VentanaPrincipal():
    def __init__(self, usuario: Usuario):
        self.ventana = tk.Tk()
        self.ventana.title('Login')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 600)

        self.usuario = usuario