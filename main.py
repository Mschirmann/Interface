from os import access
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from ui_login import Ui_Form
from OS_SIMAP_beta import Ui_MainWindow
import sys
from models.database import DataBase
from models.users import Users


class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        self.btn_login.clicked.connect(self.checkLogin)
        self.db_instance = DataBase()

    def checkLogin(self):
        db_conn = self.db_instance.create_connection()
        autenticado = Users(db_conn).check_user(
            self.txt_login.text().upper(), self.txt_password.text()
        )

        if autenticado.lower() == "administrador" or autenticado.lower() == "user":
            self.w = MainWindow(autenticado.lower())
            self.w.show()
            self.close()

        else:

            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(
                    f"Login ou Senha inválidos \n \n Tentativa: {self.tentativas +1} de 3"
                )
                msg.exec_()
                self.tentativas += 1

            if self.tentativas == 3:
                self.db_instance.close_connection(db_conn)
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Manutenção Patrimonial de TI")
        self.db_instance = DataBase()

        if user.lower() == "user":
            self.btn_pg_cadastro.setVisible(False)
            self.btn_editar.setVisible(False)
            self.btn_excluir.setVisible(False)
            self.btn_gerar.blockSignals(True)

        # *****************PÁGINAS DO SISTEMA******************
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_pg_cadastro.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_cadastro)
        )
        self.btn_gerar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_os))
        self.btn_consultar_os.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_consultar)
        )

        self.btn_cadastrar.clicked.connect(self.subscribe_user)

    def subscribe_user(self):

        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro de senha")
            msg.setText("Senhas não são iguais.")
            msg.exec()
            return None()

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db_conn = self.db_instance.create_connection()
        Users(db_conn).insert_user(nome, user, password, access)
        self.db_instance.close_connection(db_conn)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")


if __name__ == "__main__":
    DataBase().main()
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
