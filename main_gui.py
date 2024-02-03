import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QSlider, QScrollArea, QPushButton, QLCDNumber, QTableWidgetItem, QMessageBox, QGraphicsView,
                               QGraphicsRectItem, QGraphicsScene, QHBoxLayout, QWidget, QLabel, QGraphicsItem, QVBoxLayout)
# from PySide6.QtCore import QFile, Slot,QDate, QTime, QTimer, QDateTime, Qt, QEvent, QRectF
from PySide6.QtGui import QPalette, QColor, QIntValidator, QBrush, QPen, QPixmap, QIcon
from PySide6.QtUiTools import QUiLoader
# import GUI.open_gui as ui
# import GUI.interface_gui as ui2
from GUI.open_gui import Ui_open_main
from GUI.interface_gui import Ui_interface_main

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from GUI.open_gui import Ui_open_main

class MyMainWindow(QMainWindow, Ui_open_main):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_open_main()
        self.ui.setupUi(self)
        
        self.ui.start_button.clicked.connect(self.interface)
        
    def interface(self):
        print("it is working")
        new_window = InterfaceWindow()
        new_window.show()
            
class InterfaceWindow(QMainWindow):
    def __init__(self):
        super(InterfaceWindow, self).__init__()
        self.ui2 = Ui_interface_main()
        self.ui2.setupUi(self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec())
