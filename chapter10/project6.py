
nama = input("Masukkan nama file: ")
n = int(input('Masukkan nilai n  : '))

asli = open(nama, 'r')

char = asli.read()

huruf = list(char)

tersandi = []
for i in huruf:

    ascii1 = ord(i)

    if ascii1 == 32:
        ascii2 = ascii1
    else:

        ascii2 = ascii1 + n
        if ascii2 > 122:
            ascii2 = ascii2 - 26
        elif ascii2 > 90 and ascii2 <97 :
            ascii2 = ascii2 - 26
    sandi = chr(ascii2)
    tersandi = tersandi +[sandi]
    if not huruf:
        break

encrypted = ''.join(tersandi)

hasil = open('c:\encryptedFile.txt', 'w')
hasil.write(encrypted)
hasil.close()