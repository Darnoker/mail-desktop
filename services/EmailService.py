# -*- coding: utf-8 -*-

# Class, used to manage email actions.

from models.StandardItem import StandardItem


class EmailService:
    def __init__(self, emailAccount):
        self.emailAccount = emailAccount

    def getFolders(self, mailName):
        for folders in self.emailAccount.mail.list_folders():
            split = folders[-1].split('/')
            mailName.appendRow(StandardItem(split[-1]))

    # function that may be used in the future (?)
    # def fetchFolders(self):
    #     self.emailAccount.mail.select('inbox')
    #     data = self.emailAccount.mail.search(None, 'ALL')
    #     mail_ids = data[1]
    #     id_list = mail_ids[0].split()
    #     first_email_id = int(id_list[0])
    #     last_email_id = int(id_list[-1])
    #
    #     for i in range(last_email_id, first_email_id, -1):
    #         data_ = self.emailAccount.mail.fetch(str(i), '(RFC822)')
    #         for response_part in data_:
    #             arr = response_part[0]
    #             if isinstance(arr, tuple):
    #                 msg = email.message_from_string(str(arr[1], 'utf-8'))
    #                 email_subject = msg['subject']
    #                 email_from = msg['from']
    #                 print('From: ' + email_from + '\n')
    #                 print('Subject: ' + email_subject + '\n')
