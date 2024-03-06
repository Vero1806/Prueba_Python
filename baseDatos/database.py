import pymysql
from baseDatos.usuario import Usuario
from baseDatos.transacciones import Transaccion
from baseDatos.categorias import Categoria
from baseDatos.limites import Limite


class Database():

    def get_conexion(self):
        return pymysql.connect(
            host='bfd7fdiocr7zh4l7xw9b-mysql.services.clever-cloud.com',
            user='uauvkfwlwjuus5kd',
            password='Pq5txodnCxBRLAT3c1MO',
            database='bfd7fdiocr7zh4l7xw9b'
        )

    def insert_usuario(self, usuario: Usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute('INSERT INTO usuarios (nombre, apellidos, correo, contrasenna) VALUES (%s, %s, %s, %s)',
                           (usuario.nombre, usuario.apellidos, usuario.correo, usuario.contrasenna))
            db_connection.commit()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

    def select_usuario(self, usuario: Usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute(
                'SELECT idusuario, nombre, apellidos, correo, contrasenna, saldo from usuarios where correo = %s and contrasenna = %s',
                (usuario.correo, usuario.contrasenna))
            result = cursor.fetchone()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

        return result

    def select_usuario_porcorreo(self, usuario: Usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute('SELECT correo from usuarios where correo = %s',
                           usuario.correo)
            result = cursor.fetchone()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

        return result

    def insert_categoria(self, categoria: Categoria):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute('INSERT INTO categorias (nombre, idusuario) VALUES (%s, %s)',
                           (categoria.nombre, categoria.idusuario))
            db_connection.commit()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

    def select_categorias(self, usuario: Usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute('SELECT nombre from categorias where idusuario = %s',
                           (usuario.idusuario))
            resultado = cursor.fetchall()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

        return resultado

    def select_categoria_genericaYpropia(self, usuario: Usuario):

        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute('SELECT idcategoria, nombre FROM categorias WHERE idusuario is null UNION SELECT idcategoria, nombre FROM categorias WHERE idusuario = %s',
                           (usuario.idusuario))
            resultado = cursor.fetchall()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

        return resultado

    def insert_transaccion(self, transaccion: Transaccion):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute(
                'INSERT INTO transacciones (idusuario, idcategoria, concepto, cantidad, fecha) VALUES (%s, %s, %s, %s, CURDATE())',
                (transaccion.idusuario, transaccion.idcategoria, transaccion.concepto, transaccion.cantidad))
            db_connection.commit()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

    def select_transacciones(self, usuario: Usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute(
                'SELECT categorias.nombre, transacciones.concepto, transacciones.cantidad, transacciones.fecha from transacciones '
                'inner join categorias on transacciones.idcategoria = categorias.idcategoria where transacciones.idusuario = %s',
                (usuario.idusuario))
            resultado = cursor.fetchall()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

        return resultado

    def total_transacciones(self, usuario: Usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute('SELECT SUM(cantidad) FROM transacciones WHERE idusuario = %s',
                           (usuario.idusuario))
            resultado = cursor.fetchall()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

        return resultado

    def insert_limite(self, limite: Limite):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute('INSERT INTO limites (idusuario, limite, idcategoria) VALUES (%s, %s, %s)',
                           (limite.idusuario, limite.limite, limite.idcategoria))
            db_connection.commit()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

    def select_limite_idcategoria(self, usuario: Usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute('SELECT idcategoria from limites where idusuario = %s',
                           (usuario.idusuario))
            resultado = cursor.fetchall()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

        return resultado

    def select_limite_categoria(self, usuario: Usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute('select categorias.nombre, limites.limite from limites inner join categorias on limites.idcategoria = categorias.idcategoria where limites.idusuario = %s',
                           (usuario.idusuario))
            resultado = cursor.fetchall()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

        return resultado
