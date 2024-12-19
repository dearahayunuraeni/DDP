from Mahasiswa import * 
from Dosen import *

m1 = Mahasiswa("Dea Rahayu Nuraeni", "Perempuan", 19,"SI",1)
m2 = Mahasiswa("Muhamad Parhan", "Laki - laki",20,"TI",1)
d1 = Dosen("Adam Syamsul Bahri", "Laki - laki", 45,"S. Pd.","Staff Tata Usaha" )
d2 = Dosen("Dewantari Mastiyo", "Wanita", 28,"S. Kom., M.M", "Dosen Pembimbing")

d1.setGaji(12000000)
d2.setGaji(15000000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()