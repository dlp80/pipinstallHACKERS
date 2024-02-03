import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QSlider, QScrollArea, QPushButton, QLCDNumber, QTableWidgetItem, QMessageBox, QGraphicsView,
                               QGraphicsRectItem, QGraphicsScene, QHBoxLayout, QWidget, QLabel, QGraphicsItem, QVBoxLayout)
# from PySide6.QtCore import QFile, Slot,QDate, QTime, QTimer, QDateTime, Qt, QEvent, QRectF
from PySide6.QtGui import QPalette, QColor, QIntValidator, QBrush, QPen, QPixmap, QIcon
from PySide6.QtUiTools import QUiLoader
# import GUI.open_gui as ui
# import GUI.interface_gui as ui2
from GUI.open_gui import Ui_open_main
from GUI.interface_gui import Ui_Form

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from GUI.open_gui import Ui_open_main

class MyMainWindow(QMainWindow, Ui_Form):
    accuracy = 0
    workout = ""
    
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        
        self.ui.accuracy_bar.setValue(0)
        self.update()
        
    def update(self):
        self.enter_test()
        self.ui.accuracy_bar.setValue(int(self.accuracy))
        
    def set_workout(self, workout):
        self.workout = workout
        
    def get_workout(self):
        return self.workout
            
    def set_accuracy(self, a):
        self.accuracy = a
        print(a)
        
    def get_accuracy(self):
        return self.accuracy

    def enter_test(self):
        test = input("enter value for accuracy: ") 
        self.set_accuracy(test)
        print(self.accuracy)
     

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec())