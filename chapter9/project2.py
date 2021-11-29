def bintang(n):
    j = 1
    k = 1 + 2*(n)
    for i in range(n):
        a = "*" * j

        print(a.center(k))
        j +=2
bintang(4)