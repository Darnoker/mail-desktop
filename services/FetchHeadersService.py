from email.header import decode_header

from PyQt5.QtCore import QThread


def decode(header):
    if isinstance(header, bytes):
        decoded = header.decode('utf-8')
        return decoded
    else:
        return header


class FetchHeadersService(QThread):
    def __init__(self, emailAccount, folder, emailManager):
        super().__init__()
        self.emailAccount = emailAccount
        self.folder = folder
        self.emailManager = emailManager
        self.senderList = []
        self.subjectList = []
        self.emailList = []
        self.idList = []
        self.idDict = {}

    def addToList(self, messageID, sender_, email_, subject_):
        self.idList.append(messageID)
        self.senderList.append(sender_)
        self.emailList.append(email_)
        self.subjectList.append(subject_)

    def run(self):
        self.emailAccount.mail.select_folder(self.emailManager.folderDict[self.folder], readonly=True)
        messages = self.emailAccount.mail.search('ALL')
        self.messageNumber = len(messages)
        for messageID, message_data in self.emailAccount.mail.fetch(messages, ['ENVELOPE']).items():
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
                self.addToList(messageID, sender_, email_, subject_)
                # print("ID: ", message_id, "From: ", sender_, "EMAIL: ", email_, " SUBJECT: ", subject_)
            else:
                # checking other variation of sender
                if sender_[0] != '<':
                    split_sender = sender_.split(' ')
                    sender_ = mailbox + ' ' + split_sender[0]
                    email_ = split_sender[1][1:-1].replace('@', ' by ').replace('=', '@')
                    self.addToList(messageID, sender_, email_, subject_)
                    # print("ID: ", message_id, "From: ", sender_, "EMAIL: ", email_, " SUBJECT: ", subject_)

                else:
                    email_ = sender_[1:-1].replace('@', ' by ').replace('=', '@')
                    sender_ = mailbox[3:-3]
                    self.addToList(messageID, sender_, email_, subject_)
                    # print("ID: ", message_id, "From: ", sender_, "EMAIL: ", email_, " SUBJECT: ", subject_)

        j = self.messageNumber - 1
        for i in range(self.messageNumber):
            i = i + 1
            self.idDict[i] = self.idList[j]
            j = j - 1
