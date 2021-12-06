find = input('Massukkan NIM yang mau dicari: ')

file = open('c:\myfile.txt', 'r')
isi = file.readlines()
for i in range(len(isi)):
    mhs = isi[i]
    nim, nama, alamat = mhs.split('|')
    if nim == find :
        data = 'ada'

        print('Data Mahasiswa')
        print('NIM    : ', nim)
        print('Nama   : ', nama)
        print('Alamat : ', alamat)
        break
    else:
        data = 'none'

if data == 'none':
    print('Data mahasiswa tidak ditemukan')