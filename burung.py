from Animal import *

print("======BURUNG======")
class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_burung(self): 
        super().cetak()
        print("Jenis \t\t:", self.jenis,
              "\nBunyi \t\t:", self.bunyi)
        
merpati = burung("Merpati", "Jagung", "Udara", "Bertelur", "Merpati jacobin", "Berdekut")
merpati.cetak_burung()

print("==========")
gagak = burung("Gagak", "Serangga", "Udara", "Bertelur", "Corvus Frugilegus", "gak, gaok, kaok, koak")
gagak.cetak_burung()