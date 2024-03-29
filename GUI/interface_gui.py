# Form implementation generated from reading ui file 'GUI/interface.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(436, 601)
        self.selection = QtWidgets.QTabWidget(parent=Form)
        self.selection.setGeometry(QtCore.QRect(10, 20, 411, 541))
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

        self.retranslateUi(Form)
        self.selection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.accuracy_box.setTitle(_translate("Form", "Accuracy"))
        self.workout_box.setTitle(_translate("Form", "Workout"))
        self.exercise_name.setText(_translate("Form", "TextLabel"))
        self.selection.setTabText(self.selection.indexOf(self.tab), _translate("Form", "Exercise"))
        self.selection.setTabText(self.selection.indexOf(self.tab_2), _translate("Form", "Example"))
