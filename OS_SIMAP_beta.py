# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OS_SIMAP_beta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(862, 659)
        font = QFont()
        font.setFamily(u"Microsoft JhengHei")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 100, 150);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.centralwidget)
        self.btn_home.setObjectName(u"btn_home")
        font1 = QFont()
        font1.setFamily(u"Microsoft JhengHei")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_home.setFont(font1)
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(249, 196, 48);\n"
"	color: rgb(0, 100, 150);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 100, 150)\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_gerar = QPushButton(self.centralwidget)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setFont(font1)
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(249, 196, 48);\n"
"	color: rgb(0, 100, 150);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 100, 150)\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_gerar)

        self.btn_consultar_os = QPushButton(self.centralwidget)
        self.btn_consultar_os.setObjectName(u"btn_consultar_os")
        self.btn_consultar_os.setFont(font1)
        self.btn_consultar_os.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(249, 196, 48);\n"
"	color: rgb(0, 100, 150);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 100, 150)\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_consultar_os)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setFont(font)
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pg_os = QWidget()
        self.pg_os.setObjectName(u"pg_os")
        self.btn_gravar = QPushButton(self.pg_os)
        self.btn_gravar.setObjectName(u"btn_gravar")
        self.btn_gravar.setGeometry(QRect(320, 566, 75, 23))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(140, 205, 135, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_gravar.setPalette(palette)
        font2 = QFont()
        font2.setFamily(u"Microsoft JhengHei")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_gravar.setFont(font2)
        self.btn_gravar.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(140, 205, 135);\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 100, 150)\n"
