#Mateusz Parasiewicz WME19BC1S1
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog
import wfdb
import EKG


class Ui_Preprocessing_ECG(object):

    def getFiles(self):
        global fname
        fname = QFileDialog.getOpenFileName()
        print(fname)

    def readEcg(self):
        record = wfdb.rdrecord(fname, channels=[0], sampfrom=0)
        wfdb.plot_wfdb(record=record, title='Sygnał wejściowy')


    def setupUi(self, Preprocessing_ECG):
        Preprocessing_ECG.setObjectName("Preprocessing_ECG")
        Preprocessing_ECG.resize(519, 272)
        self.pushButton = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 240, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 150, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.graphicsView = QtWidgets.QGraphicsView(Preprocessing_ECG)
        self.graphicsView.setGeometry(QtCore.QRect(150, 30, 351, 201))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_4 = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 180, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 30, 111, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 240, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton_7.setGeometry(QtCore.QRect(420, 240, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 120, 111, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 90, 111, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Preprocessing_ECG)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 240, 111, 23))
        self.pushButton_10.setObjectName("pushButton_10")

        self.retranslateUi(Preprocessing_ECG)
        QtCore.QMetaObject.connectSlotsByName(Preprocessing_ECG)

    def retranslateUi(self, Preprocessing_ECG):
        _translate = QtCore.QCoreApplication.translate
        Preprocessing_ECG.setWindowTitle(_translate("Preprocessing_ECG", "Preprocessing ECG"))
        self.pushButton.setText(_translate("Preprocessing_ECG", "Read ECG"))
        self.pushButton.clicked.connect(self.getFiles)
        self.pushButton_2.setText(_translate("Preprocessing_ECG", "Clear"))
        self.pushButton_3.setText(_translate("Preprocessing_ECG", "Waverec"))
        self.pushButton_4.setText(_translate("Preprocessing_ECG", "Peaks detect."))
        self.pushButton_5.setText(_translate("Preprocessing_ECG", "Select file"))
        self.pushButton_6.setText(_translate("Preprocessing_ECG", "Back"))
        self.pushButton_7.setText(_translate("Preprocessing_ECG", "Close"))
        self.pushButton_7.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_8.setText(_translate("Preprocessing_ECG", "Wavelet dec."))
        self.pushButton_9.setText(_translate("Preprocessing_ECG", "Bandpass filter"))
        self.pushButton_10.setText(_translate("Preprocessing_ECG", "Display"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Preprocessing_ECG = QtWidgets.QDialog()
    ui = Ui_Preprocessing_ECG()
    ui.setupUi(Preprocessing_ECG)
    Preprocessing_ECG.show()
    sys.exit(app.exec())
