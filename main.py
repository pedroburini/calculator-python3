import sys

from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH
from buttons import ButtonsGrid

if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # define icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    # display
    display = Display()
    window.addWidgetToVLayout(display)

    # grid
    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)

    # execute all
    window.adjustFixedSize()
    window.show()
    app.exec()
