from random import randint
Angka = randint(0, 100)
Nilai=100
print ('Hallo.. My Name is Mr.Otong ,nah aku udah milih sebuah bilangan bulat secara acak antara 0 sampai dengan 100 nih. Ayoo tebak kalo bisaa!!')
while True:
    menebak = int(input('Tebakan Kamu : '))
    if menebak > Angka :
        print ('Maaf lur bilangan kamu terlalu besar:(')
    elif menebak < Angka :
        print ('Opps bilangan kamu terlalu kecil pak')
    elif menebak == Angka :
        print ('Mantapp slurr jawabanmu benar!!')
        break
    Nilai-=2
    if Nilai==0 :
        print('Yaahhh nilai kamu sudah 0 pakk , kamu ga boleh main lagi nihh , Nice Try')
print('Nilai kamu nihh! :', Nilai)