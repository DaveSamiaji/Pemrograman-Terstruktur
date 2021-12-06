sandi = open('c:\encryptedFile.txt', 'r')
n = int(input('Masukkan nilai n: '))

char = sandi.read()

huruf = list(char)

terbaca = []

for i in huruf:

    ascii1 = ord(i)
    if ascii1 == 32:
        ascii2 = ascii1
    else:

        ascii2 = ascii1 - n
        if ascii2 < 65:
            ascii2 = ascii2 + 26
        elif (90 < ascii2 and ascii2 <97):
            ascii2 = ascii2 + 26

    terj = chr(ascii2)

    terbaca.append(terj)

terjemahan = ''.join(terbaca)

hasil = open('c:\hasil.txt', 'w')

hasil.write(terjemahan)

hasil.close()
sandi.close()