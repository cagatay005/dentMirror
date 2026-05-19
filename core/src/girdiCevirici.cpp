#include "../include/girdiCevirici.hpp"

// sinifin kurucu fonksiyonu deger atamalari
girdiCevirici::girdiCevirici(int genislik, int yukseklik) {
    ekranGenisligi = genislik;
    ekranYuksekligi = yukseklik;
}

// secilen ayna moduna gore koordinatlari matematiksel olarak donusturur
koordinat girdiCevirici::koordinatlariCevir(int hamX, int hamY, testModu mod) {
    koordinat yeniKoordinat;

    if (mod == yatayTers) {
        yeniKoordinat.x = ekranGenisligi - hamX;
        yeniKoordinat.y = hamY;
    } 
    else if (mod == dikeyTers) {
        yeniKoordinat.x = hamX;
        yeniKoordinat.y = ekranYuksekligi - hamY;
    } 
    else if (mod == tamAyna) {
        yeniKoordinat.x = ekranGenisligi - hamX;
        yeniKoordinat.y = ekranYuksekligi - hamY;
    } 
    else {
        yeniKoordinat.x = hamX;
        yeniKoordinat.y = hamY;
    }

    return yeniKoordinat;
}