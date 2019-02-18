#!/usr/bin/env python3
"""This script helps the poor dev lead create subtasks in jira for every new sprint"""
# -*- coding: utf-8 -*-
# coding: utf-8
import sys
import json
import os
from thread import Thread
from PyQt5 import QtWidgets, QtGui
from bs4 import BeautifulSoup, Comment
from windows import design
from windows import config


class ConfigWindow(QtWidgets.QMainWindow, config.Ui_ConfigWindow):
    """Configuration Window """

    def __init__(self, parent=None):
        super(ConfigWindow, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.jira_email_text.setHtml(self.parent.config['jira_user'].strip())
        self.jira_token_text.setHtml(self.parent.config['jira_token'].strip())
        self.jira_url_text.setHtml(self.parent.config['jira_base_url'].strip())
        self.jira_email_text.textChanged.connect(self._update_config)
        self.jira_token_text.textChanged.connect(self._update_config)
        self.jira_url_text.textChanged.connect(self._update_config)
        self._update_config()

    def _update_config(self):
        self.parent.config['jira_user'] = str(
            self.jira_email_text.toPlainText()).strip()
        self.parent.config['jira_token'] = str(
            self.jira_token_text.toPlainText()).strip()
        self.parent.config['jira_base_url'] = str(
            self.jira_url_text.toPlainText()).strip()
        self.parent.save_configuration()



class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """App main window"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.config = None
        self.config_file_path = os.path.join(os.path.split(
            os.path.abspath(__file__))[0], 'config.json')
        icon = QtGui.QIcon()
        cog_file_path = os.path.join(os.path.split(
            os.path.abspath(__file__))[0], 'cog.png')
        icon.addPixmap(QtGui.QPixmap(cog_file_path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setupUi(self)
        self.report = None
        # self.report_date.setDateTime(QDateTime.currentDateTime())
        self.btn_start.disconnect()
        self.btn_start.clicked.connect(self.create_subtasks)
        self.actionCredenciais_JIRA.disconnect()
        self.actionCredenciais_JIRA.triggered.connect(self.show_configcred)
        self.actionLimpar_Log.disconnect()
        self.actionLimpar_Log.triggered.connect(self.log_entries.clear)
        self._load_configuration()
        self.thread = None
        self.config_window = ConfigWindow(self)

    def _load_configuration(self):
        if os.path.isfile(self.config_file_path):
            with open(self.config_file_path) as config_file:
                self.config = json.load(config_file)
        else:
            self.save_configuration()

    def _check_config(self):
        return (self.config["jira_base_url"] and
                self.config["jira_token"] and
                self.config["jira_user"])

    def save_configuration(self):
        """saves/creates the configuration file"""
        if not os.path.isfile(self.config_file_path):
            if not os.path.isfile(os.path.join(os.path.split(
                    os.path.abspath(__file__))[0], 'config.template.json')):
                self.config = {
                    "jira_base_url": "https://helpdeskmobly.atlassian.net",
                    "jira_token": "",
                    "jira_user": ""}
            else:
                with open(
                    os.path.join(
                        os.path.split(os.path.abspath(__file__))[0],
                        'config.template.json'
                    )
                ) as template_config_file:
                    self.config = json.load(template_config_file)
                    with open(self.config_file_path, 'w') as config_file:
                        json.dump(self.config, config_file,
                                  sort_keys=True, indent=4)

        with open(self.config_file_path, 'r+') as config_file:
            json.dump(self.config, config_file, sort_keys=True, indent=4)

    def show_configcred(self):
        """pops up the configuration window"""
        self.config_window.show()

    def add_log_post(self, log_data):
        """logs message to the board"""
        self.log_entries.append(log_data)
        self.log_entries.moveCursor(QtGui.QTextCursor.End)

    def set_progress_bar(self, value, total):
        """updates progress bar to value"""
        self.progress_bar.setValue(value)
        self.progress_bar.setMaximum(total)

    def create_subtasks(self):
        """Get the data from the table and create each subtask (DEV and QA)"""
        if not self._check_config():
            self.add_log_post("Verifique suas configurações (CTRL+J)")
            return
        self.progress_bar.setValue(0)
        self.log_entries.clear()
        if self.thread is not None and self.thread.isRunning():
            self.thread.stop()
            self.thread = None
            return
        task_list = list()
        raw_html = self.stories_data.toHtml()
        html_data = BeautifulSoup(raw_html, features='lxml')
        for line_break in html_data.find_all("br"):
            line_break.replace_with("\n")

        for row in html_data.findAll('tr'):
            cell = row.findAll('td')
            if len(cell) == 5:
                task = {
                    "parent" : cell[0].text.strip('\n'),
                    "title"  : cell[1].text.strip('\n').replace("\n", " "),
                    "desc"   : cell[2].text.strip('\n'),
                    "devpts" : float(cell[3].text.strip('\n') or 0),
                    "qapts"  : float(cell[4].text.strip('\n')) if cell[4].text.strip('\n') else ""
                }
                task_list.append(task)
            else:
                self.add_log_post(
                    "dá uma olhada na sua tabela, todas as linhas tem que ter 5 colunas: \
                    \n| Parent Story | Title | Description | DEV Points | QA Points |"
                )

        self.thread = Thread(task_list, self.config)
        self.thread.add_log_post.connect(self.add_log_post)
        self.thread.set_progress_bar.connect(self.set_progress_bar)
        self.thread.finished.connect(self.done)
        self.btn_stop.setEnabled(True)
        self.btn_stop.disconnect()
        self.btn_stop.clicked.connect(self.done)
        self.btn_start.setEnabled(False)
        self.thread.start()

    def done(self):
        """Controls UI when thread is done and kills eventual remaining threads"""
        if self.thread is not None and self.thread.isRunning():
            self.thread.stop()
            self.thread = None
        self.btn_stop.setEnabled(False)
        self.btn_start.setEnabled(True)
        self.progress_bar.setValue(0)
        self.add_log_post("Processos e conexões terminadas.")


def main():
    """startup yeah"""
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
