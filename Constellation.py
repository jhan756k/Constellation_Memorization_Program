# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Constellation.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 485)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 121, 217))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Northcheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Northcheck.setFont(font)
        self.Northcheck.setObjectName("Northcheck")
        self.gridLayout.addWidget(self.Northcheck, 4, 0, 1, 1)
        self.Autumncheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Autumncheck.setFont(font)
        self.Autumncheck.setObjectName("Autumncheck")
        self.gridLayout.addWidget(self.Autumncheck, 2, 0, 1, 1)
        self.Springcheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Springcheck.setFont(font)
        self.Springcheck.setObjectName("Springcheck")
        self.gridLayout.addWidget(self.Springcheck, 0, 0, 1, 1)
        self.Southcheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Southcheck.setFont(font)
        self.Southcheck.setObjectName("Southcheck")
        self.gridLayout.addWidget(self.Southcheck, 5, 0, 1, 1)
        self.Wintercheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Wintercheck.setFont(font)
        self.Wintercheck.setObjectName("Wintercheck")
        self.gridLayout.addWidget(self.Wintercheck, 3, 0, 1, 1)
        self.Summercheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Summercheck.setFont(font)
        self.Summercheck.setObjectName("Summercheck")
        self.gridLayout.addWidget(self.Summercheck, 1, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 240, 111, 41))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.QuestionLabel = QtWidgets.QLabel(self.centralwidget)
        self.QuestionLabel.setGeometry(QtCore.QRect(180, 10, 621, 91))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.QuestionLabel.setFont(font)
        self.QuestionLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QuestionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.QuestionLabel.setWordWrap(True)
        self.QuestionLabel.setIndent(4)
        self.QuestionLabel.setObjectName("QuestionLabel")
        self.Ansinput = QtWidgets.QLineEdit(self.centralwidget)
        self.Ansinput.setGeometry(QtCore.QRect(180, 170, 351, 61))
        self.Ansinput.setObjectName("Ansinput")
        self.CheckansLabel = QtWidgets.QLabel(self.centralwidget)
        self.CheckansLabel.setGeometry(QtCore.QRect(180, 260, 411, 111))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.CheckansLabel.setFont(font)
        self.CheckansLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CheckansLabel.setWordWrap(True)
        self.CheckansLabel.setObjectName("CheckansLabel")
        self.enteransbutton = QtWidgets.QPushButton(self.centralwidget)
        self.enteransbutton.setGeometry(QtCore.QRect(580, 170, 121, 61))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.enteransbutton.setFont(font)
        self.enteransbutton.setObjectName("enteransbutton")
        self.nextbutton = QtWidgets.QPushButton(self.centralwidget)
        self.nextbutton.setGeometry(QtCore.QRect(650, 280, 121, 61))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.nextbutton.setFont(font)
        self.nextbutton.setObjectName("nextbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 44))
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
        self.Northcheck.setText(_translate("MainWindow", "North"))
        self.Autumncheck.setText(_translate("MainWindow", "Autumn"))
        self.Springcheck.setText(_translate("MainWindow", "Spring"))
        self.Southcheck.setText(_translate("MainWindow", "South"))
        self.Wintercheck.setText(_translate("MainWindow", "Winter"))
        self.Summercheck.setText(_translate("MainWindow", "Summer"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.QuestionLabel.setText(_translate("MainWindow", "TextLabel"))
        self.CheckansLabel.setText(_translate("MainWindow", "TextLabel"))
        self.enteransbutton.setText(_translate("MainWindow", "제출"))
        self.nextbutton.setText(_translate("MainWindow", "다음"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
