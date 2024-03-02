class Categoria:
    def __init__(self, nombre, idusuario, idcategoria = None):
        self.__nombre = nombre
        self.__idusuario = idusuario
        self.__idcategoria = idcategoria

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def idusuario(self):
        return self.__idusuario

    @property
    def idcategoria(self):
        return self.__idcategoria
