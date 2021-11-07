try:
    namafile= input('Masukkan Nama File disini: ')
    file=open(namafile,'r')
    print(file.read())
except FileNotFoundError:
    print('Maaf File ini tidak ditemukan')