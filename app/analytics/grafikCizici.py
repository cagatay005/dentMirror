import sys
import matplotlib

# Eğer işletim sistemi Windows ise bu motoru kullan, Linux ise kendi haline bırak
if sys.platform == 'win32':
    matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt

# test sonuclarini gorsel grafiklere donusturen sinif
class grafikCizici:
    def __init__(self, veriCercevesi):
        self.df = veriCercevesi

    # zaman icindeki y koordinati degisimini ve hata anlarini cizer
    def hataGrafigiCiz(self):
        if self.df.empty:
            print("Grafik çizilecek veri bulunamadı.")
            return

        plt.figure(figsize=(8, 5))
        
        hataliVeriler = self.df[self.df['hataDurumu'] == True]
        dogruVeriler = self.df[self.df['hataDurumu'] == False]

        plt.scatter(dogruVeriler['zamanDamgasi'], dogruVeriler['y'], color='blue', label='Doğru Hareket', alpha=0.5)
        plt.scatter(hataliVeriler['zamanDamgasi'], hataliVeriler['y'], color='red', label='Hatalı Temas', alpha=0.8)

        plt.title('Zaman İçindeki Koordinat ve Hata Dağılımı')
        plt.xlabel('Zaman (Milisaniye)')
        plt.ylabel('Y Ekseni Hareketi')
        plt.legend()
        
        plt.tight_layout()
        plt.show(block=True)