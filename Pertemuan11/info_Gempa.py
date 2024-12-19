from Gempa import *

gempaPertama = Gempa(1.2, 'Bandung')
gempaKedua = Gempa(6.1, 'Palu')
gempaKetiga = Gempa(5.6, 'Cianjur')
gempaKeempat = Gempa(3.3, 'Jayapura')
gempaKelima = Gempa(4.0, 'Garut')

gempaPertama.dampak()
gempaKedua.dampak()
gempaKetiga.dampak()
gempaPertama.dampak()
gempaKelima.dampak()
print(f'Jumlah gempa {Gempa.jumlahGempa}')