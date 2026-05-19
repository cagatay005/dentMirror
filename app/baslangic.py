import sys
from PyQt6.QtWidgets import QApplication
from ui.anaPencere import anaPencere

# uygulamanin ana baslangic dongusunu yonetir
def baslat():
    uygulama = QApplication(sys.argv)
    anaEkran = anaPencere()
    anaEkran.show()
    sys.exit(uygulama.exec())

if __name__ == "__main__":
    baslat()