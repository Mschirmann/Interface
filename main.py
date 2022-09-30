from os import access
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from models.os import Os
from ui_login import Ui_Form
from OS_SIMAP_beta import Ui_MainWindow
import sys
from models.database import DataBase
from models.users import Users
from datetime import datetime


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
        self.btn_gravar.clicked.connect(self.save_os)
        self.btn_editar.clicked.connect(
            self.edit_os
        )  # ver como passar uma os para preencher os dados no formulario
        self.btn_excluir.clicked.connect(self.remove_os)
        self.btn_consultar.clicked.connect(self.list_os)

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

    def save_os(self):
        num_os = self.txt_num_os.text()
        status = self.cb_close.text()
        dt_os = self.dt_emissao.text()
        hr_os = self.dt_horario.text()
        # formatting date to save in database
        string_date = dt_os + " " + hr_os
        os_datetime_obj = datetime.strptime(string_date, "%d/%m/%y %H:%M")
        dt_hr_os = os_datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

        dt_end = self.dt_fechamento.text()
        if dt_end and len(dt_end) > 0:
            dt_end = datetime.strptime(dt_end, "%d/%m/%y %H:%M")
            dt_end = dt_end.strftime("%Y-%m-%d %H:%M:%S")

        customer = self.txt_solicitante.text()
        technical_manager = self.txt_responsavel.text()
        service_type = self.cb_tipo.currentText()
        service_start_dt = self.dt_inicio.text()
        if service_start_dt and len(service_start_dt) > 0:
            service_start_dt = datetime.strptime(service_start_dt, "%d/%m/%y %H:%M")
            service_start_dt = service_start_dt.strftime("%Y-%m-%d %H:%M:%S")
        service_end_dt = self.dt_termino.text()
        if service_end_dt and len(service_end_dt) > 0:
            service_end_dt = datetime.strptime(service_end_dt, "%d/%m/%y %H:%M")
            service_end_dt = service_end_dt.strftime("%Y-%m-%d %H:%M:%S")
        service_description = self.plainTextEdit.toPlainText()
        equip_number = self.txt_num_patrimonio.text()
        equip_description = self.txt_equipamento.text()
        equip_model = self.txt_modelo.text()
        equip_brand = self.txt_marca.text()
        equip_props = self.txt_acessorios.text()
        equip_defect = self.plainTextEdit_4.toPlainText()
        equip_obs = self.plainTextEdit_3.toPlainText()
        parts_used = self.plainTextEdit_2.toPlainText()
        part_type = self.txt_tipo.text()
        part_qtd = self.sb_qtde.text()
        part_price = self.txt_preco.text()
        part_total = self.txt_valor.text()

        os_data = (
            status,
            dt_hr_os,
            dt_end,
            customer,
            technical_manager,
            service_start_dt,
            service_end_dt,
            service_description,
            service_type,
            equip_number,
            equip_brand,
            equip_description,
            equip_model,
            equip_props,
            equip_defect,
            equip_obs,
            parts_used,
            part_type,
            part_qtd,
            part_price,
            part_total,
            num_os,
        )
        # validar data
        print(dt_hr_os)
        # Aqui precisa checar se o num_os já existe, caso existir será feito um update senão um create
        db_conn = self.db_instance.create_connection()
        Os(db_conn).insert_os(os_data)
        self.db_instance.close_connection(db_conn)

    def list_os(self):
        num_os = self.txt_num_os_consulta.text()
        equip_inventory = self.txt_num_patrimonio_consulta.text()
        equip_description = self.txt_equipamento_consulta.text()
        customer = self.txt_solicitante_consulta.text()
        status = self.cb_status_consulta.currentText()
        dt_os_start = self.dt_periodo_consulta.text()
        dt_os_end = self.dateEdit_2.text()

        db_conn = self.db_instance.create_connection()
        os_list = Os(db_conn).get_all_os()
        self.db_instance.close_connection(db_conn)

        print(os_list)

    def remove_os(self):
        selected_os = self.treeWidget.currentItem()
        print(selected_os)
        # db_conn = self.db_instance.create_connection()
        # Os(db_conn).delete_os(1)
        # self.db_instance.close_connection(db_conn)

    def edit_os(self):
        selected_os = self.treeWidget.currentItem()
        print(selected_os)

        self.Pages.setCurrentWidget(self.pg_os)


if __name__ == "__main__":
    DataBase().main()
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
