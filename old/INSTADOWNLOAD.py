import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
import requests
import urllib.request
from selenium import webdriver


class INSTADOWNLOAD(QDialog):
    def __init__(self):
        super(INSTADOWNLOAD,self).__init__()
        loadUi('instadownload.ui',self)
        self.setWindowTitle('INSTADOWNLOAD')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        driver = webdriver.Firefox()
        driver.get(self.lineEdit.text())
        get_div = driver.find_element_by_class_name('FFVAD')
        photolink = get_div.get_attribute('src')
        print(photolink)
        urllib.request.urlretrieve(photolink, 'INSTAPHOTO.jpg')
        self.label_3.setTest('Your download link is:', photolink)
        


app=QApplication(sys.argv)
widget=INSTADOWNLOAD()
widget.show()
sys.exit(app.exec_())
