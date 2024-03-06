from baseDatos.database import Database
from baseDatos.usuario import Usuario
from baseDatos.transacciones import Transaccion
from baseDatos.categorias import Categoria
from baseDatos.limites import Limite


class Modelo():

    @staticmethod
    def crearusuario(correo, contrasenna, nombre, apellidos):
        usuario = Usuario(correo, contrasenna, nombre, apellidos)
        db = Database()
        db.insert_usuario(usuario)

    @staticmethod
    def comprobarusuario(correo, contrasenna):
        usuario = Usuario(correo, contrasenna)
        db = Database()
        resultado = db.select_usuario(usuario)
        if resultado is not None:
            return True
        else:
            return False

    @staticmethod
    def comprobarusuarioexistente(correo):
        usuario = Usuario(correo)
        db = Database()
        resultado = db.select_usuario_porcorreo(usuario)
        if resultado is not None:
            return True
        else:
            return False

    @staticmethod
    def usuarioconectado(correo, contrasenna):
        usuario = Usuario(correo, contrasenna)
        db = Database()
        resultado = db.select_usuario(usuario)
        if resultado is not None:
            usuarioConectado = Usuario(idusuario=resultado[0], nombre=resultado[1], apellidos=resultado[2],
                                       correo=resultado[3], contrasenna=resultado[4], saldo=resultado[5])
            return usuarioConectado
        else:
            return None

    @staticmethod
    def vertransacciones(usuario: Usuario):
        db = Database()
        arrayTras = db.select_transacciones(usuario)
        listaTran = []
        for elemento in arrayTras:
            listaTran.append(
                f"Categoria: {elemento[0]}, Concepto: {elemento[1]}, Cantidad: {elemento[2]}, fecha {elemento[3]}")

        return listaTran

    @staticmethod
    def realizartransaccion(idusuario, idcategoria, concepto, cantidad):
        transaccion = Transaccion(idusuario, idcategoria, concepto, cantidad)
        db = Database()
        resultado = db.insert_transaccion(transaccion)
        if resultado is not None:
            return True
        else:
            return False

    @staticmethod
    def vercategorias(usuario: Usuario):
        db = Database()
        arrayCat = db.select_categorias(usuario)
        listaCat = []
        for elemento in arrayCat:
            listaCat.append(f"Nombre: {elemento[0]}")
        return listaCat

    @staticmethod
    def verCategoriasCompleto(usuario: Usuario):
        db = Database()
        arrayCat = db.select_categoria_genericaYpropia(usuario)
        listaCat_nombre = []
        for elemento in arrayCat:
            listaCat_nombre.append(elemento)

        return listaCat_nombre

    @staticmethod
    def verCategoriasCompletonombre(usuario: Usuario):
        db = Database()
        arrayCat = db.select_categoria_genericaYpropia(usuario)
        listaCat_id = []

        for elemento2 in arrayCat:
            listaCat_id.append(elemento2[1])

        return listaCat_id

    @staticmethod
    def insertcategorias(nombre, usuario: Usuario):
        categoria = Categoria(nombre, usuario.idusuario)
        db = Database()
        db.insert_categoria(categoria)

    @staticmethod
    def selectcategorias(usuario: Usuario):
        db = Database()
        resultado = db.select_categorias(usuario.idusuario)

        return resultado

    @staticmethod
    def insertar_gasto_ingreso(usuario: Usuario, nombreCategoria, concepto, cantidad):

        gasto = Transaccion(usuario.idusuario, nombreCategoria, concepto, cantidad)
        db = Database()
        resultado = db.insert_transaccion(gasto)
        if resultado is not None:
            return True
        else:
            return False

    @staticmethod
    def ver_limite_categoria (usuario: Usuario):
        db = Database()
        resultado = db.select_limite_categoria(usuario)
        listaLimites = []
        for elemento in resultado:
            listaLimites.append(f"Categoria: {elemento[0]}, Cantidad: {elemento[1]}")

        return listaLimites



