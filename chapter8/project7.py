def buahpalingMahal():
    data= {'apel': 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500 }
    x = list(data.values())
    x.sort(reverse=True)
    max = x[0]
    for data, x in data.items():
        if x == max:
            print('\nBuah yang paling mahal adalah buah\n',data,max)
buahpalingMahal()
