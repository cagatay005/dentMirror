#ifndef GIRDICEVIRICI_HPP
#define GIRDICEVIRICI_HPP

// kullanicinin sececegi ayna zorluk modlari
enum testModu {
    yatayTers,
    dikeyTers,
    tamAyna
};

// yeni hesaplanan ters koordinatlari tutan yapi
struct koordinat {
    int x;
    int y;
};

// fare girdilerini secilen moda gore tersine ceviren sinif
class girdiCevirici {
private:
    int ekranGenisligi;
    int ekranYuksekligi;

public:
    // sinifin kurucu fonksiyonu
    girdiCevirici(int genislik, int yukseklik);

    // gelen ham koordinatlari tersine cevirip donduren fonksiyon
    koordinat koordinatlariCevir(int hamX, int hamY, testModu mod);
};

#endif