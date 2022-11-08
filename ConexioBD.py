import pymysql
import self


class Base_Datos:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost', #ip del servidor
            user='alejo',
            password='ezio14592407',
            db='poo', #nombre de la base de datos
        )

        self.cursor = self.connection.cursor()

    def SelectUser(self, id):
        pymysql = 'SELECT idusuarios, nombre FROM usuario WHERE id = {id}'.format(id)

        try:
            self.cursor.execute(pymysql)
            user = self.cursor.fetcone()

            print("idusuario: ", user[0])
            print("usuario: ", user[1])
            print("apellido: ", user[2])

            pass
        except Exception as e:
            raise

BaseDedatos = Base_Datos
BaseDedatos.SelectUser()
