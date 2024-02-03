# Form implementation generated from reading ui file 'GUI/interface.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_interface_main(object):
    def setupUi(self, interface_main):
        interface_main.setObjectName("interface_main")
        interface_main.resize(436, 601)
        self.centralwidget = QtWidgets.QWidget(parent=interface_main)
        self.centralwidget.setObjectName("centralwidget")
        self.selection = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.selection.setGeometry(QtCore.QRect(10, 10, 411, 541))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        self.selection.setFont(font)
        self.selection.setObjectName("selection")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.cv_view = QtWidgets.QGraphicsView(parent=self.tab)
        self.cv_view.setGeometry(QtCore.QRect(30, 160, 351, 351))
        self.cv_view.setObjectName("cv_view")
        self.accuracy_box = QtWidgets.QGroupBox(parent=self.tab)
        self.accuracy_box.setGeometry(QtCore.QRect(40, 100, 331, 51))
        self.accuracy_box.setObjectName("accuracy_box")
        self.accuracy_bar = QtWidgets.QProgressBar(parent=self.accuracy_box)
        self.accuracy_bar.setGeometry(QtCore.QRect(10, 20, 301, 23))
        self.accuracy_bar.setProperty("value", 24)
        self.accuracy_bar.setObjectName("accuracy_bar")
        self.workout_box = QtWidgets.QGroupBox(parent=self.tab)
        self.workout_box.setGeometry(QtCore.QRect(30, 10, 351, 81))
        self.workout_box.setObjectName("workout_box")
        self.exercise_name = QtWidgets.QLabel(parent=self.workout_box)
        self.exercise_name.setGeometry(QtCore.QRect(10, 20, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(True)
        self.exercise_name.setFont(font)
        self.exercise_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.exercise_name.setObjectName("exercise_name")
        self.workout_box.raise_()
        self.cv_view.raise_()
        self.accuracy_box.raise_()
        self.selection.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.selection.addTab(self.tab_2, "")
        interface_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=interface_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 22))
        self.menubar.setObjectName("menubar")
        interface_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=interface_main)
        self.statusbar.setObjectName("statusbar")
        interface_main.setStatusBar(self.statusbar)

        self.retranslateUi(interface_main)
        self.selection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(interface_main)

    def retranslateUi(self, interface_main):
        _translate = QtCore.QCoreApplication.translate
        interface_main.setWindowTitle(_translate("interface_main", "MainWindow"))
        self.accuracy_box.setTitle(_translate("interface_main", "Accuracy"))
        self.workout_box.setTitle(_translate("interface_main", "Workout"))
        self.exercise_name.setText(_translate("interface_main", "TextLabel"))
        self.selection.setTabText(self.selection.indexOf(self.tab), _translate("interface_main", "Exercise"))
        self.selection.setTabText(self.selection.indexOf(self.tab_2), _translate("interface_main", "Example"))
