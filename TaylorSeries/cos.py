
import math


def fac(x):
    if x < 2:
        return x

    return x * fac(x-1)


def cos(x, e=0.001):
    tanda = 1
    suku = 1
    n = 0
    jumlah = 0
    iterasi = 0

    galatAprox = 0

    while abs(suku) >= e:
        jumlah = jumlah + suku
        n = n + 2
        tanda = -1*tanda
        suku = tanda * (x ** n) / fac(n)
        galatAprox = abs((suku)) / (jumlah + suku)
        iterasi = iterasi + 1

    galatSebenarnya = (jumlah - math.cos(5)) / math.cos(5)
    return iterasi, galatSebenarnya, galatAprox, jumlah


print(cos(5))
