#!/usr/bin/env python3
"""Class for threaded jira connection and to add tasks and save your life"""

from PyQt5.QtCore import QThread, pyqtSignal
from jira import JIRA

class Thread(QThread):
    '''Threaded process to send data to jira'''
    add_log_post = pyqtSignal(str)
    set_progress_bar = pyqtSignal(int, int)
    # save_report = pyqtSignal('PyQt_PyObject')

    def __init__(self, task_list, config):
        self.config = config
        self.task_list = task_list
        self.options = {'server': self.config["jira_base_url"]}
        self.jira = ""
        QThread.__init__(self)

    def stop(self):
        ''' kills all threads '''
        self.terminate()

    def run(self):
        ''' main process that connects to jira, downloads worklog list
        download extra task information and saves the report to csv when done
        also alerting the user if there is any story with no epic association'''
        self.add_log_post.emit(u'Conectando no Jira...')
        self.jira = JIRA(self.options, basic_auth=(
            self.config['jira_user'], self.config['jira_token']))

        for task in self.task_list.T.iteritems():
            if isinstance(task[1].devpts, (int, float))  and task[1].devpts >= 0:
                self.add_log_post.emit("Adding Dev Task: ")
                self.add_log_post.emit("+-- Parent: {}".format(task[1].parent))
                self.add_log_post.emit("+-- Title : {}".format(task[1].title))
                self.add_log_post.emit("+-- Points: {}".format(task[1].devpts))
                self.add_log_post.emit("+-- Descri: {}".format(task[1].desc))
                rootnn_dict = {
                    'project': {'key': 'PPER'},
                    'summary': "DEV - {}".format(str(task[1].title)),
                    'description': str(task[1].desc),
                    'customfield_10004': int(task[1].devpts),
                    'issuetype': {'name': 'Development Task'},
                    'parent': {'key': str(task[1].parent)}
                }
                try:
                    child = self.jira.create_issue(fields=rootnn_dict)
                    self.add_log_post.emit("+-- SubTask Key: {}".format(child.key))
                except Exception as error:
                    self.add_log_post("{}".format(error))
                self.add_log_post.emit(" ")

                # QA Task
            if isinstance(task[1].qapts, (int, float)) and task[1].qapts >= 0:
                self.add_log_post.emit("Adding QA Task: ")
                self.add_log_post.emit("+-- Parent: {}".format(task[1].parent))
                self.add_log_post.emit("+-- Title : {}".format(task[1].title))
                self.add_log_post.emit("+-- Points: {}".format(task[1].qapts))
                self.add_log_post.emit("+-- Descri: {}".format(task[1].desc))
                rootnn_dict = {
                    'project': {'key': 'PPER'},
                    'summary': "QA - {}".format(str(task[1].title)),
                    'description': str(task[1].desc),
                    'customfield_10004': int(task[1].qapts),
                    'issuetype': {'name': 'QA Task'},
                    'parent': {'key': str(task[1].parent)}
                }
                try:
                    child = self.jira.create_issue(fields=rootnn_dict)
                    self.add_log_post.emit("+-- SubTask Key: {}".format(child.key))
                except Exception as error:
                    self.add_log_post("{}".format(error))
                self.add_log_post.emit(" ")
