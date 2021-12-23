import email
import html2text

from PyQt5.QtCore import QThread

# Class that fetches message contents from emails.
class FetchMessagesService(QThread):
    def __init__(self, emailAccount, messageID):
        super().__init__()
        self.emailAccount = emailAccount
        self.messageID = messageID

    def run(self):
        # fetching message body
        response = self.emailAccount.mail.fetch(self.messageID, ['RFC822', 'BODY[TEXT]'])
        # iterating through dictionary
        for message_id, message_data in response.items():
            # parsing email
            parsedEmail = email.message_from_bytes(message_data[b'RFC822'])
            if parsedEmail.is_multipart():
                for part in parsedEmail.walk():
                    if part.get_content_type() == 'text/plain':
                        # decoding message
                        self.message = part.get_payload(decode=True).decode('utf-8')
            # if message is html
            else:
                text = f"{parsedEmail.get_payload(decode=True).decode('utf-8')}"
                html = text.replace("b'", "")
                h = html2text.HTML2Text()
                h.ignore_links = True
                output = (h.handle(f'''{html}''').replace("\\r\\n", ""))
                self.message = output.replace("'", "")

