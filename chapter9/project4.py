import random
def shuffleString(x,n):

    kata = list(x)

    listHasil = []
    listHasil1 = []
    while True:

        random.shuffle(kata)

        hasil = "".join(kata)

        a = hasil in listHasil1
        if a == False:
            listHasil1 = listHasil1 + [hasil]
        if len(listHasil1)== n :
            listHasil = listHasil1
            break
    return listHasil
print(shuffleString('aku',2))
print(shuffleString('aku',3))
print(shuffleString('aku',4))