import sys

from PyQt5.QtWidgets import QWidget,QTextEdit,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

class Pencere(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.kaydet = QPushButton("Kaydet")
        self.temizle = QPushButton("Temizle")

        h_box = QHBoxLayout()

        h_box.addStretch()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.click)
        self.kaydet.clicked.connect(self.click)

        self.setWindowTitle("Yazıyı Kaydet")
        self.show()

    def click(self):
        sender = self.sender()
        sayı = 1
        if (sender.text() == "Temizle"):
            self.yazi_alani.clear()
        else:
            with open(r"C:\Users\Yener\Desktop\yazı.txt","w") as dosya:
                dosya.write(self.yazi_alani.toPlainText())



app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec())