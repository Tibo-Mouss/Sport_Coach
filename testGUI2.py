from PyQt5 import QtCore, QtGui, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.textBrowser = QtWidgets.QTextBrowser()
        self.lineEdit = QtWidgets.QLineEdit()
        button = QtWidgets.QPushButton("Replace Last Line")
        self.textBrowser.append("Stack\nOverflow\nHello\nWorld")
        button.clicked.connect(self.on_clicked)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.textBrowser)
        lay.addWidget(self.lineEdit)
        lay.addWidget(button)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        self.replace_last_line("hi :)")

    def replace_last_line(self, text):
        self.textBrowser.setText(text)
       


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())