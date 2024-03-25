from math import floor

i = int(input("sayı = "))


def sayi_atama(sayi):
    while sayi > 99 or sayi < 10:
        sayi = int(input("sayı iki haneli olmalı ! sayı = "))
    x = sayi
    print(sayi_okunusu(x))


def sayi_okunusu(oku):
    bolum = floor(oku / 10)
    bolum_oku = ""
    kalan = oku % 10
    kalan_oku = ""

    if bolum == 1:
        bolum_oku = "on"
    elif bolum == 2:
        bolum_oku = "yirmi"
    elif bolum == 3:
        bolum_oku = "otuz"
    elif bolum == 4:
        bolum_oku = "kırk"
    elif bolum == 5:
        bolum_oku = "elli"
    elif bolum == 6:
        bolum_oku = "altmış"
    elif bolum == 7:
        bolum_oku = "yetmiş"
    elif bolum == 8:
        bolum_oku = "seksen"
    else:
        bolum_oku = "doksan"

    if kalan == 1:
        kalan_oku = "bir"
    elif kalan == 2:
        kalan_oku = "iki"
    elif kalan == 3:
        kalan_oku = "üç"
    elif kalan == 4:
        kalan_oku = "dört"
    elif kalan == 5:
        kalan_oku = "beş"
    elif kalan == 6:
        kalan_oku = "altı"
    elif kalan == 7:
        kalan_oku = "yedi"
    elif kalan == 8:
        kalan_oku = "sekiz"
    elif kalan == 9:
        kalan_oku = "dokuz"
    else:
        kalan_oku = ""

    return print("{}{}".format(bolum_oku, kalan_oku))


sayi_atama(i)
