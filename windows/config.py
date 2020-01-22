# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfigWindow(object):
    def setupUi(self, ConfigWindow):
        ConfigWindow.setObjectName("ConfigWindow")
        ConfigWindow.resize(555, 210)
        ConfigWindow.setMinimumSize(QtCore.QSize(555, 210))
        ConfigWindow.setMaximumSize(QtCore.QSize(555, 210))
        self.centralwidget = QtWidgets.QWidget(ConfigWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.jira_email_label = QtWidgets.QLabel(self.centralwidget)
        self.jira_email_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.jira_email_label.setObjectName("jira_email_label")
        self.horizontalLayout.addWidget(self.jira_email_label)
        self.jira_email_text = QtWidgets.QTextEdit(self.centralwidget)
        self.jira_email_text.setMaximumSize(QtCore.QSize(465, 30))
        self.jira_email_text.setObjectName("jira_email_text")
        self.horizontalLayout.addWidget(self.jira_email_text)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.jira_token_label = QtWidgets.QLabel(self.centralwidget)
        self.jira_token_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.jira_token_label.setOpenExternalLinks(True)
        self.jira_token_label.setObjectName("jira_token_label")
        self.horizontalLayout_2.addWidget(self.jira_token_label)
        self.jira_token_text = QtWidgets.QTextEdit(self.centralwidget)
        self.jira_token_text.setMaximumSize(QtCore.QSize(465, 30))
        self.jira_token_text.setObjectName("jira_token_text")
        self.horizontalLayout_2.addWidget(self.jira_token_text)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.jira_url_label = QtWidgets.QLabel(self.centralwidget)
        self.jira_url_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.jira_url_label.setObjectName("jira_url_label")
        self.horizontalLayout_4.addWidget(self.jira_url_label)
        self.jira_url_text = QtWidgets.QTextEdit(self.centralwidget)
        self.jira_url_text.setMaximumSize(QtCore.QSize(465, 30))
        self.jira_url_text.setObjectName("jira_url_text")
        self.horizontalLayout_4.addWidget(self.jira_url_text)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 4000, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        ConfigWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ConfigWindow)
        self.statusbar.setObjectName("statusbar")
        ConfigWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ConfigWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfigWindow)

    def retranslateUi(self, ConfigWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfigWindow.setWindowTitle(_translate("ConfigWindow", "Configurações"))
        self.label_3.setText(_translate("ConfigWindow", "Configurações"))
        self.label_4.setText(_translate("ConfigWindow", "Credenciais do JIRA"))
        self.jira_email_label.setText(_translate("ConfigWindow", "email"))
        self.jira_token_label.setText(_translate("ConfigWindow", "<a href=\"https://id.atlassian.com/manage/api-tokens\">jira token</a>"))
        self.jira_url_label.setText(_translate("ConfigWindow", "jira url"))
