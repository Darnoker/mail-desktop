import traceback


class LoginService:
    def __init__(self, emailAccount):
        self.emailAccount = emailAccount

    def login_(self):
        try:
            self.emailAccount.mail.login(self.emailAccount.address, self.emailAccount.password)
        except Exception as e:
            traceback.print_exc()
            print(str(e))