"\n"
"}")
        self.btn_sair = QPushButton(self.pg_os)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setGeometry(QRect(428, 566, 75, 23))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(200, 70, 100, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.btn_sair.setPalette(palette1)
        self.btn_sair.setFont(font2)
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(200, 70, 100);\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 100, 150)\n"
"\n"
"}")
        self.btn_sair.setCheckable(False)
        self.dados_equip = QGroupBox(self.pg_os)
        self.dados_equip.setObjectName(u"dados_equip")
        self.dados_equip.setGeometry(QRect(220, 26, 580, 280))
        font3 = QFont()
        font3.setFamily(u"Microsoft JhengHei")
        font3.setBold(True)
        font3.setWeight(75)
        self.dados_equip.setFont(font3)
        self.dados_equip.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.label_21 = QLabel(self.dados_equip)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(11, 30, 105, 16))
        self.label_21.setMinimumSize(QSize(105, 0))
        self.label_27 = QLabel(self.dados_equip)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(212, 30, 62, 16))
        self.label_27.setMinimumSize(QSize(62, 0))
        self.label_28 = QLabel(self.dados_equip)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(212, 60, 34, 16))
        self.label_28.setMinimumSize(QSize(34, 0))
        self.label_29 = QLabel(self.dados_equip)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(11, 60, 29, 16))
        self.label_29.setMinimumSize(QSize(29, 0))
        self.label_30 = QLabel(self.dados_equip)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 120, 89, 13))
        self.label_31 = QLabel(self.dados_equip)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(11, 90, 51, 16))
        self.label_31.setMinimumSize(QSize(51, 0))
        self.label_32 = QLabel(self.dados_equip)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 182, 71, 16))
        self.txt_num_patrimonio = QLineEdit(self.dados_equip)
        self.txt_num_patrimonio.setObjectName(u"txt_num_patrimonio")
        self.txt_num_patrimonio.setGeometry(QRect(120, 30, 81, 20))
        self.txt_num_patrimonio.setMinimumSize(QSize(81, 0))
        self.txt_num_patrimonio.setStyleSheet(u"background-color: rgb(250, 250, 250)")
        self.txt_equipamento = QLineEdit(self.dados_equip)
        self.txt_equipamento.setObjectName(u"txt_equipamento")
        self.txt_equipamento.setGeometry(QRect(278, 30, 291, 20))
        self.txt_equipamento.setMinimumSize(QSize(291, 0))
        self.txt_equipamento.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.txt_marca = QLineEdit(self.dados_equip)
        self.txt_marca.setObjectName(u"txt_marca")
        self.txt_marca.setGeometry(QRect(44, 60, 157, 20))
        self.txt_marca.setMinimumSize(QSize(111, 0))
        self.txt_marca.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.txt_modelo = QLineEdit(self.dados_equip)
        self.txt_modelo.setObjectName(u"txt_modelo")
        self.txt_modelo.setGeometry(QRect(278, 60, 157, 20))
        self.txt_modelo.setMinimumSize(QSize(141, 0))
        self.txt_modelo.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.txt_acessorios = QLineEdit(self.dados_equip)
        self.txt_acessorios.setObjectName(u"txt_acessorios")
        self.txt_acessorios.setGeometry(QRect(65, 90, 504, 20))
        self.txt_acessorios.setStyleSheet(u"background-color: rgb(245, 245, 245)")
        self.plainTextEdit_3 = QPlainTextEdit(self.dados_equip)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(10, 202, 560, 61))
        self.plainTextEdit_4 = QPlainTextEdit(self.dados_equip)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(10, 138, 560, 40))
        self.dados_pecas = QGroupBox(self.pg_os)
        self.dados_pecas.setObjectName(u"dados_pecas")
        self.dados_pecas.setGeometry(QRect(415, 309, 385, 238))
        self.dados_pecas.setFont(font3)
        self.dados_pecas.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.label_33 = QLabel(self.dados_pecas)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 30, 151, 16))
        self.label_34 = QLabel(self.dados_pecas)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(13, 142, 21, 16))
        self.txt_tipo = QLineEdit(self.dados_pecas)
        self.txt_tipo.setObjectName(u"txt_tipo")
        self.txt_tipo.setGeometry(QRect(39, 140, 335, 20))
        self.txt_tipo.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.label_35 = QLabel(self.dados_pecas)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 170, 31, 16))
        self.sb_qtde = QSpinBox(self.dados_pecas)
        self.sb_qtde.setObjectName(u"sb_qtde")
        self.sb_qtde.setGeometry(QRect(39, 170, 42, 20))
        self.sb_qtde.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.label_36 = QLabel(self.dados_pecas)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(93, 170, 71, 16))
        self.txt_preco = QLineEdit(self.dados_pecas)
        self.txt_preco.setObjectName(u"txt_preco")
        self.txt_preco.setGeometry(QRect(163, 170, 73, 20))
        self.txt_preco.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.txt_valor = QLineEdit(self.dados_pecas)
        self.txt_valor.setObjectName(u"txt_valor")
        self.txt_valor.setGeometry(QRect(301, 170, 73, 20))
        self.txt_valor.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.label_37 = QLabel(self.dados_pecas)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(248, 170, 71, 16))
        self.dt_fechamento = QDateTimeEdit(self.dados_pecas)
        self.dt_fechamento.setObjectName(u"dt_fechamento")
        self.dt_fechamento.setGeometry(QRect(243, 200, 131, 22))
        self.dt_fechamento.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.label_38 = QLabel(self.dados_pecas)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(93, 202, 151, 16))
        font4 = QFont()
        font4.setBold(False)
        font4.setWeight(50)
        self.label_38.setFont(font4)
        self.plainTextEdit_2 = QPlainTextEdit(self.dados_pecas)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(10, 50, 364, 81))
        self.label_38.raise_()
        self.label_37.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.txt_tipo.raise_()
        self.label_35.raise_()
        self.sb_qtde.raise_()
        self.label_36.raise_()
        self.txt_preco.raise_()
        self.txt_valor.raise_()
        self.dt_fechamento.raise_()
        self.plainTextEdit_2.raise_()
        self.dados_os = QGroupBox(self.pg_os)
        self.dados_os.setObjectName(u"dados_os")
        self.dados_os.setGeometry(QRect(20, 26, 191, 280))
        self.dados_os.setMaximumSize(QSize(481, 16777215))
        self.dados_os.setFont(font3)
        self.dados_os.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.label_39 = QLabel(self.dados_os)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 30, 73, 16))
        self.label_40 = QLabel(self.dados_os)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 77, 38, 16))
        self.txt_num_os = QLineEdit(self.dados_os)
        self.txt_num_os.setObjectName(u"txt_num_os")
        self.txt_num_os.setGeometry(QRect(10, 50, 81, 20))
        self.txt_num_os.setStyleSheet(u"background-color: rgb(250, 250, 250)")
        self.dt_emissao = QDateEdit(self.dados_os)
        self.dt_emissao.setObjectName(u"dt_emissao")
        self.dt_emissao.setGeometry(QRect(10, 98, 79, 18))
        self.dt_emissao.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.label_41 = QLabel(self.dados_os)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(10, 127, 35, 16))
        self.dt_horario = QTimeEdit(self.dados_os)
        self.dt_horario.setObjectName(u"dt_horario")
        self.dt_horario.setGeometry(QRect(10, 147, 69, 18))
        self.dt_horario.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.label_42 = QLabel(self.dados_os)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 175, 49, 16))
        self.txt_solicitante = QLineEdit(self.dados_os)
        self.txt_solicitante.setObjectName(u"txt_solicitante")
        self.txt_solicitante.setGeometry(QRect(10, 195, 171, 20))
        self.txt_solicitante.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.label_43 = QLabel(self.dados_os)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 222, 121, 16))
        self.txt_responsavel = QLineEdit(self.dados_os)
        self.txt_responsavel.setObjectName(u"txt_responsavel")
        self.txt_responsavel.setGeometry(QRect(10, 242, 171, 20))
        self.txt_responsavel.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.label_44 = QLabel(self.dados_os)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(110, 30, 73, 16))
        self.cb_open = QCheckBox(self.dados_os)
        self.cb_open.setObjectName(u"cb_open")
        self.cb_open.setGeometry(QRect(110, 49, 70, 17))
        self.cb_close = QCheckBox(self.dados_os)
        self.cb_close.setObjectName(u"cb_close")
        self.cb_close.setGeometry(QRect(110, 66, 70, 17))
        self.dados_serv = QGroupBox(self.pg_os)
        self.dados_serv.setObjectName(u"dados_serv")
        self.dados_serv.setGeometry(QRect(20, 310, 385, 238))
        self.dados_serv.setMaximumSize(QSize(481, 16777215))
        self.dados_serv.setFont(font3)
        self.dados_serv.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.label_45 = QLabel(self.dados_serv)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 30, 20, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        self.label_46 = QLabel(self.dados_serv)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(108, 30, 101, 16))
        self.label_47 = QLabel(self.dados_serv)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(246, 30, 111, 16))
        self.label_49 = QLabel(self.dados_serv)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(10, 80, 51, 16))
        self.plainTextEdit = QPlainTextEdit(self.dados_serv)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(11, 100, 363, 123))
        self.cb_tipo = QComboBox(self.dados_serv)
        self.cb_tipo.addItem("")
        self.cb_tipo.addItem("")
        self.cb_tipo.setObjectName(u"cb_tipo")
        self.cb_tipo.setGeometry(QRect(11, 51, 88, 20))
        sizePolicy.setHeightForWidth(self.cb_tipo.sizePolicy().hasHeightForWidth())
        self.cb_tipo.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(8)
        self.cb_tipo.setFont(font5)
        self.cb_tipo.setAutoFillBackground(False)
        self.cb_tipo.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.cb_tipo.setEditable(True)
        self.cb_tipo.setIconSize(QSize(16, 16))
        self.cb_tipo.setDuplicatesEnabled(False)
        self.cb_tipo.setFrame(True)
        self.dt_inicio = QDateTimeEdit(self.dados_serv)
        self.dt_inicio.setObjectName(u"dt_inicio")
        self.dt_inicio.setGeometry(QRect(108, 51, 127, 20))
        self.dt_inicio.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.dt_termino = QDateTimeEdit(self.dados_serv)
        self.dt_termino.setObjectName(u"dt_termino")
        self.dt_termino.setGeometry(QRect(246, 51, 127, 20))
        self.dt_termino.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.Pages.addWidget(self.pg_os)
        self.dados_serv.raise_()
        self.btn_gravar.raise_()
        self.btn_sair.raise_()
        self.dados_equip.raise_()
        self.dados_pecas.raise_()
        self.dados_os.raise_()
        self.pg_consultar = QWidget()
        self.pg_consultar.setObjectName(u"pg_consultar")
        self.groupBox = QGroupBox(self.pg_consultar)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(22, 20, 800, 131))
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.txt_num_os_consulta = QLineEdit(self.frame_2)
        self.txt_num_os_consulta.setObjectName(u"txt_num_os_consulta")

        self.horizontalLayout_9.addWidget(self.txt_num_os_consulta)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)

        self.txt_num_patrimonio_consulta = QLineEdit(self.frame_2)
        self.txt_num_patrimonio_consulta.setObjectName(u"txt_num_patrimonio_consulta")

        self.horizontalLayout_10.addWidget(self.txt_num_patrimonio_consulta)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_14.addWidget(self.label_19)

        self.txt_solicitante_consulta = QLineEdit(self.frame_2)
        self.txt_solicitante_consulta.setObjectName(u"txt_solicitante_consulta")

        self.horizontalLayout_14.addWidget(self.txt_solicitante_consulta)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_15.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.cb_status_consulta = QComboBox(self.frame_3)
        self.cb_status_consulta.addItem("")
        self.cb_status_consulta.addItem("")
        self.cb_status_consulta.setObjectName(u"cb_status_consulta")

        self.horizontalLayout_13.addWidget(self.cb_status_consulta)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.dt_periodo_consulta = QDateEdit(self.frame_3)
        self.dt_periodo_consulta.setObjectName(u"dt_periodo_consulta")

        self.horizontalLayout_11.addWidget(self.dt_periodo_consulta)

        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_18)

        self.dateEdit_2 = QDateEdit(self.frame_3)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.horizontalLayout_11.addWidget(self.dateEdit_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.txt_equipamento_consulta = QLineEdit(self.frame_3)
        self.txt_equipamento_consulta.setObjectName(u"txt_equipamento_consulta")

        self.horizontalLayout_12.addWidget(self.txt_equipamento_consulta)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_15.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_20)


        self.horizontalLayout_15.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.pg_consultar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(22, 530, 801, 70))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 100, 150);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_consultar = QPushButton(self.frame_5)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setFont(font2)
        self.btn_consultar.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(140, 205, 135);\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 100, 150)\n"
