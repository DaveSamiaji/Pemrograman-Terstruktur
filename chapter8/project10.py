buah = {'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7800,
    'duku' : 6500}

jenis = list(buah)
harga = list(buah.values())
tambah = 'ya'
total = 0
while True:
    namaBuah = input("Nama buah yang ingin dibeli: ")
    kgBuah = int(input("Berapa kg : "))
    indeks = jenis.index(namaBuah)
    totalSementara = harga[indeks] * kgBuah
    total = total + totalSementara
    tambah = input("Ingin beli buah yang lain(ya/tidak)? ")
    if tambah == "tidak":
        break
print("<------------------------------------------->")

print("Total harga                     : ", total)