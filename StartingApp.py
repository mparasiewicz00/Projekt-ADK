from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QMenu
from PySide6.QtGui import QCloseEvent, QIcon, QAction

class Apka(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
    def setup(self):
        krew = QPushButton('krew', self)
        ekg = QPushButton('ekg', self)
        icg = QPushButton('ICG', self)
        przycisk_zamknij = QPushButton('Zamknij Aplikacje', self)
        przycisk_zamknij.clicked.connect(QApplication.instance().quit)
        przycisk_zamknij.resize(przycisk_zamknij.sizeHint())
        przycisk_zamknij.move(158, 120)
        krew.setGeometry(0, 0, 250, 40)
        ekg.setGeometry(0, 0, 250, 40)
        icg.setGeometry(0, 0, 250, 40)
        krew.move(80, 0)
        ekg.move(80, 40)
        icg.move(80, 80)

        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Aplikacja(Grupa 3)')
        self.setWindowIcon(QIcon('icon/ekg_icon.png'))

        self.show()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'wiadomosc', 'Czy jesteś pewny ze chcesz zamknąć?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def run():
    app = QApplication([])
    appka = Apka()

    app.exec()

if __name__ == '__main__':
    run()