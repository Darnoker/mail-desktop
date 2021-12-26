# -*- coding: utf-8 -*-

import traceback


# Class, that is used to manage login actions.
from PyQt5 import QtCore

# Class that uses multi-threading for logging in.
class LoginService(QtCore.QThread):
    def __init__(self, emailAccount, loginWindowController):
        super().__init__()
        self.emailAccount = emailAccount
        self.loginWindowController = loginWindowController
        self.FLAG = False

    def run(self):
        try:
            self.emailAccount.mail.login(self.emailAccount.address, self.emailAccount.password)
            self.FLAG = True
        except Exception as e:
            traceback.print_exc()
            print(str(e))
            self.loginWindowController.errorLabel.setText("Invalid username or password!")
            self.FLAG = False

