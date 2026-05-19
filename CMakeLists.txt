cmake_minimum_required(VERSION 3.10)
project(dentMirror)

# pybind11 paketini sistemde arar ve projeye dahil eder
find_package(pybind11 REQUIRED)

# derlenecek c++ kaynak dosyalarini bir degiskende tutar
set(kaynakDosyalar
    core/src/girdiCevirici.cpp
    core/src/veriToplayici.cpp
    core/src/simulatorMotoru.cpp
    core/src/baglayici.cpp
)

# c++ kodlarini python in kullanabilecegi dentMirrorCore modulune donusturur
pybind11_add_module(dentMirrorCore ${kaynakDosyalar})