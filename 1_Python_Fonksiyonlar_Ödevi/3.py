vize1 = -1
vize2 = -1
final = -1

sınavlar = ["vize1= ", "vize2= ", "final= "]
notlar = [vize1, vize2, final]

for i in range (0, len(sınavlar)):
    while (notlar[i] > 100 or notlar[i] < 0):
        notlar[i] = int(input(sınavlar[i]))



hesap = ((notlar[0]*3/10)+(notlar[1]*3/10)+(notlar[2]*4/10))
harf_notu = ""

if (hesap >= 90 and hesap <= 100):
    harf_notu = "AA"
elif (hesap >= 85):
    harf_notu = "BA"
elif (hesap >= 80):
    harf_notu = "BB"
elif (hesap >= 75):
    harf_notu = "CB"
elif (hesap >= 70):
    harf_notu = "CC"
elif (hesap >= 65):
    harf_notu = "DC"
elif (hesap >= 60):
    harf_notu = "DD"
elif (hesap >= 55):
    harf_notu = "FD"
else :
    harf_notu = "FF"


print(harf_notu, hesap)