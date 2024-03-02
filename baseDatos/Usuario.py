class Usuario:
    def __init__(self, nombre, apellidos, correo, contrasenna, idusuario = None):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__correo = correo
        self.__contrasenna = contrasenna
        self.__idusuario = idusuario

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, nuevos_apellidos):
        self.__apellidos = nuevos_apellidos

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = nuevo_correo

    @property
    def contrasenna(self):
        return self.__contrasenna

    @contrasenna.setter
    def contrasenna(self, nueva_contrasenna):
        self.__contrasenna = nueva_contrasenna


    @property
    def idusuario(self):
        return self.__idusuario

    @idusuario.setter
    def idusuario(self, nueva_idusuario):
        self.__idusuario = nueva_idusuario