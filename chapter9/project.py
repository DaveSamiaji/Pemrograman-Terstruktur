def ubahHuruf(teks, a, b):

    listHuruf= list(teks)
    baru = []
    for i in range (len(listHuruf)):
        huruf = listHuruf[i]

        if huruf == a:
            huruf = b
        baru = baru + [huruf]

    hasil= "".join(baru)
    return hasil
y = ubahHuruf('MATEMATIKA', 'T', 'S')
print(y)
