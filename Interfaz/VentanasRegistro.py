import tkinter as tk
from tkinter import ttk, messagebox
from capaIntermedia.Modelo import Modelo

class VentanaRegistro:

    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Registrarse")
        self.ventana.geometry('500x600')

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, padx=25, pady=10, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top
        frame_form_top = tk.Frame(frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de usuario", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_nombre = tk.Label(frame_form_fill, text="Nombre", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20, pady=5)
        self.nombre = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.nombre.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_apellidos = tk.Label(frame_form_fill, text="Apellidos", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_apellidos.pack(fill=tk.X, padx=20, pady=5)
        self.apellidos = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.apellidos.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_correo = tk.Label(frame_form_fill, text="Correo electrónico", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_correo.pack(fill=tk.X, padx=20, pady=5)
        self.correo = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.correo.pack(fill=tk.X, padx=20, pady=10)


        etiqueta_contrasenna = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_contrasenna.pack(fill=tk.X, padx=20, pady=5)
        self.contrasenna = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.contrasenna.pack(fill=tk.X, padx=20, pady=10)
        self.contrasenna.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Registar", font=('Times', 15), bg='#3a7ff6', bd=0, fg='#fff', command=self.register)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.register()))

        self.ventana.mainloop()

    def register(self):
        usuario_existe = Modelo().comprobarusuarioexistente(self.correo.get())

        if not usuario_existe:
            Modelo().crearusuario(self.correo.get(), self.contrasenna.get(), self.nombre.get(), self.apellidos.get())
            messagebox.showinfo(message="Se registro el usuario", title="Mensaje")
            self.ventana.destroy()

        else:
            messagebox.showinfo(message="El correo " + self.correo.get() + " ya esta registrado", title="Mensaje")