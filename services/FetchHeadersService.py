from email.header import decode_header

from PyQt5.QtCore import QThread


def decode(header):
    if isinstance(header, bytes):
        decoded = header.decode('utf-8')
        return decoded
    else:
        return header

class FetchHeadersService(QThread):
    def __init__(self, folder):
        super().__init__()
        self.folder = folder
        self.emailAccount = None

    def setAccount(self, emailAccount):
        self.emailAccount = emailAccount


    def run(self, folder):
        self.emailAccount.mail.select_folder(folder, readonly=True)
        messages = self.emailAccount.mail.search('ALL')
        for uid, message_data in self.emailAccount.mail.fetch(messages, ['ENVELOPE']).items():
            envelope = message_data[b'ENVELOPE']
            # decoding subject
            subject_ = envelope.subject.decode('utf-8')
            subject_ = decode(decode_header(subject_)[0][0])
            # decoding sender
            sender_ = envelope.sender[0].name.decode('utf-8')
            sender_ = decode(decode_header(sender_)[0][0])
            # decoding mailbox and getting host
            mailbox = envelope.sender[0].mailbox.decode('utf-8')
            host = envelope.sender[0].host
            if host is not None:
                host = host.decode('utf-8')
                # getting email string
                email_ = mailbox + "@" + host
            else:
                # replacing sender and mailbox
                sender_ = mailbox[3:-3]
                mailbox = sender_[1:-1].replace('@', ' by ').replace('=', '@')





