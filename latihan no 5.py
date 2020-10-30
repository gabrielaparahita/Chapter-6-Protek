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
ta = 5
ti = 10
tunank = 5/100
tunis = 10/100
gajikotora = 11500000
gajikotorb = 9775000
gajikotorc = 8050000
gajikotord = 6077500
pothargaa = 2500000
pothargab = 170000
pothargac = 105000
pothargad = 55000

# masukkan keterangannya
kode = (input("Masukkan kode karyawan  :"))
nama = (input("Masukkan nama karyawan  :"))
gol = (input("Masukkan golongan       :"))
sta = (input("Masukkan status         :"))
if (sta== '1'):
    ank = input("Masukkan jumlah anak    :")

# tampilan
print ("=================================================")
print ("STRUK RINCIAN GAJI KARYAWAN")
print ("-------------------------------------------------")
print ("Nama Karyawan            :",nama,"(Kode:",kode,")")
print ("Golongan                 :",gol)
print ("Status Menikah           :",sta)
if (sta== '1'):
    print("Jumlah anak              :",ank)
print ("-------------------------------------------------")

# gaji pokok
if (gol == 'A'):
    print ("Gaji Pokok               :",ga)
elif (gol == 'B'):
    print ("Gaji Pokok               :",gb)
elif (gol == 'C'):
    print ("Gaji Pokok               :",gc)
elif (gol == 'D'):
    print ("Gaji Pokok               :",gd)

# tunjangan anak istri
if (sta== '1'):
    if (gol == 'A'):
      print("Tunjangan Istri/Suami    :",int(tunis*ga))
    elif (gol == 'B'):
      print("Tunjangan Istri/Suami    :",int(tunis*gb))
    elif (gol == 'C'):
      print("Tunjangan Istri/Suami    :",int(tunis*gc))
    elif (gol == 'D'):
      print("Tunjangan Istri/Suami    :",int(tunis*gd))
ank = 1
if (sta == '1'):
        if (gol == 'A'):
          print("Tunjangan Anak           :",int(tunank*ga*ank))
        elif (gol == 'B'):
          print("Tunjangan Anak           :",int(tunank*gb*ank))
        elif (gol == 'C'):
          print("Tunjangan Anak           :",int(tunank*gc*ank))
        elif (gol == 'D'):
          print("Tunjangan Anak           :",int(tunank*gd*ank))
print ("-------------------------------------------------+")

# gaji kotor nih
if (sta== '2'):
    if (gol == 'A'):
      print("Gaji Kotor    :",ga)
      
    elif (gol == 'B'):
      print("Gaji Kotor    :",gb)
    elif (gol == 'C'):
      print("Gaji Kotor    :",gc)
    elif (gol == 'D'):
      print("Gaji Kotor    :",gd)
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

# gaji bersih nih
if (sta== '1'):
    if (gol == 'A'):
      print("Gaji Bersih              :", gajikotora-pothargaa)
    elif (gol == 'B'):
      print("Gaji Bersih              :", gajikotorb-pothargab)
    elif (gol == 'C'):
      print("Gaji Bersih              :", gajikotorc-pothargac)
    elif (gol == 'D'):
      print("Gaji Bersih              :", gajikotord-pothargad)
if (sta== '2'):
    if (gol == 'A'):
      print("Gaji Bersih              :", ga-pothargaa)
    elif (gol == 'B'):
      print("Gaji Bersih              :", gb-pothargab)
    elif (gol == 'C'):
      print("Gaji Bersih              :", gc-pothargac)
    elif (gol == 'D'):
      print("Gaji Bersih              :", gd-pothargad)
