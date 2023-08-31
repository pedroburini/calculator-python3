import sys

from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    window = MainWindow()

    # define icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # execute all
    window.adjustFixedSize()
    window.show()
    app.exec()
