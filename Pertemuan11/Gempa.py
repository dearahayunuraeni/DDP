#Membuat kelas gempa

class Gempa:

    jumlahGempa = 0

    def __init__(self, skala, lokasi):
        self.skala = skala
        self.lokasi = lokasi
        Gempa.jumlahGempa +=1

    def dampak(self):
        if self.skala < 2:
            dampak = 'Gempa tidak terasa'
        elif self.skala >= 2 and self.skala < 4:
            dampak = 'Gempa bangunan retak - retak'
        elif self.skala >= 4 and self.skala < 6:
            dampak = 'Gempa bangunan roboh'
        elif self.skala >= 6 :
            dampak = 'Bangunan roboh dan berpotensi tsunami'

        print(f'Gempa di lokasi {self.lokasi} dengan skala {self.skala}, berpotensi {dampak}')