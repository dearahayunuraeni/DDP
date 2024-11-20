#SOAL NO 1
print('----Mencari celcius ke fahrenheit----')
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

#SOAL NO 2
print('\n----Mencari bilangan genap----')
def is_genap(genap):
    return genap %2 == 0
#Untuk mencetak value
print(is_genap(4))
print(is_genap(7))

#SOAL NO 3
print('\n----Mencetak nilai kelulusan----')
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return 'Lulus'
    else :
        return 'Gagal'
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))

#SOAL NO 4
print('\n----Menampilkan bilangan ganjil----')
def is_ganjil(ganjil):
    for i in range (1, ganjil, 2):
        print(i, end=" ")
print(is_ganjil(20))