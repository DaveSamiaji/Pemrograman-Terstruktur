
def terbaik(data):
    rekap = []
    for a in range(len(data)):
        list = nilaiMhs[a]
        nilaiAkhir = (list['mid'] + 2*list['uas']) / 3
        rekap.append(nilaiAkhir)
    best = rekap.index(max(rekap))
    where = data[best]
    who = where['nama'] + " " + where['nim']
    return who
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

print('\nNilai terbaik diraih oleh\n',terbaik(nilaiMhs))