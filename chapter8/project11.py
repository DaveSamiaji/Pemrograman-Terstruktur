
print("Menu:")
print("A. Tambah data")
print("B. Beli buah")
buah = {'apel' : 5000,
    'jeruk' : 8500,
    'mangga' : 7800,
    'duku' : 6500}
pilih = input("Pilihan Menu : ")
if pilih == "a" :
    nama = input("Masukkan nama buah    : ")
    harga = int(input("Masukkan harga satuan : "))
    ada = nama in buah.keys()
    if ada == True:
        print("Nama buah sudah terdaftar")
    else:
        buah[nama] = harga
    print("Data buah: ")
    for x, y in buah.items() :
        print("-", x, "(Harga Rp", y, ")")
elif pilih == "b":

    jenis = list(buah)
    harga = list(buah.values())
    tambah = 'ya'
    total = 0
    while True:
        namaBuah = input("Nama buah yang dibeli: ")
        kgBuah = int(input("Berapa kg : "))
        indeks = jenis.index(namaBuah)
        totalSementara = harga[indeks] * kgBuah
        total = total + totalSementara
        tambah = input("Ingin beli buah yang lain(ya/tidakk)? ")
        if tambah == "tidak":
            break
    print("<------------------------------------------->")

    print("Total harga                     : ", total)