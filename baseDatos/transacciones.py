class Transaccion:
    def __init__(self, idusuario, idcategoria, concepto, cantidad, fecha, idtransaccion = None):
        self.idusuario = idusuario
        self.idcategoria = idcategoria
        self.concepto = concepto
        self.cantidad = cantidad
        self.fecha = fecha
        self.idtransaccion = idtransaccion

    @property
    def idusuario(self):
        return self.__idusuario
    @idusuario.setter
    def idusuario(self, nuevo_idusuario):
        self.__idusuario = nuevo_idusuario

    @property
    def idcategoria(self):
        return self.__idcategoria
    @idcategoria.setter
    def idcategoria(self, nuevo_idcategoria):
        self.__idcategoria = nuevo_idcategoria

    @property
    def concepto(self):
        return self.__concepto
    @concepto.setter
    def concepto(self, nuevo_concepto):
        self.__concepto = nuevo_concepto

    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, nuevo_cantidad):
        self.__cantidad = nuevo_cantidad

    @property
    def fecha(self):
        return self.__fecha
    @cantidad.setter
    def cantidad(self, nuevo_fecha):
        self.__fecha = nuevo_fecha

    @property
    def idtransaccion(self):
        return self.__idtransaccion
    @cantidad.setter
    def idtransaccion(self, idtransaccion):
        self.__idtransaccion = idtransaccion