x = int(input('Ingin memasukkan berapa angka? : '))
bil = []
for i in range(x):
    a = int(input('Masukkan bilangan bulatnya : '))
    bil.append(a)
bil.sort()
bil.reverse()
print('\nHasil bilangan dengan urutan dari angka besar ke kecil adalah2\n',bil)