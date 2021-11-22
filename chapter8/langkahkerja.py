#1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(a)
print(b)

#2
a.insert(2, 10)
b.insert(1, 15)
print(a)
print(b)

#3
a.append(4)
b.append(8)
print(a)
print(b)

#4
a.sort()
b.sort()
print(a)
print(b)

#5
c = a[:8]
d = b[2:10]
print(c)
print(d)

#6
e = []
for num in range(len(c)):
    e += [c[num]+d[num]]
print(e)


#7
e = tuple(e)
print(e)

#8
print(min(e))
print(max(e))
print(sum(e))

#9
myString = "python adalah bahasa pemrograman yang menyenangkan"

#10
myString = set(myString)
print(myString)

#11
myString = list(myString)
myString.sort()
print(myString)
