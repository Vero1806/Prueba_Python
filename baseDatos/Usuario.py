import database

class Usuarios:
    def __init__(self,nombre, apellidos, correo, contrasenna):
        self.__contrasenna = contrasenna
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__correo = correo
        self.contrasenna = contrasenna

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombreNuevo):
        self.__nombre= nombreNuevo

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidosNuevo):
        self.__apellidos= apellidosNuevo

    @property
    def correo(self):
        return self.__apellidos

    @correo.setter
    def correo(self, correoNuevo):
        self.__correo= correoNuevo

    @property
    def contrasenna(self):
        return self.__contrasenna

    @contrasenna.setter
    def contrasenna(self, contrasennaNueva):
        self.__contrasenna = contrasennaNueva

    @property
    def idusuario(self):
        return self.__idusuario




