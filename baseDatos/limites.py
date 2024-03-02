class Limite:
    def __init__(self, idusuario, limite, idlimite = None):
        self.__idlimite = idlimite
        self.__idusuario = idusuario
        self.__limite = limite

    @property
    def idlimite(self):
        return self.__idlimite

    @property
    def idusuario(self):
        return self.__idusuario

    @property
    def limite(self):
        return self.__limite

    @nombre.setter
    def limite(self, nuevo_limite):
        self.__limite = nuevo_limite