"\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_consultar)

        self.btn_excluir = QPushButton(self.frame_5)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setFont(font2)
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(200, 70, 100);\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 100, 150)\n"
"\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_excluir)

        self.treeWidget = QTreeWidget(self.pg_consultar)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(22, 160, 800, 360))
        font6 = QFont()
        font6.setKerning(True)
        self.treeWidget.setFont(font6)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setMinimumSectionSize(40)
        self.treeWidget.header().setDefaultSectionSize(115)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setStretchLastSection(False)
        self.Pages.addWidget(self.pg_consultar)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_3 = QVBoxLayout(self.pg_home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        font7 = QFont()
        font7.setFamily(u"Montserrat Medium")
        self.label.setFont(font7)
        self.label.setStyleSheet(u"background-color: rgb(0, 100, 150);")

        self.verticalLayout_3.addWidget(self.label)

        self.btn_pg_cadastro = QPushButton(self.pg_home)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setFont(font1)
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(249, 196, 48);\n"
"	color: rgb(0, 100, 150);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 100, 150)\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_pg_cadastro)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_2 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")
        font8 = QFont()
        font8.setFamily(u"Microsoft JhengHei")
        font8.setPointSize(20)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet(u"background-color: rgb(0, 100, 150);\n"
"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_4 = QLabel(self.pg_cadastro)
        self.label_4.setObjectName(u"label_4")
        font9 = QFont()
        font9.setFamily(u"Microsoft JhengHei")
        font9.setPointSize(11)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_4.setFont(font9)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.pg_cadastro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setFont(font)
        self.txt_nome.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.horizontalLayout_4.addWidget(self.txt_nome)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font10 = QFont()
        font10.setFamily(u"Microsoft JhengHei")
        font10.setPointSize(10)
        self.label_6.setFont(font10)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.horizontalLayout_5.addWidget(self.txt_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font10)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font10)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setFont(font)
        self.txt_senha_2.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font10)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setFont(font)
        self.cb_perfil.setStyleSheet(u"background-color: rgb(240, 240, 240);")

        self.horizontalLayout_3.addWidget(self.cb_perfil)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_14)

        self.frame = QFrame(self.pg_cadastro)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 100, 150);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(249, 196, 48);\n"
