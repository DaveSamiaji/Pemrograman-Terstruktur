
file = open('c:\myFile.txt', 'w')

lagi = 'y'
while lagi == 'y':
    nim = input('Masukkan NIM          : ')
    nama = input('Masukkan Nama Mhs     : ')
    alamat = input('Masukkan Alamat       : ')
    dataAwal = [nim, nama, alamat]

    data = '|'.join(dataAwal) + '\n'

    file.write(data)
    lagi = input('Ulangi input lagi(y/n): ')
file.close()
file = open('c:\myfile.txt', 'r')
hasil = file.read()
print(hasil)
file.close()