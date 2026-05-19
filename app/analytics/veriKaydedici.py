import os
import csv
from datetime import datetime

# test sonuclarini csv dosyasina kalici olarak kaydeden sinif
class veriKaydedici:
    def __init__(self):
        self.dosyaYolu = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/gelisimRaporu.csv'))

    # yeni bir test sonucunu csv dosyasina ekler
    def raporKaydet(self, ogrenciAdi, testModuStr, basariOrani):
        dosyaMevcut = os.path.exists(self.dosyaYolu)
        zamanDamgasi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.dosyaYolu, mode='a', newline='', encoding='utf-8') as dosya:
            yazici = csv.writer(dosya)
            
            # dosya ilk kez olusuyorsa baslik satirlarini ekler
            if not dosyaMevcut:
                yazici.writerow(["Zaman", "Ogrenci Adi", "Test Modu", "Basari Orani"])
                
            yazici.writerow([zamanDamgasi, ogrenciAdi, testModuStr, f"{basariOrani:.2f}"])