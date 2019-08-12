# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_preview(object):
    def setupUi(self, Dialog, photolink = ''):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-image: url(:/images/images/background.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.webView = QtWebKitWidgets.QWebEngineView(Dialog)
        self.webView.setStyleSheet("background-image: url(:/images/images/transparent.jpg);")
        #self.webView.setProperty("url", QtCore.QUrl("https://instagram.fccu1-1.fna.fbcdn.net/vp/4ab5042a84c5aa0fabb7db4f811cb0a0/5DCED915/t51.2885-15/e35/67108978_161040128371727_8059326166010212020_n.jpg?_nc_ht=instagram.fccu1-1.fna.fbcdn.net"))
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet("background-image: url(:/images/images/transparent.jpg);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.webView.setProperty("url", QtCore.QUrl(photolink))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Image Preview"))

from PyQt5 import QtWebEngineWidgets as QtWebKitWidgets
import instadownload_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_preview()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
