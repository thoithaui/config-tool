# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 201, 81))
        self.groupBox.setObjectName("groupBox")
        self.memoryCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.memoryCheckBox.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.memoryCheckBox.setText("")
        self.memoryCheckBox.setObjectName("memoryCheckBox")
        self.memorySpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.memorySpinBox.setGeometry(QtCore.QRect(70, 30, 81, 22))
        self.memorySpinBox.setDecimals(1)
        self.memorySpinBox.setMaximum(100.0)
        self.memorySpinBox.setSingleStep(0.1)
        self.memorySpinBox.setProperty("value", 100.0)
        self.memorySpinBox.setObjectName("memorySpinBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 21, 21))
        self.label_2.setObjectName("label_2")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(430, 490, 93, 28))
        self.startBtn.setObjectName("startBtn")
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setGeometry(QtCore.QRect(660, 490, 93, 28))
        self.closeBtn.setObjectName("closeBtn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 20, 201, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cpuCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.cpuCheckBox.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.cpuCheckBox.setText("")
        self.cpuCheckBox.setObjectName("cpuCheckBox")
        self.cpuSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.cpuSpinBox.setGeometry(QtCore.QRect(80, 30, 81, 22))
        self.cpuSpinBox.setDecimals(1)
        self.cpuSpinBox.setMaximum(100.0)
        self.cpuSpinBox.setSingleStep(0.1)
        self.cpuSpinBox.setProperty("value", 100.0)
        self.cpuSpinBox.setObjectName("cpuSpinBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 21, 21))
        self.label_3.setObjectName("label_3")
        self.endBtn = QtWidgets.QPushButton(self.centralwidget)
        self.endBtn.setGeometry(QtCore.QRect(550, 490, 93, 28))
        self.endBtn.setObjectName("endBtn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 440, 201, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.timeSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.timeSpinBox.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.timeSpinBox.setDecimals(0)
        self.timeSpinBox.setMinimum(1.0)
        self.timeSpinBox.setMaximum(3600.0)
        self.timeSpinBox.setSingleStep(1.0)
        self.timeSpinBox.setProperty("value", 10.0)
        self.timeSpinBox.setObjectName("timeSpinBox")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(120, 29, 55, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Memory"))
        self.label_2.setText(_translate("MainWindow", "%"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.groupBox_2.setTitle(_translate("MainWindow", "CPU"))
        self.label_3.setText(_translate("MainWindow", "%"))
        self.endBtn.setText(_translate("MainWindow", "End"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Time"))
        self.label.setText(_translate("MainWindow", "seconds"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
