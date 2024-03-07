class insan:
    def __init__(self):
        self.ad = "ad"
        self.soyad = "soyad"
        self.yas = 0
        self.ulke = "Turkey"
        self.sehir = "Ankara"
        self.yetenekler = []

    def kisi_bilgileri(self):
        return print(self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler)

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


x = insan()
x.ad = "hüseyin"
x.yas = 29
x.yetenek_ekle("python")
x.yetenek_ekle("java")
x.kisi_bilgileri()