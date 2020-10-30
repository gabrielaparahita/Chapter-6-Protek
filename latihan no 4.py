A = ga = 10000000
B = gb = 8500000
C = gc = 7000000
D = gd = 550000
pa = 2.5
pb = 2.0
pc = 1.5
pd = 1.0
pota = 2.5/100
potb = 2/100
potc = 1.5/100
potd = 1/100
kode = (input("Masukkan kode karyawan  :"))
nama = (input("Masukkan nama karyawan  :"))
gol = (input("Masukkan golongan       :"))
print ("=================================================")
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("-------------------------------------------------")
print ("Nama Karyawan            :",nama,"(Kode:",kode,")")
print ("Golongan                 :",gol)
print ("-------------------------------------------------")
if (gol == 'A'):
    print ("Gaji Pokok               :",ga)
    print ("Potongan(",pa,"%)        ",":",int (pota*A))
elif (gol == 'B'):
    print ("Gaji Pokok               :",gb)
    print ("Potongan(",pb,"%)        ",":",int (potb*B))
elif (gol == 'C'):
    print ("Gaji Pokok               :",gc)
    print ("Potongan(",pc,"%)"        ,":",int (potc*C))
elif (gol == 'D'):
    print ("Gaji Pokok               :",gd)
    print ("Potongan(",pd,"%)        ",":",int (potd*D))
print ("-------------------------------------------------")
if (gol == 'A'):
    print ("Gaji Bersih              :",int(ga-pota*A))
elif (gol == 'B'):
    print ("Gaji Bersih              :",int(gb-potb*B))
elif (gol == 'C'):
    print ("Gaji Bersih              :",int(gc-potc*C))
elif (gol == 'D'):
    print ("Gaji Bersih              :",int(gd-potd*D))




