import pymysql


class Database():

    def insert_usuario(self, usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute(('INSERT INTO usuarios (nombre, apellidos, correo, contraseña) VALUES (%s, %s, %s, %s)',
                            (usuario.nombre, usuario.apellidos, usuario.correo, usuario.contrasenna)))
            db_connection.commit()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

    def select_usuario(self, usuario):
        try:
            db_connection = self.get_conexion()
            cursor = db_connection.cursor()

        except Exception as e:
            return e

        try:
            cursor.execute(('SELECT idusuario, nombre, apellidos, correo, contraseña, saldo from usuarios where correo = %s and contraseña = %s',
                            (usuario.correo, usuario.contrasenna)))
            resultado = cursor.fetchone()

        except Exception as e:
            return e

        finally:
            cursor.close()
            db_connection.close()

        return resultado

    def get_conexion(self):

        return pymysql.connect(
            host='bfd7fdiocr7zh4l7xw9b-mysql.services.clever-cloud.com',
            user='uauvkfwlwjuus5kd',
            password='Pq5txodnCxBRLAT3c1MO',
            database='bfd7fdiocr7zh4l7xw9b'
        )
