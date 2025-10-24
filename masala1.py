# Ichma-ich shart operatorlaridan masalalar

#1-masala:
ball = int(input("Ballni kiriting(0-100): "))
if ball < 0 or ball > 100:
    print("Xato: Ball 0 dan 100 gacha bo‘lishi kerak")
else:
    if ball >= 90:
        print("A")
    elif ball >= 80:
        print("B")
    elif ball >= 70:
        print("C")
    elif ball >= 60:
        print("D")
    else:
        print("F")



#2-masala:
yosh = int(input("Yoshingizni kiriting(0 <= 120): "))
daromad = float(input("Daromadni kiriting(>= 0): "))
if 0 < yosh > 120 or daromad <0:
    print("Xato: Yosh 0-120 oralig‘ida, daromad musbat bo‘lishi kerak.")
else:
    if yosh < 18:
        print("Soliq: 0%")
    elif yosh <= 60:
        if daromad > 5000:
            print("Soliq: 20%")
        else:
            print("Soliq: 10%")
    else:
        print("Soliq: 5%")


#3-masala:
kun = int(input("Hafta kunini kiriting(1-7): "))
soat = int(input("Soatni kiriting(0-23): "))
if kun < 1 or kun > 7 or soat < 0 or soat > 23:
    print("Xato: Kun 1-7, soat 0-23 oralig‘ida bo‘lishi kerak")
else:
    if kun == 6 or kun == 7:
        print("Dam olish kuni")
    else:
        if  9 <= soat <= 17:
            print("Ish vaqti")
        else:
            print("Ish vaqtidan tashqari")


#4-masala:
harorat = int(input("Haroratni kiriting(°C): "))
y_holat = input("Yomg'ir holatini kiriting(True/False): ")
if harorat < -50 or harorat > 60:
    print("Xato: Harorat –50°C dan 60°C gacha bo‘lishi kerak.")
else:
    if harorat < 0:
        print("Qor yog‘ishi mumkin")
    elif harorat <= 20:
        if y_holat == "True":
            print("Yomg‘irli va sovuq")
        else:
            print("Sovuq, lekin quruq")
    else:
        print("Issiq")


#5-masala:
masofa = float(input("Masofani kiriting(km): "))
vaqt = float(input("Vaqtni kiriting(soat): "))
if masofa < 0 or vaqt < 0:
    print("Xato: Masofa va vaqt manfiy bo‘lmasligi kerak")
else:
    if masofa < 5:
        print("Piyoda boring")
    elif masofa <= 50:
        if vaqt > 1:
            print("Avtobus")
        else:
            print("Velosiped")
    else:
        print("Samolyot")


#6-masala:
yosh = int(input("Yoshingizni kiriting: "))
daromad = float(input("Daromatingizni kiriting: "))
k_summasi = float(input("Kredit summasini kirting: "))
if yosh < 18 or yosh > 100 or daromad < 0 or k_summasi <= 0:
    print("Xato: Yosh 18-100 oralig'ida, daromad va kredit summasi musbat bo'lishi kerak")
else:
    if yosh < 21:
        print("Kredit berilmaydi")
    elif yosh <= 60:
        if daromad > k_summasi * 0.2:
            print("Kredit tasdiqlandi")
        else:
            print("Kredit rad etildi")
    else:
        print("Kredit faqat maxsus shartlarda")


#7-masala:
tur = input("Ovqat turini kiriting(go'sht/baliq/vegetarian): ")
narx = float(input("Narxni kiriting: "))
if narx <= 0:
    print("Xato: Narx musbat bo'lishi kerak")
else:
    if tur == "Go'sht":
        if narx > 50:
           print("Premium go'shtli taom")
        else:
           print("Oddiy go'shtli taom")
    elif tur == "Baliq":
        print("Baliqli taom")
    elif tur == "Vegeterian":
        if narx > 30:
            print("Premium vegetarian")
        else:
            print("Oddiy vegetarian")
    else:
        print( "Xato: Noto'g'ri ovqat turi")


#8-masala:
baho = int(input("Bahongizni kiriting: "))
daromad = float(input("Daromadingizni kiriting: "))
if baho < 0 or baho > 5.0 or daromad < 0:
    print("Xato: Baho 0-5.0 oralig'ida, daromad musbat bo'lishi kerak")
else:
    if baho < 3.0:
        print("Stipendiya yo'q")
    elif baho < 4.0:
        if daromad < 1000:
            print("Oddiy stipendiya")
        else:
            print("Stipendiya yo'q")
    else:
        if daromad < 2000:
            print("Yuqori stipendiya")
        else:
            print("Stipensiya yo'q")


#9-masala:
daqiqa = int(input("Daqiqani kiriting(>=0): "))
internet = int(input("Internetni kiriting(GB,>= 0): "))
if daqiqa < 0 or internet < 0:
    print("Xato: Daqiqalar va internet manfiy bo'lmasligi kerak")
else:
    if daqiqa < 100:
        print("Mini tarif")
    elif  daqiqa <= 500:
        if internet > 5:
            print("Standart tarif")
        else:
            print("Ekonom tarif")
    else:
        print("Premium tarif")


#10-masala:
harorat = int(input("Haroratni kiriting(-50 harorat <= 50): "))
sh_tezligi = int(input("Shamol teligini kiriting(m/s): "))
if harorat < 10 and sh_tezligi > 10:
    print("Uyda qoling")
elif harorat <=25:
    if sh_tezligi < 5:
        print("Sayr qiling")
    else:
        print("Ehtiyot bo'ling")
else:
    print("SUv iching")


























