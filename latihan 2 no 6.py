import random
angka = random.randint(1,100)  

maksimum_tebakan = 50
nomor_tebakan = 0
tebakan_benar = False

print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!'.format(maksimum_tebakan))

teks_petunjuk = 'tebakan ke-{} anda.'
while not tebakan_benar and not nomor_tebakan >= maksimum_tebakan:
  nomor_tebakan = nomor_tebakan + 1
  tebakan = input(teks_petunjuk.format(nomor_tebakan))
  tebakan = int(tebakan)
  if tebakan == angka:
    tebakan_benar = True
  elif tebakan > angka:
    print('Hehehe… Bilangan tebakan anda terlalu besar')
  else:
    print('Hehehe… Bilangan tebakan anda terlalu kecil')
  

if tebakan_benar:
  print('Yeeee… Bilangan tebakan anda BENAR :-)'.format(nomor_tebakan))
else:
  print('Skore anda habis, anda kalah')

