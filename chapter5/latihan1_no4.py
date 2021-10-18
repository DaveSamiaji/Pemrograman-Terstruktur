NamaKar = input("Masukkan Nama Karyawan: ")
KodeKar = input("Masukkan Kode Karyawan: ")
Golongankar = str(input("Masukkan Golongan     : "))
if (Golongankar == "a") or (Golongankar == "A"):
    GajiPokok = 10000000
    Persen = 2.5

elif (Golongankar == "b") or (Golongankar == "B"):
    GajiPokok = 8500000
    Persen = 2.0

elif (Golongankar == "c") or (Golongankar == "C"):
    GajiPokok = 7000000
    Persen = 1.5

elif (Golongankar == "D") or (Golongankar == "d"):
    GajiPokok = 5500000
    Persen = 1.0

else:
    print("Golongan tidak valid")

GajiKotor = Persen / 100 * GajiPokok
GajiBersih = GajiPokok - GajiKotor

print("************************************")
print("")
print("STRUK RINCIAN GAJI KARYAWAN")
print("")
print("************************************")
print("")
print("Nama Karyawan    : " + NamaKar + " (Kode : " + KodeKar + ")")
print("Golongan         : " + Golongankar)
print("")
print("####################################")
print("")
print("Gaji Pokok       : Rp.", GajiPokok)
print("Potongan (" + str(Persen) + "%)  : Rp.", int(GajiKotor))
print("")
print("####################################")
print("")
print("Gaji Bersih      : Rp.", int(GajiBersih))