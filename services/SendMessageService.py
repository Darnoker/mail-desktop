import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PyQt5.QtCore import QThread


class SendMessageService(QThread):
    def __init__(self, emailAccount, name, to_emails, subject, message):
        super().__init__()
        self.emailAccount = emailAccount
        self.from_email = name + ' <' + emailAccount.address + '>'
        self.to_emails = to_emails
        self.subject = subject
        self.message = message

    def run(self):
        assert isinstance(self.to_emails, list)

        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ", ".join(self.to_emails)
        msg['Subject'] = self.subject

        textPart = MIMEText(self.message)
        msg.attach(textPart)
        msg_str = msg.as_string()

        server = smtplib.SMTP(self.emailAccount.properties.get("outgoingHost"), 587)
        server.ehlo()
        server.starttls()
        server.login(self.emailAccount.address, self.emailAccount.password)
        server.sendmail(self.from_email,self.to_emails,msg_str)
        server.quit()



