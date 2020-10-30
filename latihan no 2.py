print("status kelulusan siswa")
nilaiindo = a = int(input("masukkan nilai bahasa indonesia:"))
nilaiipa = b = int(input("masukkan nilai ipa:"))
nilaimtk = c = int(input("masukkan nilai matematika:"))

if (a<60):
    if (a<96):
        if (a<80):
            print("LULUS")
else:
    print ("Maaf input ada yang tidak valid")
