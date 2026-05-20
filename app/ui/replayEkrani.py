from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider
from PyQt6.QtGui import QPainter, QPen, QColor, QFont
from PyQt6.QtCore import Qt, QTimer

class replayEkrani(QDialog):
    def __init__(self, veriTablosu):
        super().__init__()
        self.setWindowTitle("DentMirror - Simülasyon Tekrar Oynatımı")
        # Kontrol butonlarina yer acmak icin yuksekligi 600'den 660'a cikardik
        self.setFixedSize(800, 660) 
        
        self.veriTablosu = veriTablosu
        self.toplamKare = len(self.veriTablosu)
        self.guncelIndeks = 0
        self.cizimNoktalari = []
        self.anlikHata = False
        self.oynatiliyor = True # Medya oynatici durumu

        # Performans Icin: Pandas tablosunu hizli bir listeye ceviriyoruz (Kasma olmamasi icin)
        self.tumVeriler = []
        for i in range(self.toplamKare):
            satir = self.veriTablosu.iloc[i]
            x = int(satir.get('X', satir.get('x', 0)))
            y = int(satir.get('Y', satir.get('y', 0)))
            h = bool(satir.get('Hata', satir.get('hataVarMi', satir.get('hata', False))))
            self.tumVeriler.append((x, y, h))

        duzen = QVBoxLayout()
        
        # Baslik
        self.bilgiEtiketi = QLabel("Simülasyon Tekrar Oynatılıyor... (Replay)")
        self.bilgiEtiketi.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.bilgiEtiketi.setStyleSheet("color: darkblue;")
        duzen.addWidget(self.bilgiEtiketi)
        
        # Cizim alanini (tuvali) uste itmek icin bosluk
        duzen.addStretch()

        # --- YENİ: Medya Oynatıcı Kontrol Çubuğu ---
        kontrolDuzeni = QHBoxLayout()
        
        # Geri Sar Butonu
        self.geriButonu = QPushButton("⏪ -10 Kare")
        self.geriButonu.clicked.connect(self.geriSar)
        kontrolDuzeni.addWidget(self.geriButonu)

        # Oynat/Duraklat Butonu
        self.oynatDuraklatButonu = QPushButton("⏸ Duraklat")
        self.oynatDuraklatButonu.setStyleSheet("font-weight: bold;")
        self.oynatDuraklatButonu.clicked.connect(self.oynatDuraklat)
        kontrolDuzeni.addWidget(self.oynatDuraklatButonu)

        # Ileri Sar Butonu
        self.ileriButonu = QPushButton("⏩ +10 Kare")
        self.ileriButonu.clicked.connect(self.ileriSar)
        kontrolDuzeni.addWidget(self.ileriButonu)

        # Zaman Cizelgesi (Slider)
        self.zamanCizelgesi = QSlider(Qt.Orientation.Horizontal)
        self.zamanCizelgesi.setRange(0, self.toplamKare - 1)
        self.zamanCizelgesi.setValue(0)
        self.zamanCizelgesi.valueChanged.connect(self.cizelgeDegisti)
        kontrolDuzeni.addWidget(self.zamanCizelgesi)

        duzen.addLayout(kontrolDuzeni)
        # -------------------------------------------

        self.setLayout(duzen)

        # Oynatici motorunu (Zamanlayiciyi) baslatiyoruz
        self.zamanlayici = QTimer()
        self.zamanlayici.timeout.connect(self.sonrakiKareyiOynat)
        self.zamanlayici.start(30)

    # Buton Fonksiyonlari
    def oynatDuraklat(self):
        if self.oynatiliyor:
            self.zamanlayici.stop()
            self.oynatDuraklatButonu.setText("▶ Oynat")
            self.bilgiEtiketi.setText("Duraklatıldı.")
            self.bilgiEtiketi.setStyleSheet("color: orange;")
        else:
            if self.guncelIndeks >= self.toplamKare - 1:
                self.zamanCizelgesi.setValue(0) # En sondayken basilirsa basa sar
            self.zamanlayici.start(30)
            self.oynatDuraklatButonu.setText("⏸ Duraklat")
            self.bilgiEtiketi.setText("Simülasyon Tekrar Oynatılıyor...")
            self.bilgiEtiketi.setStyleSheet("color: darkblue;")
        
        self.oynatiliyor = not self.oynatiliyor

    def geriSar(self):
        hedef = max(0, self.guncelIndeks - 10)
        self.zamanCizelgesi.setValue(hedef)

    def ileriSar(self):
        hedef = min(self.toplamKare - 1, self.guncelIndeks + 10)
        self.zamanCizelgesi.setValue(hedef)

    # Slider hareket ettiginde veya zamanlayici tikladiginda calisir
    def cizelgeDegisti(self, deger):
        self.guncelIndeks = deger
        # Cizim listesini guncel indekse gore bastan olustur
        self.cizimNoktalari = [(d[0], d[1]) for d in self.tumVeriler[:self.guncelIndeks + 1]]
        self.anlikHata = self.tumVeriler[self.guncelIndeks][2]
        self.update() # Ekrani aninda ciz

    # Her 30 milisaniyede bir calisip slider'i bir tik saga kaydirir
    def sonrakiKareyiOynat(self):
        if self.guncelIndeks < self.toplamKare - 1:
            # setValue tetiklendiginde otomatik olarak cizelgeDegisti() fonksiyonunu cagirir
            self.zamanCizelgesi.setValue(self.guncelIndeks + 1)
        else:
            self.zamanlayici.stop()
            self.oynatiliyor = False
            self.oynatDuraklatButonu.setText("▶ Tekrar Oynat")
            self.bilgiEtiketi.setText("Tekrar Oynatım Tamamlandı.")
            self.bilgiEtiketi.setStyleSheet("color: darkgreen;")

    def paintEvent(self, event):
        ressam = QPainter(self)
        ressam.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Hata aninda kirmizi filtre
        if self.anlikHata:
            ressam.fillRect(self.rect(), QColor(255, 0, 0, 60))

        # Guvenli kanal rotasi (X: 150-250 arasi, Y: 0-600)
        ressam.setPen(QPen(QColor(200, 200, 200), 1, Qt.PenStyle.DashLine))
        ressam.setBrush(QColor(230, 255, 230, 100))
        ressam.drawRect(150, 0, 100, 600)

        # Gecmise yonelik tum noktalari birlestirip ciziyoruz
        kalem = QPen(QColor(0, 0, 255), 4) 
        kalem.setCapStyle(Qt.PenCapStyle.RoundCap)
        kalem.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        ressam.setPen(kalem)

        for i in range(1, len(self.cizimNoktalari)):
            onceki = self.cizimNoktalari[i-1]
            anlik = self.cizimNoktalari[i]
            ressam.drawLine(onceki[0], onceki[1], anlik[0], anlik[1])