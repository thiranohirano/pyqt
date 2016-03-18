import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QApplication

from ui_button import Ui_Form


class ExampleApp(QtGui.QWidget, Ui_Form.Ui_Form):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
