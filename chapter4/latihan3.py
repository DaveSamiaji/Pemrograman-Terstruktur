print ("--Pengisian BBM perjalanan dari kota A ke kota C--")


jaraktempuh= int(input("Masukkan jarak tempuh: "))
print ("Perbandingan konsumsi BBM")
bbm= int(input("bbm = "))
jarak= int(input("jarak = "))
jumlahbensin= bbm/jarak*jaraktempuh

print ("Jumlah bensin yang dikeluarkan: ",jumlahbensin,"liter")
if (jumlahbensin>50):
    isibensin= jumlahbensin//50
elif (jumlahbensin<50):
    isibensin= 0
print ("minimal isi bensin: ",isibensin,"kali")

