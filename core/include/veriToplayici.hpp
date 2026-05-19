#ifndef VERITOPLAYICI_HPP
#define VERITOPLAYICI_HPP

#include <vector>
#include <chrono>

// anlik hareket ve hata durumunu tutan yapi
struct hareketVerisi {
    long long zamanDamgasi;
    int x;
    int y;
    bool hataDurumu;
};

// test boyunca uretilen verileri ram uzerinde saklayan sinif
class veriToplayici {
private:
    std::vector<hareketVerisi> toplananVeriler;
    std::chrono::time_point<std::chrono::high_resolution_clock> baslangicZamani;

public:
    // zaman sayacini sifirlar ve testi baslatir
    void testiBaslat();

    // anlik koordinat ve hata durumunu listeye ekler
    void veriEkle(int x, int y, bool hata);

    // toplanan tum verileri dondurur
    std::vector<hareketVerisi> verileriGetir();

    // yeni test icin listeyi temizler
    void verileriTemizle();
};

#endif