"	color: rgb(0, 100, 150);\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 100, 150)\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_cadastrar)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages.addWidget(self.pg_cadastro)
        self.frame.raise_()
        self.label_12.raise_()
        self.label_4.raise_()
        self.label_14.raise_()

        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"Gerar O.S", None))
        self.btn_consultar_os.setText(QCoreApplication.translate("MainWindow", u"Consultar O.S", None))
        self.btn_gravar.setText(QCoreApplication.translate("MainWindow", u"Gravar", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.dados_equip.setTitle(QCoreApplication.translate("MainWindow", u"Dados do equipamento", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de patrim\u00f4nio", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Equipamento", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Defeito / problema", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Acess\u00f3rios", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None))
        self.dados_pecas.setTitle(QCoreApplication.translate("MainWindow", u"Dados das pe\u00e7as", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o das pe\u00e7as utilizadas", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Qtde", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o unit\u00e1rio", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Valor total", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Data / Hor\u00e1rio de Fechamento", None))
        self.dados_os.setTitle(QCoreApplication.translate("MainWindow", u"Dados gerais da ordem de servi\u00e7o", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"N\u00famero da O.S", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Emiss\u00e3o", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Solicitante", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Respons\u00e1vel pelo servi\u00e7o", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.cb_open.setText(QCoreApplication.translate("MainWindow", u"Aberta", None))
        self.cb_close.setText(QCoreApplication.translate("MainWindow", u"Fechada", None))
        self.dados_serv.setTitle(QCoreApplication.translate("MainWindow", u"Dados do servi\u00e7o", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Data / Hor\u00e1rio in\u00edcio", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Data / Hor\u00e1rio t\u00e9rmino", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Atividade", None))
        self.cb_tipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Reparo", None))
        self.cb_tipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Substitui\u00e7\u00e3o", None))

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es de consulta", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"N\u00famero da O.S", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de patrim\u00f4nio", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Solicitante", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.cb_status_consulta.setItemText(0, QCoreApplication.translate("MainWindow", u"Aberta", None))
        self.cb_status_consulta.setItemText(1, QCoreApplication.translate("MainWindow", u"Fechada", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"at\u00e9", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Equipamento", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">AAAAAAAAAAAAAAAAAAAAAAAAAAAAA</span></p></body></html>", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"CONSULTAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Valor total", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Emiss\u00e3o", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Equipamento", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"N\u00ba do patrim\u00f4nio", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Solicitante", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"N\u00ba da O.S", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body></p><p align=\"center\"><p align=\"center\"><img src=\"SIMAP.png\" width=\"300\"><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Sistema de Manuten\u00e7\u00e3o de Patrim\u00f4nio</span><br/></p></body></html>", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tela de Cadastro", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USU\u00c1RIO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome</span><span style=\" font-size:10pt; color:#ffffff;\">ie</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Senha<span style=\" color:#ffffff;\">ie</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Senha<span style=\" color:#ffffff;\">ie</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_14.setText("")
        self.label_2.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_3.setText("")
    # retranslateUi

