# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_phone.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.input_phone.setObjectName("input_phone")
        self.gridLayout_2.addWidget(self.input_phone, 4, 1, 1, 1)
        self.input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_name.setObjectName("input_name")
        self.gridLayout_2.addWidget(self.input_name, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_2.addWidget(self.btn_add, 0, 2, 5, 1)
        self.phone_book = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.phone_book.setFont(font)
        self.phone_book.setObjectName("phone_book")
        self.gridLayout_2.addWidget(self.phone_book, 5, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Телефон"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.btn_add.setText(_translate("MainWindow", "Добавить"))
