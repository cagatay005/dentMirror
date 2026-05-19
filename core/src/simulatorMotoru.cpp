#include "../include/simulatorMotoru.hpp"

// motorun kurucu fonksiyonu
simulatorMotoru::simulatorMotoru(int genislik, int yukseklik) : cevirici(genislik, yukseklik) {}

// testi baslatir ve zamanlayiciyi sifirlar
void simulatorMotoru::testiBaslat(testModu mod) {
    aktifMod = mod;
    toplayici.verileriTemizle();
    toplayici.testiBaslat();
}

// fare her oynatildiginda bu fonksiyon tetiklenir
koordinat simulatorMotoru::anlikHareket(int x, int y) {
    // 1. ham koordinati al ve ayna moduna gore tersine cevir
    koordinat islenmisKoor = cevirici.koordinatlariCevir(x, y, aktifMod);

    // 2. basit bir hata senaryosu (ornek: cizgi X ekseninde 150 ile 250 arasinda olmali)
    // disari tasarsa hataDurumu 'true' olur
    bool hataVarMi = (islenmisKoor.x < 150 || islenmisKoor.x > 250); 
    
    // 3. veriyi c++ hafizasina milisaniye damgasiyla kaydet
    toplayici.veriEkle(islenmisKoor.x, islenmisKoor.y, hataVarMi);

    // 4. ekranda cizilmesi icin islenmis ters koordinati python'a dondur
    return islenmisKoor; 
}

// analiz edilmek uzere toplanan verileri dondurur
std::vector<hareketVerisi> simulatorMotoru::sonuclariGetir() {
    return toplayici.verileriGetir();
}