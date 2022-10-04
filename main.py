from os import access
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QMessageBox,
    QTreeWidgetItem,
)
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
            # self.btn_editar.setVisible(False)
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
        # self.btn_editar.clicked.connect(self.edit_os)
        self.btn_excluir.clicked.connect(self.remove_os)
        self.btn_consultar.clicked.connect(self.list_os)
        self.btn_sair.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))

        # self.treeWidget.itemClicked.connect(self.onItemClicked)

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
        status = "Fechada" if self.cb_close.isChecked() else "Aberta"
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
            int(num_os),
        )
        # Aqui precisa checar se o num_os já existe, caso existir será feito um update senão um create
        db_conn = self.db_instance.create_connection()
        created_id = Os(db_conn).insert_os(os_data)
        self.db_instance.close_connection(db_conn)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Nova Ordem de serviço")
        if created_id[0]:
            msg.setText(
                "Ordem de serviço: {} inserida com sucesso!".format(created_id[1])
            )
        else:
            msg.setText("Não foi possível inserir nova Ordem de serviço!")
        msg.exec()

    def list_os(self):

        # Get data from form
        num_os = self.txt_num_os_consulta.text()
        equip_inventory = self.txt_num_patrimonio_consulta.text()
        equip_description = self.txt_equipamento_consulta.text()
        customer = self.txt_solicitante_consulta.text()
        status = self.cb_status_consulta.currentText()
        dt_os_start = self.dt_periodo_consulta.text()
        dt_os_end = self.dateEdit_2.text()

        # validate data
        num_os = num_os if num_os else None
        equip_inventory = equip_inventory if equip_inventory else None
        equip_description = equip_description if equip_description else None
        customer = customer if customer else None
        status = status if status else None
        if dt_os_start:
            dt_os_start = datetime.strptime(dt_os_start, "%d/%m/%y")
            dt_os_start = dt_os_start.strftime("%Y-%m-%d %H:%M:%S")
        else:
            dt_os_start = None
        if dt_os_end:
            dt_os_end = datetime.strptime(dt_os_end, "%d/%m/%y")
            dt_os_end = dt_os_end.strftime("%Y-%m-%d %H:%M:%S")
        else:
            dt_os_end = None

        # Open db connection
        db_conn = self.db_instance.create_connection()

        # Call method to fetch all OS by filter options
        os_list = Os(db_conn).get_all_os(
            id=num_os,
            equip_inventory_number=equip_inventory,
            equip_name=equip_description,
            customer=customer,
            status=status,
            dt_start=dt_os_start,
            dt_end=dt_os_end,
        )
        self.db_instance.close_connection(db_conn)

        # First clear current table then list filtered items
        self.treeWidget.clear()
        items = []
        for os in os_list:
            os_dt = os["created_at"]
            os_dt = datetime.strptime(os_dt, "%Y-%m-%d %H:%M:%S")
            os_dt = os_dt.strftime("%d/%m/%Y")
            item = QTreeWidgetItem(
                [
                    "",
                    str(os["id"]),
                    os["customer"],
                    os["equip_inventory_number"],
                    os["equip_name"],
                    os_dt,
                    os["status"],
                    str(os["part_total"]),
                ]
            )
            items.append(item)
        self.treeWidget.insertTopLevelItems(0, items)

    def remove_os(self):
        selected_os = self.treeWidget.currentItem()
        os_num = selected_os.text(1)
        if os_num:
            db_conn = self.db_instance.create_connection()
            Os(db_conn).delete_os(os_num)
            self.db_instance.close_connection(db_conn)
        self.list_os()

    def edit_os(self):
        selected_os = self.treeWidget.currentItem()
        os_num = selected_os.text(1)
        if os_num:
            db_conn = self.db_instance.create_connection()
            os_instance = Os(db_conn).get_os(os_num)
            self.db_instance.close_connection(db_conn)
        self.Pages.setCurrentWidget(self.pg_os)


if __name__ == "__main__":
    DataBase().main()
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
