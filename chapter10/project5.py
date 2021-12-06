
asal = open('c:\data2.txt', 'r')

tujuan = open('c:\hasil.txt', 'w')

data = asal.readlines()

for i in range(len(data)):
    bil = data[i]
    #memisahkan data
    bilA, bilB = bil.split('|')
    #menjumlah dua bilangan
    bilC = int(bilA) + int(bilB)
    bil3 = str(bilC)
    #menuliskan hasil pada file baru
    tujuan.write(bil3)
    tujuan.write('\n')
tujuan.close()
hasil = open('c:\hasil.txt', 'r')
print(hasil.read())
hasil.close