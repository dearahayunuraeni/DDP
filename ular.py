from Animal import *
print("======ULAR======")
class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, design, racun):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.design = design
        self.racun = racun

    def cetak_ular(self): 
        super().cetak()
        print("Design \t\t:", self.design,
              "\nRacun \t\t:", self.racun)
        
anaconda = ular("Anaconda", "Daging", "Darat", "Bertelur", "Batik", "Tidak Berbisa")
anaconda.cetak_ular()

print("==========")
python = ular("Python", "Daging", "Darat", "Bertelur", "Sanca Batik", "Berbisa")
python.cetak_ular()

