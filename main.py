# coding:utf-8

from PyQt4 import QtGui, QtCore  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import os
import mainwindow  # This file holds our MainWindow and all design related things


# it also keeps events etc that we defined in Qt Designer

class ExampleApp(QtGui.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.toolbar = QtGui.QToolBar()
        exit_action = QtGui.QAction("閉じる", self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(QtGui.qApp.quit)
        self.toolbar.addAction(exit_action)
        self.addToolBar(self.toolbar)

        self.pushButton.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.listWidget.clear()
        # In case there are any existing elements in the list
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if directory:  # if user didn't pick a directory don't continue
            for file_name in os.listdir(directory):  # for all files, if any, in the directory
                self.listWidget.addItem(file_name.encode('utf-8'))  # add file to the listWidget


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
