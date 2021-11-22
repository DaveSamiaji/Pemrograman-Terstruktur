
buah = {'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7800,
    'duku' : 6500}

jenis = list(buah)
harga = list(buah.values())
namaBuah = input("Nama buah yang ingin dibeli: ")
kgBuah = int(input("Berapa kg : "))
print("<------------------------------------------->")
indeks = jenis.index(namaBuah)
total = harga[indeks] * kgBuah
print("Total harga                     : ", total)