class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinif = ogrenci_sinif


ali = Ogrenci('ali', 'veli', 3)
print(ali.ogrenci_adi, ali.ogrenci_soyadi, ali.ogrenci_sinif)


class Soru:
    def net_sayisi(self, dogru, yanlis):
        return dogru - (yanlis / 4)

    def hesapla(self, net):
        return print(net * 2)


x = Soru()
net = x.net_sayisi(44, 6)
x.hesapla(net)
