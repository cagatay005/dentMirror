from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QPainter, QPen, QColor, QFont
from PyQt6.QtCore import Qt, QTimer # Geri sayim icin QTimer dahil ettik
import dentMirrorCore
from analytics.veriIsleyici import veriIsleyici
from analytics.veriKaydedici import veriKaydedici
from ui.raporPenceresi import raporPenceresi

class testEkrani(QDialog):
    def __init__(self, secilenModIndeksi, ogrenciAdi, sureAktif, toplamSure):
        super().__init__()
        self.secilenModIndeksi = secilenModIndeksi
        self.ogrenciAdi = ogrenciAdi
        self.sureAktif = sureAktif
        self.kalanSure = toplamSure
        
        self.setWindowTitle("DentMirror - Aktif Simülasyon Alanı")
        self.setFixedSize(800, 600)
        self.setMouseTracking(True)

        self.motor = dentMirrorCore.simulatorMotoru(800, 600)
        
        if secilenModIndeksi == 0:
            self.motor.testiBaslat(dentMirrorCore.testModu.yatayTers)
            self.modStr = "Yatay Ters"
        elif secilenModIndeksi == 1:
            self.motor.testiBaslat(dentMirrorCore.testModu.dikeyTers)
            self.modStr = "Dikey Ters"
        else:
            self.motor.testiBaslat(dentMirrorCore.testModu.tamAyna)
            self.modStr = "Tam Ayna"

        self.cizimNoktalari = []

        duzen = QVBoxLayout()
        
        # --- YENİ: Ekranda Gorunecek Zamanlayici Etiketi ---
        self.zamanlayiciEtiketi = QLabel("")
        self.zamanlayiciEtiketi.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.zamanlayiciEtiketi.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        duzen.addWidget(self.zamanlayiciEtiketi)
        
        # Eger sure siniri aktifse QTimer mekanizmasini kurup baslatiyoruz
        if self.sureAktif:
            self.zamanlayiciEtiketi.setText(f"Kalan Süre: {self.kalanSure} sn ")
            self.zamanlayiciEtiketi.setStyleSheet("color: darkred;")
            self.zamanlayici = QTimer()
            self.zamanlayici.timeout.connect(self.saniyeyiGuncelle)
            self.zamanlayici.start(1000) # Her 1000 milisaniyede (1 saniye) bir tetiklenir
        else:
            self.zamanlayiciEtiketi.setText("Serbest Çalışma Modu ")
            self.zamanlayiciEtiketi.setStyleSheet("color: darkgreen;")
        # --------------------------------------------------

        duzen.addStretch()
        
        bitirButonu = QPushButton("Testi Bitir ve Raporu Gör")
        bitirButonu.setFixedSize(200, 40)
        bitirButonu.clicked.connect(self.testiBitir)
        duzen.addWidget(bitirButonu, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(duzen)

    # --- YENİ: Her saniye tetiklenen geri sayim fonksiyonu ---
    def saniyeyiGuncelle(self):
        self.kalanSure -= 1
        self.zamanlayiciEtiketi.setText(f"Kalan Süre: {self.kalanSure} sn ")
        
        # Sure bittiyse zamanlayiciyi durdur ve testi otomatik olarak sonlandir
        if self.kalanSure <= 0:
            self.zamanlayici.stop()
            print("Süre doldu! Test otomatik bitiriliyor...")
            self.testiBitir()
    # ---------------------------------------------------------

    def mouseMoveEvent(self, event):
        hamX = event.pos().x()
        hamY = event.pos().y()

        islenmisKoor = self.motor.anlikHareket(hamX, hamY)
        self.cizimNoktalari.append((islenmisKoor.x, islenmisKoor.y))
        self.update()

    def paintEvent(self, event):
        ressam = QPainter(self)
        ressam.setRenderHint(QPainter.RenderHint.Antialiasing)

        ressam.setPen(QPen(QColor(200, 200, 200), 1, Qt.PenStyle.DashLine))
        ressam.setBrush(QColor(230, 255, 230, 100))
        ressam.drawRect(150, 0, 100, 600) 

        kalem = QPen(QColor(255, 0, 0), 4)
        kalem.setCapStyle(Qt.PenCapStyle.RoundCap)
        kalem.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        ressam.setPen(kalem)

        for i in range(1, len(self.cizimNoktalari)):
            onceki = self.cizimNoktalari[i-1]
            anlik = self.cizimNoktalari[i]
            ressam.drawLine(onceki[0], onceki[1], anlik[0], anlik[1])

    def testiBitir(self):
        # Eger zamanlayici hala calisiyorsa guvenli bir sekilde durduruyoruz
        if self.sureAktif and hasattr(self, 'zamanlayici') and self.zamanlayici.isActive():
            self.zamanlayici.stop()

        hamVeriler = self.motor.sonuclariGetir()

        if not hamVeriler:
            self.close()
            return

        isleyici = veriIsleyici(hamVeriler)
        df = isleyici.dataframeOlustur()
        basariOrani = isleyici.istatistikleriHesapla(df)

        kaydedici = veriKaydedici()
        kaydedici.raporKaydet(self.ogrenciAdi, self.modStr, basariOrani)

        self.rapor = raporPenceresi(basariOrani, df)
        self.close()
        self.rapor.exec()