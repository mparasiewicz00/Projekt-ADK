#Mateusz Parasiewicz WME19BC1S1
import csv
import os
import matplotlib.pyplot as mtpl
import scipy.signal
import pandas as pd
import numpy as np
from PyQt5.QtCore import QDir
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.uic.properties import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtCore import QCoreApplication
from scipy.signal import firwin
from scipy.signal import freqz
from scipy.signal import filtfilt
import ICG


# class mymainwindow(QtGui.QMainWindow): # <- from program 2
#     def __init__(self):
#         QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
#         .
#         .
#         myQDialog = QtGui.QDialog() # <- from program 1
#         ui = Ui_Dialog()            # <- from program 1
#         ui.setupUi(myQDialog)       # <- from program 1
#         .
#         .
#         self.setCentralWidget(myQDialog) # <- from program 1 into 2
#         .
#         .


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 121, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 310, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(710, 490, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 10, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 10, 121, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(290, 10, 121, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(840, 490, 121, 41))
        self.pushButton_10.setObjectName("pushButton_10")

        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(30, 160, 121, 41))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 210, 121, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 110, 121, 41))
        self.radioButton_3.setObjectName("radioButton_3")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(160, 60, 800, 420))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)


        self.valueNQ = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.valueNQ.setGeometry(QtCore.QRect(30, 260, 121, 21))
        self.valueNQ.setObjectName("valueNQ")
        self.valueNQ.decimals()
        self.valueNQ.setMaximum(0.99)
        self.valueNQ.setMinimum(0.01)
        self.valueNQ.setSingleStep(0.01)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def insertData(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        self.path = path
        data = pd.read_csv(path)
        imp = data["ECG"]
        ekg = np.gradient(imp)
        figure = Figure()
        ax1 = figure.gca()
        x = list(np.arange(1, len(ekg) + 1))
        y = np.array(ekg)
        ax1.plot(x, y, "-k", label="EKG")
        ax1.legend()
        ax1.grid(True, color='black', linewidth='0.2')

        canvas = FigureCanvas(figure)
        canvas.resize(1500, 400)
        self.scene.addWidget(canvas)

    def loadFile(self, name, passType, nq):
        data = pd.read_csv(f'{name}')
        imp = data["ECG"]
        imp = np.gradient(imp)
        b, a = scipy.signal.butter(3, nq, passType)
        ekg = scipy.signal.filtfilt(b, a,  imp)
        data["ECG"] = ekg

        self.data = data
        figure = Figure()
        ax2 = figure.gca()
        x = list(np.arange(1, len(ekg) + 1))
        y = np.array(ekg)
        ax2.plot(x, -y, "-k", label="Filtered")
        ax2.legend()
        ax2.grid(True, color='black', linewidth='0.2')

        canvas = FigureCanvas(figure)
        canvas.resize(1500, 450)
        self.scene.addWidget(canvas)

    def plotECG(self):
        nq = self.valueNQ.text()
        nq = float(nq.replace(',', '.'))
        if self.radioButton_1.isChecked():
            self.loadFile(self.path, 'lowpass', nq)
        elif self.radioButton_2.isChecked():
            self.loadFile(self.path, 'highpass', nq)


    def csvSave(self):
        filename = 'afterPostProc' + self.path[-8:-4] + '.csv'
        headerList = ['ECG', 'IMP', 'Z0']
        self.data.to_csv(filename, header=headerList, index=False)

    def retranslateUi(self, MainWindow):
        self.data = []
        self.path = ''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EKG Preprocessing"))
        self.pushButton.setText(_translate("MainWindow", "Wprowadz dane"))
        self.pushButton.clicked.connect(self.insertData)
        self.radioButton_1.setText(_translate("MainWindow", "Lowpass"))
        self.radioButton_2.setText(_translate("MainWindow", "Highpass"))
        self.radioButton_3.setText(_translate("MainWindow", "Input signal"))
        self.pushButton_5.setText(_translate("MainWindow", "Wizualizacja"))
        self.pushButton_5.clicked.connect(self.plotECG)
        self.pushButton_6.setText(_translate("MainWindow", "Zapisz wynik"))
        self.pushButton_6.clicked.connect(self.csvSave)
        self.pushButton_7.setText(_translate("MainWindow", "Krew"))
        self.pushButton_8.setText(_translate("MainWindow", "EKG"))
        self.pushButton_9.setText(_translate("MainWindow", "ICG"))
        self.pushButton_10.setText(_translate("MainWindow", "Koniec"))
        self.pushButton_10.clicked.connect(QCoreApplication.instance().quit)
        self.graphicsView.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
