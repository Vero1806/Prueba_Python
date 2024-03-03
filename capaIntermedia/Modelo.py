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
        usuarioConectado = Usuario()
        usuarioConectado.idusuario = resultado[0]
        usuarioConectado.nombre = resultado[1]
        usuarioConectado.apellidos = resultado[2]
        usuarioConectado.correo = resultado[3]
        usuarioConectado.contrasenna = resultado[4]
        usuarioConectado.saldo = resultado[5]

        return usuarioConectado

    @staticmethod
    def vertransacciones(idusuario):
        usuario = Usuario()
        usuario.idusuario = idusuario
        db = Database()
        return db.select_transacciones(usuario)


print(Modelo().vertransacciones(1))




