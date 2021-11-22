sayur = ['Bayam', 'Kangkung', 'Wortel', 'Selada']

print('Menu: ')
print('A. Tambah data sayuran')
print('B. Hapus data sayuran')
print('C. Tampilkan data sayuran')

pilih = input('Pilih Opsi: ')
while True:
    try:
        if pilih == 'A' or pilih == 'a':
            tambah = input('Tambahan data sayur:')
            sayur.append(tambah)
        elif pilih == 'B' or pilih == 'b':
            hapus = input('data Sayuran yang dihapus:')
            sayur.remove(hapus)
        elif pilih == 'C' or pilih == 'c':
            for veg in range(len(sayur)):
                print(str(sayur[veg]), end=" ")
            print ()
        pilih = input('Pilih Opsi: ')
    except ValueError:
        print('Data tidak valid')
        break