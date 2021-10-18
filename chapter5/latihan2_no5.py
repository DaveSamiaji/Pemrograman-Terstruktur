from random import randint
Angka = randint(0, 100)
print ('Hallo.. My Name is Mr.Otong , nah aku udah milih sebuah bilangan bulat secara acak antara 0 sampai dengan 100 nih. Ayoo tebak kalo bisa!')
while True:
    menebak = int(input('Tebakan Kamu nih : '))
    if menebak > Angka :
        print ('Sayang sekali bilangan Kamu terlalu besar lurr ')
    elif menebak < Angka :
        print ('sayang sekali bilangan Kamu kekecilan pak ')
    elif menebak == Angka :
        print ('GG lur tebakanmu benar, SELAMAT YA!!')
        break