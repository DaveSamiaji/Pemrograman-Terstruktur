def kuadrat(angka):
    hasil = []
    for data in range(len(angka)):
        result = angka[data] ** 2
        hasil = hasil + [result]
    return hasil  #

angka = [2, 3, 4, 5, 6]
print(kuadrat(angka))