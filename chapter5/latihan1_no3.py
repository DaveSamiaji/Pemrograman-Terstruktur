print("**** Status Kelulusan Ujian ****")
Nama= (input("Nama : "))
nilaimtk= int(input("Nilai Matematika : "))
nilaibindo= int(input("Nilai Bahasa Indonesia :"))
nilaiipa= int(input("Nilai IPA :"))
if(nilaimtk<0) or (nilaibindo<0) or (nilaiipa<0) or (nilaimtk>100) or (nilaibindo>100) or (nilaiipa>100):
    print("Maaf input ada yang tidak valid")
elif(nilaimtk>70) and (nilaibindo>=60) and (nilaiipa>=60):
    print("Status Kelulusan : ", Nama,"DINYATAKAN LULUS")
else:
    print("Status Kelulusan : ", Nama,"DINYATAKAN TIDAK LULUS")
    print("Sebab")
    if (nilaimtk < 70):
        print("Nilai Matematika kamu kurang dari 70")
    if (nilaibindo < 60):
        print("Nilai Bahasa Indonesia kamu kurang dari 60")
    if (nilaiipa < 60):
        print("Nilai IPA kamu kurang dari 60")

