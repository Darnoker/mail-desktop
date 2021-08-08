class LoginWindowController:
    def __init__(self, loginWindow):
        self.loginWindow = loginWindow

    def loginButtonAction(self):
        if self.checkFields():
            self.loginWindow.viewHandler.showMainWindow()
            self.loginWindow.viewHandler.closeLoginWindow()

    def checkFields(self):
        if not self.loginWindow.emailAdressField.text():
            print("Email Adress is empty!\n")
            return False
        if not self.loginWindow.passwordField.text():
            print("Password field is empty!\n")
            return False

        return True
