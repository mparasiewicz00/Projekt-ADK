# Mateusz Parasiewicz WME19BC1S1
import scipy.signal
import pandas as pd
import numpy as np

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtCore import QCoreApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 410, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(710, 490, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(840, 490, 121, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(30, 70, 121, 41))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 120, 121, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 170, 121, 41))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 220, 121, 41))
        self.radioButton_4.setObjectName("radioButton_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(160, 30, 800, 420))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
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
        ax1.minorticks_on()
        ax1.plot(x, y, "-k", label="EKG")
        ax1.legend()
        ax1.grid(which='major', linestyle='-', color='red', linewidth='0.8')
        ax1.grid(which='minor', linestyle=':', color='black', linewidth='0.5')
        canvas = FigureCanvas(figure)
        canvas.resize(1500, 400)
        self.scene.addWidget(canvas)

    def loadFile(self, name):
        data = pd.read_csv(f'{name}')
        imp = data["ECG"]
        imp = np.gradient(imp)
        b, a = scipy.signal.butter(3, 0.1)
        ekg = scipy.signal.filtfilt(b, a, imp)
        data["ECG"] = ekg
        self.data = data
        figure = Figure()
        ax2 = figure.gca()
        x = list(np.arange(1, len(ekg) + 1))
        y = np.array(ekg)
        ax2.minorticks_on()
        ax2.plot(x, -y, "-k", label="3-pole lowpass filter at 0.1 Nyquist frequency")
        ax2.legend()
        ax2.grid(which='major', linestyle='-', color='red', linewidth='0.8')
        ax2.grid(which='minor', linestyle=':', color='black', linewidth='0.5')
        canvas = FigureCanvas(figure)
        canvas.resize(1500, 450)
        self.scene.addWidget(canvas)
    def loadFile_2(self, name):
        data = pd.read_csv(f'{name}')
        imp = data["ECG"]
        imp = np.gradient(imp)
        b, a = scipy.signal.butter(3, [.01, .05], 'band')
        ekg = scipy.signal.filtfilt(b, a, imp)
        data["ECG"] = ekg
        self.data = data
        figure = Figure()
        ax2 = figure.gca()
        x = list(np.arange(1, len(ekg) + 1))
        y = np.array(ekg)
        ax2.minorticks_on()
        ax2.plot(x, -y, "-k", label="Bandpass filter")
        ax2.legend()
        ax2.grid(which='major', linestyle='-', color='red', linewidth='0.8')
        ax2.grid(which='minor', linestyle=':', color='black', linewidth='0.5')
        canvas = FigureCanvas(figure)
        canvas.resize(1500, 450)
        self.scene.addWidget(canvas)


    def loadFile_3(self, name, passType):
        data = pd.read_csv(f'{name}')
        imp = data["ECG"]
        imp = np.gradient(imp)
        b, a = scipy.signal.butter(3, 0.05, passType)
        ekg = scipy.signal.filtfilt(b, a, imp)
        data["ECG"] = ekg
        self.data = data
        figure = Figure()
        ax2 = figure.gca()
        x = list(np.arange(1, len(ekg) + 1))
        y = np.array(ekg)
        ax2.minorticks_on()
        if passType == 'lowpass':
            ax2.plot(x, -y, "-k", label="Lowpass filter")
        else:
            ax2.plot(x, -y, "-k", label="Highpass filter")
        ax2.legend()
        ax2.grid(which='major', linestyle='-', color='red', linewidth='0.8')
        ax2.grid(which='minor', linestyle=':', color='black', linewidth='0.5')
        canvas = FigureCanvas(figure)
        canvas.resize(1500, 450)
        self.scene.addWidget(canvas)

    def plotECG(self):
        if self.radioButton_1.isChecked():
             self.loadFile(self.path)
        elif self.radioButton_2.isChecked():
             self.loadFile_2(self.path)
        elif self.radioButton_3.isChecked():
             self.loadFile_3(self.path, 'lowpass')
        elif self.radioButton_4.isChecked():
             self.loadFile_3(self.path, 'highpass')

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
        self.radioButton_1.setText(_translate("MainWindow", "3-pole/Nyq"))
        self.radioButton_2.setText(_translate("MainWindow", "Bandpass"))
        self.radioButton_3.setText(_translate("MainWindow", "Lowpass"))
        self.radioButton_4.setText(_translate("MainWindow", "Highpass"))
        self.pushButton_5.setText(_translate("MainWindow", "Wizualizacja"))
        self.pushButton_5.clicked.connect(self.plotECG)
        self.pushButton_6.setText(_translate("MainWindow", "Zapisz wynik"))
        self.pushButton_6.clicked.connect(self.csvSave)
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
