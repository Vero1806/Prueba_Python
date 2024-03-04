class Limite:
    def __init__(self, idusuario, limite, idlimite = None):
        self.__idlimite = idlimite
        self.__idusuario = idusuario
        self.__limite = limite

    @property
    def idlimite(self):
        return self.__idlimite
    @idlimite.setter
    def idlimite(self, nuevo_idlimite):
        self.__limite = nuevo_idlimite

    @property
    def idusuario(self):
        return self.__idusuario

    @idusuario.setter
    def idusuario(self, nuevo_idusuario):
        self.__limite = nuevo_idusuario

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, nuevo_limite):
        self.__limite = nuevo_limite
