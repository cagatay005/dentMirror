#include "../include/veriToplayici.hpp"

// zaman sayacini sifirlar ve testi baslatir
void veriToplayici::testiBaslat() {
    baslangicZamani = std::chrono::high_resolution_clock::now();
}

// anlik koordinat ve hata durumunu listeye ekler
void veriToplayici::veriEkle(int x, int y, bool hata) {
    auto anlikZaman = std::chrono::high_resolution_clock::now();
    auto gecenSure = std::chrono::duration_cast<std::chrono::milliseconds>(anlikZaman - baslangicZamani).count();
    
    hareketVerisi yeniVeri;
    yeniVeri.zamanDamgasi = gecenSure;
    yeniVeri.x = x;
    yeniVeri.y = y;
    yeniVeri.hataDurumu = hata;
    
    toplananVeriler.push_back(yeniVeri);
}

// toplanan tum verileri dondurur
std::vector<hareketVerisi> veriToplayici::verileriGetir() {
    return toplananVeriler;
}

// yeni test icin listeyi temizler
void veriToplayici::verileriTemizle() {
    toplananVeriler.clear();
}