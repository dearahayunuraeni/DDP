# SOAL NO 1
kendaraan = ["aerox", "motor", "200cc", "roda 2"]
kendaraan.append("25.000.000")
kendaraan.append("matic")
kendaraan.insert(2, "honda")
print(kendaraan)


#SOAL NO 2
pilihan =int(input("""Pilih Nomor Pilihan:
1 : Menghitung luas persegi
2 : Menghitung luas lingkaran
3 : Menghitung luas segitiga
"""))

match pilihan :
        case 1:
            print("Menghitung luas persegi")
            s = int(input("Masukan nilai sisi: "))
            luasPersegi = s * s
            print(f"Luas persegi dengan sisi {s} adalah {luasPersegi}")
        case 2:
            print("Menghitung luas lingkaran")
            pi = 3.14
            r = int(input("Masukan nilai jari-jari: "))
            luasLingkaran = pi * r ** 2
            print(f"Luas lingkaran dengan jari-jari {r} adalah {luasLingkaran}")
        case 3:
            print("Menghitung luas segitiga")
            alas = int(input("Masukan nilai alas: "))
            tinggi = int(input("Masukan tinggi: "))
            luasSegitiga = 1/2 * alas * tinggi
            print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")
        case _:
            print("input tidak valid")
        