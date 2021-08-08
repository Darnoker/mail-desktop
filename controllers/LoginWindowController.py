class LoginWindowController:
    def __init__(self, loginWindow):
        self.loginWindow = loginWindow

    def loginButtonAction(self):
        if self.checkFields():
            self.loginWindow.viewHandler.showMainWindow()
            self.loginWindow.viewHandler.closeLoginWindow()

    def checkFields(self):
        if not self.loginWindow.emailAdressField.text():
            self.loginWindow.errorLabel.setText("Email Address field is empty!")
            return False
        if not self.loginWindow.passwordField.text():
            self.loginWindow.errorLabel.setText("Password field is empty!")
            return False

        return True
