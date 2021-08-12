# -*- coding: utf-8 -*-

import traceback


# Class, that is used to manage login actions.
class LoginService:
    def __init__(self, emailAccount, loginWindow):
        self.emailAccount = emailAccount
        self.loginWindow = loginWindow

    def login_(self):
        try:
            self.emailAccount.mail.login(self.emailAccount.address, self.emailAccount.password)
            return True
        except Exception as e:
            traceback.print_exc()
            print(str(e))
            self.loginWindow.errorLabel.setText("Invalid username or password!")
            return False
