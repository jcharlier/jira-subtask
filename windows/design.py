# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jcharlier/Mobly/Projetos/jira-subtask/windows/design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menu_first_area_2 = QtWidgets.QWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_first_area_2.sizePolicy().hasHeightForWidth())
        self.menu_first_area_2.setSizePolicy(sizePolicy)
        self.menu_first_area_2.setMinimumSize(QtCore.QSize(0, 20))
        self.menu_first_area_2.setObjectName("menu_first_area_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menu_first_area_2)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, 1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_start = QtWidgets.QPushButton(self.menu_first_area_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.btn_stop = QtWidgets.QPushButton(self.menu_first_area_2)
        self.btn_stop.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy)
        self.btn_stop.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.verticalLayout_3.addWidget(self.menu_first_area_2)
        self.verticalLayout.addWidget(self.verticalWidget)
        self.stories_area = QtWidgets.QHBoxLayout()
        self.stories_area.setObjectName("stories_area")
        self.stories_vertical_separator = QtWidgets.QVBoxLayout()
        self.stories_vertical_separator.setContentsMargins(-1, 0, 0, 0)
        self.stories_vertical_separator.setSpacing(6)
        self.stories_vertical_separator.setObjectName("stories_vertical_separator")
        self.stories_label = QtWidgets.QLabel(self.centralwidget)
        self.stories_label.setObjectName("stories_label")
        self.stories_vertical_separator.addWidget(self.stories_label)
        self.stories_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.stories_label_2.setObjectName("stories_label_2")
        self.stories_vertical_separator.addWidget(self.stories_label_2)
        self.stories_data = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stories_data.sizePolicy().hasHeightForWidth())
        self.stories_data.setSizePolicy(sizePolicy)
        self.stories_data.setObjectName("stories_data")
        self.stories_vertical_separator.addWidget(self.stories_data)
        self.stories_area.addLayout(self.stories_vertical_separator)
        self.verticalLayout.addLayout(self.stories_area)
        self.log_area = QtWidgets.QHBoxLayout()
        self.log_area.setObjectName("log_area")
        self.log_vertical_separator = QtWidgets.QVBoxLayout()
        self.log_vertical_separator.setContentsMargins(-1, 0, 0, 0)
        self.log_vertical_separator.setSpacing(6)
        self.log_vertical_separator.setObjectName("log_vertical_separator")
        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setObjectName("log_label")
        self.log_vertical_separator.addWidget(self.log_label)
        self.log_entries = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_entries.sizePolicy().hasHeightForWidth())
        self.log_entries.setSizePolicy(sizePolicy)
        self.log_entries.setObjectName("log_entries")
        self.log_vertical_separator.addWidget(self.log_entries)
        self.log_area.addLayout(self.log_vertical_separator)
        self.verticalLayout.addLayout(self.log_area)
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout.addWidget(self.progress_bar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 527, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionLista_de_Usu_rios = QtWidgets.QAction(MainWindow)
        self.actionLista_de_Usu_rios.setObjectName("actionLista_de_Usu_rios")
        self.actionCredenciais_JIRA = QtWidgets.QAction(MainWindow)
        self.actionCredenciais_JIRA.setObjectName("actionCredenciais_JIRA")
        self.actionLimpar_Log = QtWidgets.QAction(MainWindow)
        self.actionLimpar_Log.setObjectName("actionLimpar_Log")
        self.menuMenu.addAction(self.actionLimpar_Log)
        self.menuMenu.addAction(self.actionCredenciais_JIRA)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSair)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.actionSair.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JIRA Subtask"))
        self.btn_start.setText(_translate("MainWindow", "Iniciar"))
        self.btn_stop.setText(_translate("MainWindow", "Parar"))
        self.stories_label.setText(_translate("MainWindow", "Paste from spreadsheet without header:"))
        self.stories_label_2.setText(_translate("MainWindow", "Format: | Parent Story | Title | Description | DEV Points | QA Points |"))
        self.log_label.setText(_translate("MainWindow", "Log"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionSair.setText(_translate("MainWindow", "&Sair"))
        self.actionSair.setToolTip(_translate("MainWindow", "Sair deste maravilhoso programa"))
        self.actionSair.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionLista_de_Usu_rios.setText(_translate("MainWindow", "Lista de Usuários"))
        self.actionLista_de_Usu_rios.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionCredenciais_JIRA.setText(_translate("MainWindow", "Credenciais JIRA"))
        self.actionCredenciais_JIRA.setShortcut(_translate("MainWindow", "Ctrl+J"))
        self.actionLimpar_Log.setText(_translate("MainWindow", "&Limpar Log"))
        self.actionLimpar_Log.setShortcut(_translate("MainWindow", "Ctrl+L"))

