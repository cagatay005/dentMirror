import sys
import os
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QLineEdit, QCheckBox, QSpinBox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../build')))
import dentMirrorCore

from ui.testEkrani import testEkrani

class anaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DentMirror - İndirekt Görüş Simülatörü")
        self.setFixedSize(400, 420) # Yeni elemanlar icin yuksekligi biraz artirdik

        anaArac = QWidget()
        duzen = QVBoxLayout()

        # Ogrenci ismi bolumu
        isimEtiketi = QLabel("Öğrenci Adı Soyadı:")
        duzen.addWidget(isimEtiketi)
        self.isimGiris = QLineEdit()
        self.isimGiris.setPlaceholderText("Örn: Çağatay")
        duzen.addWidget(self.isimGiris)

        # Ayna modu bolumu
        bilgiEtiketi = QLabel("Lütfen çalışmak istediğiniz ayna modunu seçin:")
        duzen.addWidget(bilgiEtiketi)
        self.modSecici = QComboBox()
        self.modSecici.addItems(["Yatay Ters", "Dikey Ters", "Tam Ayna"])
        duzen.addWidget(self.modSecici)

        # --- YENİ: Sure Siniri Ayarlari ---
        self.sureKontrol = QCheckBox("Süre Sınırı Uygulansın")
        self.sureKontrol.stateChanged.connect(self.sureKutusunuKapaAc)
        duzen.addWidget(self.sureKontrol)

        sureDuzen = QHBoxLayout()
        self.sureEtiketi = QLabel("Süre (Saniye):")
        self.sureEtiketi.setEnabled(False) # Ilk basta pasif
        
        self.sureSecici = QSpinBox()
        self.sureSecici.setRange(5, 300) # En az 5, en cok 300 saniye (5 dakika)
        self.sureSecici.setValue(30) # Varsayilan 30 saniye
        self.sureSecici.setEnabled(False) # Ilk basta pasif
        
        sureDuzen.addWidget(self.sureEtiketi)
        sureDuzen.addWidget(self.sureSecici)
        duzen.addLayout(sureDuzen)
        # ----------------------------------

        # Testi baslat butonu
        baslatButonu = QPushButton("Testi Başlat")
        baslatButonu.clicked.connect(self.testiBaslat)
        duzen.addWidget(baslatButonu)

        anaArac.setLayout(duzen)
        self.setCentralWidget(anaArac)

    # Onay kutusunun durumuna gore sure giris alanini aktif/pasif yapar
    def sureKutusunuKapaAc(self, durum):
        aktifMi = (durum == 2) # PyQt6'da 2 degeri 'Checked' anlamina gelir
        self.sureEtiketi.setEnabled(aktifMi)
        self.sureSecici.setEnabled(aktifMi)

    # Verilen tum parametreleri test ekranina iletir
    def testiBaslat(self):
        ogrenciAdi = self.isimGiris.text().strip()
        if not ogrenciAdi:
            ogrenciAdi = "Anonim Ogrenci"

        secilenMod = self.modSecici.currentIndex()
        sureAktif = self.sureKontrol.isChecked()
        toplamSure = self.sureSecici.value()

        print(f"Test Başlatılıyor -> İsim: {ogrenciAdi}, Mod: {secilenMod}, Süre Sınırı: {sureAktif} ({toplamSure} sn)")
        
        # Parametreleri test ekranina pasliyoruz
        self.simulasyonPenceresi = testEkrani(secilenMod, ogrenciAdi, sureAktif, toplamSure)
        self.simulasyonPenceresi.exec()