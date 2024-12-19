import math

#deklarasi fungsi
def luasBalok(p, l, t):
    hitung = 2 * (p*l) + (p*t) + (l*t)
    print(f'luas balok adalah {hitung}')
    
def luasKubus(s):
    hitung = 6 * s * s
    print(f'luas kubus adalah {hitung}')
    
def luasTabung(r, t):
    hitung = 2 * 3,14
    print(f'luas tabung adalah {hitung}')
    
def luasLimasSegitiga(a,t):
    hitung = 1/2 * a * t
    print(f'luas limas adalah {hitung}')
    
def luasPrismaSegitiga(a,t):
    hitung = 1/2 * a * t
    print(f'luas prisma segitiga adalah {hitung}')