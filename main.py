import sys
import UiExt
from PyQt5.QtWidgets import QApplication, QMainWindow

from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Base = declarative_base()
    MainWindow = QMainWindow()
    ui = UiExt.UiExt()
    ui.setupUi(MainWindow)

    ui.func()
    MainWindow.show()

    sys.exit(app.exec_())