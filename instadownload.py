# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instadownload.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import urllib.request
from selenium import webdriver
from preview import Ui_Dialog_preview

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 265)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image: url(:/images/images/background.jpg);\n"
"background-position: center center;\n"
"background-repeat:   no-repeat;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 76, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(56, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(:/images/images/transparent.jpg);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("background-image: url(:/images/images/transparent.jpg);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 2, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setStyleSheet("background-image: url(:/images/images/transparent.jpg);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 2, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.toolButton.clicked.connect(self.parse)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INSTADOWNLOAD"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Welcome to INSTADOWNLOAD!</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter instagram post URL here...."))
        self.toolButton.setText(_translate("MainWindow", "..."))

    def parse(self):
        options = webdriver.firefox.options.Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get(self.lineEdit.text())
        get_div = driver.find_element_by_class_name('FFVAD')
        self.photolink = get_div.get_attribute('src')
        #print(photolink)
        #urllib.request.urlretrieve(photolink, 'INSTAPHOTO.jpg')
        self.preview()

    def preview(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_preview()
        ui.setupUi(Dialog, self.photolink)
        Dialog.show()
        rsp = Dialog.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            urllib.request.urlretrieve(self.photolink, 'INSTAPHOTO.jpg')

import instadownload_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
