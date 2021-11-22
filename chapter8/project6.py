def sortStringByChar(n):
    hasil = []
    banyak = len(n) - 1
    panjang = len(n[0])
    for data in range(banyak):
        x = len(n) - 1
        i = 0

        while i < x:
            if len(n[i]) > len(n[i + 1]):
                besar = n[i]
                kecil = n[i + 1]
            elif len(n[i]) < len(n[i + 1]):
                besar = n[i + 1]
                kecil = n[i]
            i += 1
        hasil.append(kecil)
        n.remove(kecil)
    hasil.insert(0, besar)
    return hasil


myData = ['apel', 'rambutan', 'jeruk ']
print(sortStringByChar(myData))