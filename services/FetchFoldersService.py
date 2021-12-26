from PyQt5.QtCore import QThread

from models.StandardItem import StandardItem


def isInList(list_, string):
    for i in range(len(list_)):
        if string == list_[i][-1]:
            return True

    return False

# Class for fetching folders, using multi-threading
class FetchFoldersService(QThread):
    def __init__(self, treeItem, emailAccount, emailManager):
        super().__init__()
        self.foldersRoot = treeItem
        self.emailAccount = emailAccount
        self.emailManager = emailManager
        self.foldersList = []

    def run(self):

        # flags that will be fetched from list_folders()
        has_children = b'\\HasChildren'
        no_select = b'\\Noselect'
        continue_ = False
        list_ = list()
        # fetching list of folders
        for folder in self.emailAccount.mail.list_folders():
            select_ = False
            _tuple = folder[0]
            # checking if there is  b'\\Noselect' flag
            for i in range(len(_tuple)):
                if _tuple[i] == no_select:
                    select_ = False
                else:
                    select_ = True
            # if there is not, add folder to the list
            if select_:
                self.foldersList.append(folder[-1])
            children = False
            flags = folder[0]
            # checking if there is a flag b'\\HasChildren'
            for i in range(len(flags)):
                if flags[i] == has_children:
                    children = True
            # if there is, add folder to tree view and append sub folders to it
            if children:
                node = StandardItem()
                node.setSelectable(False)
                rootFolder = folder[-1]
                list_ = self.emailAccount.mail.list_sub_folders(rootFolder)
                for i in range(len(list_)):
                    # first will be non-selectable
                    if i == 0:
                        node.setText(folder[-1])
                        self.foldersRoot.appendRow(node)
                    else:
                        split = list_[i][-1].split('/')
                        sub_node = StandardItem(split[-1])
                        node.appendRow(sub_node)
            # check if folder is on the list
            else:
                continue_ = isInList(list_, folder[-1])
                # folders are named [GMAIL]/foldername, so split by '/' and add to dict only foldername
                if continue_:
                    split = folder[-1].split('/')
                    self.emailManager.folderDict[split[-1]] = folder[-1]
                    continue
                # if it isn't on the list, add it to tree view
                else:
                    self.emailManager.folderDict[folder[-1]] = folder[-1]
                    node = StandardItem(folder[-1])
                    self.foldersRoot.appendRow(node)


