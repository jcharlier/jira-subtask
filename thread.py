#!/usr/bin/env python3
"""Class for threaded jira connection and to add tasks and save your life"""

from PyQt5.QtCore import QThread, pyqtSignal
from jira import JIRA

class Thread(QThread):
    '''Threaded process to send data to jira'''
    add_log_post = pyqtSignal(str)
    set_progress_bar = pyqtSignal(int, int)

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
        ''' main process that reads task list, connects to jira, and creates
        every DEV and QA task'''
        if not self.config['project_key']:
            self.add_log_post.emit("Por favor defina uma chave de projeto")
            self.stop()

        self.add_log_post.emit(u'Conectando no Jira...')
        self.jira = JIRA(self.options, basic_auth=(
            self.config['jira_user'], self.config['jira_token']))
        for task in self.task_list:
            last_dev_key = None
            if isinstance(task["devpts"], (int, float))  and task["devpts"] >= 0:
                self.add_log_post.emit("Adding Dev Task: ")
                self.add_log_post.emit("+-- Parent: {}".format(task["parent"]))
                self.add_log_post.emit("+-- Title : {}".format(task["title"]))
                self.add_log_post.emit("+-- Points: {}".format(task["devpts"]))
                self.add_log_post.emit("+-- Descri: {}".format(task["desc"]))
                rootnn_dict = {
                    'project': {'key': self.config["project_key"]},
                    'summary': "DEV - {}".format(str(task["title"])),
                    'description': str(task["desc"]),
                    'customfield_10004': int(task["devpts"]),
                    'issuetype': {'name': 'Development Task'},
                    'parent': {'key': str(task["parent"])}
                }
                try:
                    print("dev")
                    print(rootnn_dict)
                    child = self.jira.create_issue(fields=rootnn_dict)
                    last_dev_key = child.key
                    self.add_log_post.emit("+-- SubTask Key: {}".format(child.key))
                except Exception as error:
                    self.add_log_post.emit("{}".format(error))
                    self.stop()
                self.add_log_post.emit(" ")

                # QA Task
            if isinstance(task["qapts"], (int, float)) and task["qapts"] >= 0:
                self.add_log_post.emit("Adding QA Task: ")
                self.add_log_post.emit("+-- Parent: {}".format(task["parent"]))
                self.add_log_post.emit("+-- Title : {}".format(task["title"]))
                self.add_log_post.emit("+-- Points: {}".format(task["qapts"]))
                self.add_log_post.emit("+-- Descri: {}".format(task["desc"]))
                rootnn_dict = {
                    'project': {'key': self.config["project_key"]},
                    'summary': "QA - {}".format(str(task["title"])),
                    'description': str(task["desc"]),
                    'customfield_10004': int(task["qapts"]),
                    'issuetype': {'name': 'QA Task'},
                    'parent': {'key': str(task["parent"])}
                }
                try:
                    print("qa")
                    child = self.jira.create_issue(fields=rootnn_dict)
                    self.add_log_post.emit("+-- SubTask Key: {}".format(child.key))
                except Exception as error:
                    self.add_log_post("{}".format(error))
                if last_dev_key:
                    try:
                        self.jira.create_issue_link(
                            type="depended by",
                            inwardIssue=child.key,
                            outwardIssue=last_dev_key
                        )
                    except Exception as error:
                        self.add_log_post("{}".format(error))
                self.add_log_post.emit(" ")
