print("status kelulusan siswa")
nilaiindo = a = int(input("masukkan nilai bahasa indonesia:"))
nilaiipa = b = int(input("masukkan nilai ipa:"))
nilaimtk = c = int(input("masukkan nilai matematika:"))

if (a>60):
    if (b>60):
        if (c>70):
            print("Status Kelulusan: LULUS")
else:
    print ("Status Kelulusan: TIDAK LULUS")
    print ("Sebab:")
    if (a<60):
        print ("-Nilai bahasa indonesia kurang dari 60")
    if (a<70):
        print ("-Nilai matematika kurang dari 70")
