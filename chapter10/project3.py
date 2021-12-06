
file= open('c:\myfile.txt', 'r')

data = file.readlines()

dataMahasiswa = {}

for i in range(len(data)):
    mhs = data[i]

    nim, nama, alamat = mhs.split('|')
    alamat = alamat.replace('\n', '')

    dataMhs = {'nim': nim, 'nama': nama, 'alamat': alamat}
    dataMahasiswa[nama] = dataMhs
print(dataMahasiswa)

file.close()