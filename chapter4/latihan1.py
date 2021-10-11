print ("----Rental Mobil Dave----")

#input data
tarif1= int(input("Masukkan tarif awal rental /12 jam:"))
tarif2= int(input("Masukkan tarif tambahan jika lebih dari 12 jam /jam:"))
print ("Masukkan waktu peminjaman mobil")
jampinjam= int(input("jam:"))
menitpinjam= int(input("menit:"))
print ("Masukkan waktu pengembalian mobil")
jamkembali= int(input("jam:"))
menitkembali= int(input("menit:"))
selisihjam= jamkembali-jampinjam
selisihmenit= menitkembali-menitpinjam


print ("Total waktu rental:",selisihjam,"jam",selisihmenit,"menit")
if (selisihjam>12):
    total= selisihjam-12
    biayarental= total*tarif2 + selisihmenit/60*tarif2 + tarif1
elif (selisihjam<12):
    total= selisihjam
    biayarental= total*tarif2 + selisihmenit/60*tarif2
elif (selisihjam==12):
    total= selisihjam
    biayarental= tarif1
    
print ("Biaya rental: ",biayarental)
bayar= int(input("Masukkan pembayaran: "))
kembalian= (bayar-biayarental)
print ("Uang kembalian: ","Rp.",kembalian)
