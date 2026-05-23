from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from analytics.grafikCizici import grafikCizici
from ui.replayEkrani import replayEkrani

class raporPenceresi(QDialog):
    def __init__(self, basariOrani, veriTablosu):
        super().__init__()
        self.setWindowTitle("DentMirror - Sınav Sonuç Raporu")
        self.setFixedSize(400, 250) 
        
        self.veriTablosu = veriTablosu

        duzen = QVBoxLayout()
        
        self.sonucEtiketi = QLabel(f"Simülasyon Bitti!\nMotor Beceri Başarı Oranınız: %{basariOrani:.2f}")
        self.sonucEtiketi.setStyleSheet("font-size: 14px; font-weight: bold;")
        duzen.addWidget(self.sonucEtiketi)

        grafikButonu = QPushButton("Koordinat ve Hata Grafiğini Göster")
        grafikButonu.clicked.connect(self.grafigiGoster)
        duzen.addWidget(grafikButonu)

        # Buton ayarlari
        replayButonu = QPushButton("Simülasyonu Tekrar İzle")
        replayButonu.setStyleSheet("background-color: #e3f2fd; color: black; font-weight: bold;")
        replayButonu.clicked.connect(self.tekrarIzle)
        duzen.addWidget(replayButonu)

        self.setLayout(duzen)

    def grafigiGoster(self):
        cizici = grafikCizici(self.veriTablosu)
        cizici.hataGrafigiCiz()

    def tekrarIzle(self):
        self.tekrarPenceresi = replayEkrani(self.veriTablosu)
        self.tekrarPenceresi.show()