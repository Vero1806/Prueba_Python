import tkinter as tk
from tkinter import ttk, messagebox
import util.generic as utl
from Interfaz.VentanasRegistro import VentanaRegistro
from Interfaz.VentanaPrincipal import VentanaPrincipal
from capaIntermedia.Modelo import Modelo

class VentanaLogin:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Login')
        self.ventana.geometry('800x600')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 600)

        logo = utl.leer_imagen("./util/logo.png", (200, 200))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200,relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_correo = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_correo.pack(fill=tk.X, padx=20, pady=5)
        self.correo = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.correo.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_contrasenna = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_contrasenna.pack(fill=tk.X, padx=20, pady=5)
        self.contrasenna = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.contrasenna.pack(fill=tk.X, padx=20, pady=10)
        self.contrasenna.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Iniciar sesión", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.verificar()))


        inicio = tk.Button(frame_form_fill, text="Registrar Usuario", font=('Times', 15), bg='#fcfcfc', bd=0, fg="#3a7ff6", command=self.userRegister)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.userRegister()))


        self.ventana.mainloop()


    def verificar(self):
        usuario_correcto = Modelo().comprobarusuario(self.correo.get(), self.contrasenna.get())

        if usuario_correcto:
            usuario_conectado = Modelo().usuarioconectado(self.correo.get(), self.contrasenna.get())
            messagebox.showinfo(message="Bienvenido " + usuario_conectado.nombre, title="Mensaje")
            self.ventana.destroy()
            VentanaPrincipal(usuario_conectado)


        else:
            messagebox.showinfo(message="Usuario o contraseña Incorrecto", title="Mensaje")

    def userRegister(self):
       VentanaRegistro()
