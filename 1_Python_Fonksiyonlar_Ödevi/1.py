min = int(input("min sayı = "))
max = int(input("max sayı = "))
bolen = int(input("bolen sayı = "))


def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):
    tam_bolunenler = list()
    for sayi in range(min_sayi, max_sayi+1):
        if (sayi % bolen_sayi == 0):
            tam_bolunenler.append(sayi)
    return print("Tam bölünenler = ", tam_bolunenler, "\nToplam sayı", (max_sayi - (min_sayi + 1)))

bolunen_sayi_bulma(min, max, bolen)