NamaKar = input("Masukkan Nama Karyawan: ")
KodeKar = input("Masukkan Kode Karyawan: ")
Golongankar = str(input("Masukkan Golongan     : "))
if (Golongankar == "a") or (Golongankar == "A"):
    GajiPokok = 10000000
    Potongan = 2.5
elif (Golongankar == "b") or (Golongankar == "B"):
    GajiPokok = 8500000
    Potongan = 2.0
elif (Golongankar == "c") or (Golongankar == "C"):
    GajiPokok = 7000000
    Potongan = 1.5
elif (Golongankar == "d") or (Golongankar == "D"):
    GajiPokok = 5500000
    Potongan = 1.0
else:
    print("Golongan tidak valid")

StatusMenikah = int(input("Masukkan Status (1: Menikah, 2: Belum): "))

if (StatusMenikah == 1):
    Status = "Menikah"
    TunjanganMenikah = 10 / 100 * GajiPokok
    JumlahAnak = int(input("Masukkan jumlah Anak  : "))
    TunjanganAnak = 5 / 100 * GajiPokok
    TunjanganAnak = TunjanganAnak * JumlahAnak

elif (StatusMenikah == 2):
    Status = "Belum Menikah"
    TunjanganMenikah = 0
    TunjanganAnak = 0
    JumlahAnak = "-"

else:
    print("Status Menikah Tidak Valid")

GajiKotor = GajiPokok + TunjanganMenikah + TunjanganAnak
Potongan = Potongan / 100 * GajiKotor
GajiBersih = GajiKotor - Potongan

print("************************************")
print("")
print("STRUK RINCIAN GAJI KARYAWAN")
print("")
print("*************************************")
print("")
print("Nama Karyawan    : " + NamaKar + " (Kode : " + KodeKar + ")")
print("Golongan         : " + Golongankar)
print("Status Menikah   : " + Status)
print("Jumlah Anak      : " + str(JumlahAnak))
print("")
print("####################################")
print("")
print("Gaji Pokok       : Rp.", GajiPokok)
print("Tunjangan Menikah: Rp.", int(TunjanganMenikah))
print("Tunjangan Anak   : Rp.", int(TunjanganAnak))
print("")
print("####################################")
print("")
print("Gaji Kotor       : Rp.", int(GajiKotor))
print("Potongan (" + str(Potongan) + "%)  : Rp.", int(Potongan))
print("")
print("####################################")
print("")
print("Gaji Bersih      : Rp.", int(GajiBersih))
print("")
print("====================================")






