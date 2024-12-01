import math

#deklarasi fungsi
def luasPersegi(sisi):
    hitung = sisi * sisi
    print(f'luas persegi adalah {hitung}')
    
def luasPersegiPanjang(p, l):
    hitung = p * l
    print(f'luas persegi panjang adalah {hitung}')
    
def luasSegitiga(alas, tinggi):
    hitung = 1/2 * alas * tinggi
    print(f'luas segitiga adalah {hitung}')
    
def luasLingkaran(r):
    hitung = r * 3,14 * r
    print(f'luas lingkaran adalah {hitung}')
    
def luasJajargenjang(alas,tinggi):
    hitung = alas * tinggi
    print(f'luas jajargenjang adalah {hitung}')