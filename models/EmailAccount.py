import imaplib


# Class, that defines an email account of user.
class EmailAccount:
    def __init__(self, address, password):
        self.address = address
        self.password = password
        self.properties = {
            "incomingHost": "imap.gmail.com",
            "outgoingHost": "smtp.gmail.com"
        }
        self.mail = imaplib.IMAP4_SSL(self.properties.get("incomingHost"))
