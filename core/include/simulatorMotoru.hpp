#ifndef SIMULATORMOTORU_HPP
#define SIMULATORMOTORU_HPP

#include <string>
#include "girdiCevirici.hpp"
#include "veriToplayici.hpp"

// ana oyun dongusunu ve pencereyi yoneten sinif
class simulatorMotoru {
private:
    girdiCevirici cevirici;
    veriToplayici toplayici;
    testModu aktifMod;

public:
    simulatorMotoru(int genislik, int yukseklik);

    // secilen ayna modunu hafizaya alip sureci baslatir
    void testiBaslat(testModu mod);

    // python uzerinden gelen anlik fare hareketini isleyip loglar
    koordinat anlikHareket(int x, int y);

    // toplanan test sonuclarini python katmani icin dondurur
    std::vector<hareketVerisi> sonuclariGetir();
};

#endif