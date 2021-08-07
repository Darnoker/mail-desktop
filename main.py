import sys

from PyQt5 import QtWidgets

from models.EmailAccount import EmailAccount
from services.EmailService import EmailService
from services.LoginService import LoginService
from view.ViewHandler import ViewHandler

# declare variable app.
app = QtWidgets.QApplication(sys.argv)

# declare viewHandler to manage our view.
viewHandler = ViewHandler()
viewHandler.showLoginWindow()

# exit app
sys.exit(app.exec_())
