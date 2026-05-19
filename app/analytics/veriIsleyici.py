import pandas as pd

# c++ motorundan gelen ham verileri isleyip pandas veri cercevesine (dataframe) cevirir
class veriIsleyici:
    def __init__(self, hamVeriler):
        self.hamVeriler = hamVeriler

    # c++ listesini python sozluklerine cevirerek pandas tablosu olusturur
    def dataframeOlustur(self):
        veriListesi = []
        for veri in self.hamVeriler:
            veriListesi.append({
                "zamanDamgasi": veri.zamanDamgasi,
                "x": veri.x,
                "y": veri.y,
                "hataDurumu": veri.hataDurumu
            })
        return pd.DataFrame(veriListesi)

    # hata durumlarina gore oransal basari puanini hesaplar
    def istatistikleriHesapla(self, df):
        if df.empty:
            return 0.0

        toplamVeri = len(df)
        hataliIslem = df['hataDurumu'].sum()
        dogruIslem = toplamVeri - hataliIslem

        basariOrani = (dogruIslem / toplamVeri) * 100
        return basariOrani