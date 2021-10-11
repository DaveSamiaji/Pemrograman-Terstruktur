print ("---LAMA PERJALANAN PAK AMIR---")

def lamaAB(jarak1,rata1,break1):
    return(jarak1/rata1)*60+break1

def lamaBC(jarak2,rata2,break2):
    return(jarak2/rata2)*60+break2

def total(totalAB,totalBC):
    return totalAB+totalBC

#perjalanan dari kota A ke B
jarak1= int(input("Masukkan jarak A ke B = "))
rata1= int(input("Masukkan rata-rata kecepatan dari A ke B(km/jam) = "))
break1= int(input("Masukkan waktu istirahat(menit) = "))

#perjalanan dari kota B ke C
jarak2= int(input("Masukkan jarak B ke C = "))
rata2= int(input("Masukkan rata-rata kecepatan dari B ke C(km/jam) = "))
break2= int(input("Masukkan waktu istirahat(menit) = "))

totalAB= lamaAB(jarak1,rata1,break1)
totalBC= lamaBC(jarak2,rata2,break2)

totalperjalanan= total(totalAB,totalBC)

print ("Lama perjalanan dari kota A ke C adalah",totalperjalanan,"menit")
print ("Atau",int(totalperjalanan/60),"jam")

def totalmenit(totalperjalanan):
    return totalperjalanan/60-round(totalperjalanan/60)

def waktutiba(waktu,totalperjalanan):
    return waktu+totalperjalanan/60

#waktu sampai tujuan
waktu= float(input("Masukkan waktu keberangkatan = "))
totalwaktu= waktutiba(waktu,totalperjalanan)
totalwaktumenit= totalmenit(totalperjalanan)*60

print ("Pak Amir tiba pukul : ",round(totalwaktu),"jam",round(totalwaktumenit),"menit")
