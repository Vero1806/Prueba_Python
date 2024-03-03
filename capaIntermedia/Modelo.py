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
    def vertransacciones(idusuario):
        usuario = Usuario()
        usuario.idusuario = idusuario
        db = Database()
        return db.select_transacciones(usuario)


print(Modelo().vertransacciones(1))




