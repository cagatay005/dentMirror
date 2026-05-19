#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "../include/simulatorMotoru.hpp"

namespace py = pybind11;

// c++ siniflarini ve yapilarini python a baglayan ana modul
PYBIND11_MODULE(dentMirrorCore, m) {
    
    // ayna zorluk modlarini python enum yapisina aktarir
    py::enum_<testModu>(m, "testModu")
        .value("yatayTers", yatayTers)
        .value("dikeyTers", dikeyTers)
        .value("tamAyna", tamAyna)
        .export_values();

    // toplanan verileri python tarafinda okunabilir hale getirir
    py::class_<hareketVerisi>(m, "hareketVerisi")
        .def_readwrite("zamanDamgasi", &hareketVerisi::zamanDamgasi)
        .def_readwrite("x", &hareketVerisi::x)
        .def_readwrite("y", &hareketVerisi::y)
        .def_readwrite("hataDurumu", &hareketVerisi::hataDurumu);

    // islenmis koordinat yapisini python'a acar
    py::class_<koordinat>(m, "koordinat")
        .def_readwrite("x", &koordinat::x)
        .def_readwrite("y", &koordinat::y);

    // motor sinifini ve guncel fonksiyonlari python a acar
    py::class_<simulatorMotoru>(m, "simulatorMotoru")
        .def(py::init<int, int>())
        .def("testiBaslat", &simulatorMotoru::testiBaslat)
        .def("anlikHareket", &simulatorMotoru::anlikHareket)
        .def("sonuclariGetir", &simulatorMotoru::sonuclariGetir);
}