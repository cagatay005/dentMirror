from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from analytics.grafikCizici import grafikCizici

# test sonrasi basari skorunu ve gorsel analiz secenegini sunan pencere
class raporPenceresi(QDialog):
    def __init__(self, basariOrani, veriCercevesi):
        super().__init__()
        self.veriCercevesi = veriCercevesi
        
        self.setWindowTitle("DentMirror - Sınav Raporu")
        self.setFixedSize(350, 200)

        duzen = QVBoxLayout()

        skorEtiketi = QLabel(f"Simülasyon Bitti!\nMotor Beceri Başarı Oranınız: %{basariOrani:.2f}")
        duzen.addWidget(skorEtiketi)

        grafikButonu = QPushButton("Koordinat ve Hata Grafiğini Göster")
        grafikButonu.clicked.connect(self.grafigiAc)
        duzen.addWidget(grafikButonu)

        self.setLayout(duzen)

    # matplotlib uzerinden interaktif analiz grafigini acar
    def grafigiAc(self):
        cizici = grafikCizici(self.veriCercevesi)
        cizici.hataGrafigiCiz()