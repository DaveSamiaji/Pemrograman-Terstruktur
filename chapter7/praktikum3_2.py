try:
    file = open('d:/dataa.txt','r')
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except ValueError:
    print('Tipe data tidak valid')