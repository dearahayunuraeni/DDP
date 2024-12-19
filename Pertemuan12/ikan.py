from Animal import *

print("======IKAN======")
class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.jenis = jenis
        self.warna = warna

    def cetak_ikan(self): 
        super().cetak()
        print("Jenis \t\t:", self.jenis,
              "\nWarna \t\t:", self.warna)
        
Koi = ikan("Koi", "Pelet", "Air", "Bertelur", "Koi goromo", "Indigo, Hitam, Putih")
Koi.cetak_ikan()

print("==========")
Tuna = ikan("Tuna", "Cumi - Cumi", "Air", "Bertelur", "Tuna Thunus", "Biru Kehitaman")
Tuna.cetak_ikan()