from random import randint
sum = 0
while True:
 bil = randint(0,10)
 sum = sum + 1
 print(bil)
 if bil == 5:
   break
 print('Jumlah perulangan : ' + str(sum))
