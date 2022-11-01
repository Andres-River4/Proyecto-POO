import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic.properties import QtWidgets

from login import *
from registro import *
import conexion
import time

class MiApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#eliminar barra
		self.setWindowFlag(Qt.FramelessWindowHint)
		#transparente
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.ui.bt_ingresar.clicked.connect(self.iniciar_sesion)
     	# base de datos

		##self.datos = conexion.Registro_datos()


	def iniciar_sesion(self):
		self.ui.contrasena_incorrecta.setText('')
		self.ui.usuario_incorrecto.setText('')
		users_entry = self.ui.users.text()
		password_entry = self.ui.password.text()

		users_entry = str("'" + users_entry + "'")
		password_entry = str("'" + password_entry + "'")

		dato1 = self.datos.busca_users(users_entry)
		dato2 = self.datos.busca_password(password_entry)

		fila1 = dato1
		fila2 = dato2

		if fila1 == fila2:
			if dato1 == [] and dato2 ==[]:
				self.ui.contrasena_incorrecta.setText('Contraseña incorrecta')
				self.ui.usuario_incorrecto.setText('Usuario incorrecto')
			else:

				if dato1 ==[]:
					self.ui.usuario_incorrecto.setText('Usuario incorrecto')
				else:
					dato1 = dato1[0][1]

				if dato2 ==[]:
					self.ui.contrasena_incorrecta.setText('Contraseña incorrecta')
				else:
					dato2 = dato2[0][2]

				if dato1 != [] and dato2 != []:
					for i in range(0,99):
						time.sleep(0.02)
						self.ui.progressBar.setValue(i)
						self.ui.cargando.setText('Cargando...')

					self.hide()
					self.registro1 = registro()
					self.ventana.show()
		else:
			self.ui.contrasena_incorrecta.setText(' Error ')
			self.ui.usuario_incorrecto.setText(' Error ')
			#


##class registro:
	##pass


##class registro(QMainWindow):
	##def __init__(self):
		##super().__init__()
		##self.registro= registro()
		##self.registro.setupUi(self)##



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())