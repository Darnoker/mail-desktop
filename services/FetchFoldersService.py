from PyQt5.QtCore import QThread

from models.StandardItem import StandardItem


def isInList(list_, string):
    for i in range(len(list_)):
        if string == list_[i][-1]:
            return True

    return False


class FetchFoldersService(QThread):
    def __init__(self, treeItem, emailAccount, emailManager):
        super().__init__()
        self.foldersRoot = treeItem
        self.emailAccount = emailAccount
        self.emailManager = emailManager
        self.foldersList = []


    def run(self):
        has_children = b'\\HasChildren'
        no_select = b'\\Noselect'
        continue_ = False
        list_ = list()
        for folder in self.emailAccount.mail.list_folders():
            select_ = False
            _tuple = folder[0]
            for i in range(len(_tuple)):
                if _tuple[i] == no_select:
                    select_ = False
                else:
                    select_ = True

            if select_:
                self.foldersList.append(folder[-1])
            children = False
            flags = folder[0]

            for i in range(len(flags)):
                if flags[i] == has_children:
                    children = True

            if children:
                node = StandardItem()
                node.setSelectable(False)
                rootFolder = folder[-1]
                list_ = self.emailAccount.mail.list_sub_folders(rootFolder)
                for i in range(len(list_)):
                    if i == 0:
                        node.setText(folder[-1])
                        self.foldersRoot.appendRow(node)
                    else:
                        split = list_[i][-1].split('/')
                        sub_node = StandardItem(split[-1])
                        node.appendRow(sub_node)
            else:
                continue_ = isInList(list_, folder[-1])
                if continue_:
                    split = folder[-1].split('/')
                    self.emailManager.folderDict[split[-1]] = folder[-1]
                    continue
                else:
                    self.emailManager.folderDict[folder[-1]] = folder[-1]
                    node = StandardItem(folder[-1])
                    self.foldersRoot.appendRow(node)


