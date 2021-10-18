print("**** Status Kelulusan Ujian ****")
Nama= (input("Nama : "))
nilaimtk= int(input("Nilai Matematika : "))
nilaibindo= int(input("Nilai Bahasa Indonesia :"))
nilaiipa= int(input("Nilai IPA :"))
if(nilaimtk>70) and (nilaibindo>=60) and (nilaiipa>=60):
    print("Status Kelulusan : ", Nama,"DINYATAKAN LULUS")
else:
    print("Status Kelulusan : ", Nama,"DINYATAKAN TIDAK LULUS")
