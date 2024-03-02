class Transaccion:
    def __init__(self, idusuario, idcategoria, concepto, cantidad, fecha,  idtransaccion = None):
        self.idusuario = idusuario
        self.idcategoria = idcategoria
        self.concepto = concepto
        self.cantidad = cantidad
        self.fecha = fecha
        self.idtransaccion = idtransaccion

