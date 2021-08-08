from models.EmailAccount import EmailAccount
from services.LoginService import LoginService


class LoginWindowController:
    def __init__(self, loginWindow):
        self.loginWindow = loginWindow
        self.emailAccount = None
        self.loginService = None

    def loginButtonAction(self):
        if self.checkFields():
            self.emailAccount = EmailAccount(self.loginWindow.emailAdressField.text(),
                                             self.loginWindow.passwordField.text())
            
            self.loginService = LoginService(self.emailAccount, self.loginWindow)

            if self.loginService.login_() and self.checkFields():
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
