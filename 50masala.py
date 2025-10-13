# 1-masala:
s = input("Xarid summasini kiriting: ")
if s.isdigit():
    summa = int(s)
    if summa < 50000:
        print("Chegirma yo'q")
    elif summa < 100000:
        print(" 5% chegirma")
    elif summa < 200000:
        print("10 % chegirma")
    else:
        print("15% chegirma")
else:
    print("Hurmatli foydalanuvchi faqat raqam kiriting!")


#2-masala:
svetafor = input("Yo'l chirog'i rangini kiriting: ")
if svetafor == "Qizil":
    print("To'xtang")
elif svetafor == "Sariq":
    print("Tayyorlaning")
elif svetafor == "Yashil":
    print("Yo'l bo'sh yuring")
else:
    print("Kuting!")


#3-masala:
vaqt = int(input("Vaqtni kiriting: "))
if 6 <= vaqt <= 11:
    print("Ertalabki dori")
elif 12 <= vaqt <= 17:
    print("Kunduzki dori")
elif 18 <= vaqt <= 23:
    print("Kechki dori")
else:
    print("Hozir dori ichish kerak emas!")



#4-masala:
harorat = int(input("Haroratni kiriting: "))
if harorat < 0:
    print("Qalin palto, qo'lqop kiying")
elif harorat < 15:
    print("Jaket kiying")
elif harorat < 25:
    print("Futbolka yetarli")
else:
    print("Yengil kiyim, soyabon oling")


#5-masala:
sinf = int(input("O‘quvchining sinfini kiriting (1-9): "))
ogirlik = int(input("Sumka og‘irligini kiriting (kg): "))
if 1 <= sinf <= 4 and ogirlik > 2:
    print("Og‘ir, kamaytiring!")
elif 5 <= sinf <= 9 and ogirlik > 4:
    print("Og‘ir, kamaytiring!")
else:
    print("Normal")


#6-masala:
yosh = int(input("Bemor yoshini kiriting: "))
holat = input("Bemor holatini kiriting (oddiy yoki og‘ir): ")
if yosh  < 10 or yosh > 70:
    print("Zudlik bilan")
elif holat == "og‘ir":
    print("1-soat ichida")
else:
    print("3-soat ichida")


#7-masala:
kun = input("Bugun qaysi kun? (masalan: Dushanba, Seshanba... ").lower()
masofa = float(input("Masofani kiriting (km): "))
ish_kuni = ["dushanba", "seshanba", "chorshanba", "payshanba","juma"]
dam_kuni = ["shanba", "yakshanba"]
if kun in  dam_kuni:
    if masofa > 10:
        print("Bugun dam olish kuni")
        print(f"Summa: {(3600 * masofa)* 0.9} Sizga masofa 10 kmdan oshganligi sababli 10% chegirma.")
    else:
        print("Bugun dam olish kuni")
        print(f"{3600 * masofa} so'm.")
elif kun in ish_kuni:
    if masofa > 10:
        print("Bugun ish kuni")
        print(f"Summa:{(3000 * masofa) * 0.9} so'm. Sizga masofa 10 kmdan oshganligi sababli 10% chegirma. ")
    else:
        print("Bugu ish kuni")
        print(f"Summa:{3000 * masofa} so'm.")
else:
    print("Qiymat xato kiritilgan")


#8-masala:
harorat = int(input("Haroratni kiriting (°C): "))
Ehtimol = float(input("Yomg'ir ehtimolini kiriting (%): "))
if Ehtimol >= 70:
    print("Uyda qoling")
elif harorat < 5:
    print("Juda sovuq, sayr qilish tavsiya etilmaydi")
else:
    print("Ajoyib kun, sayrga boring!")


#9-masala:
daromad = float(input("Oylik daromadingizni kiriting (so‘m): "))
xarajat = float(input("Oylik xarajatlaringizni kiriting (so‘m): "))
if xarajat > daromad:
    print("Xavfli! Xarajatlarni kamaytiring ⚠")
elif xarajat == daromad:
    print("Aynan yetarli ")
else:
    print("Ajoyib! Tejamkorlik qilyapsiz ")


#10-masala:
tur = input("Velosiped turini kiriting ('shahar' yoki 'sport'): ")
vaqt_narxi = int(input("Ijaraga olingan vaqtni kiriting (soat): "))
if tur == "shahar":
    vaqt_narx = 10000
else:
    vaqt_narx = 15000
    umumiy_narx = vaqt_narx * vaqt
    if vaqt >= 5:
       umumiy_narx *= 0.8
    elif vaqt >= 3:
       umumiy_narx *= 0.9
print("Yakuniy narx:", umumiy_narx, "so‘m")


#11-masala:
m_ogirlik = float(input("Meva og‘irligini kiriting (g): "))
m_korinish = input("Meva ko‘rinishini kiriting (“yaxshi”/“yomon”): ").lower()
if m_korinish == "yomon":
    print("Past sifat")
elif m_ogirlik < 100:
    print("Rad etiladi")
elif m_ogirlik >= 200:
    print("Premium")
else:
    print("Standart")


#12-masala:
summa = input("Harid summasini kiriting: ")
vaqt = int(input("Harid vaqtini kiriting: "))
if summa >= 100000 and 18 <= vaqt <= 22:
    print("15% chegirma")
elif 50000 >= summa < 100000 and 10 <= vaqt <= 18:
    print("10% chegirma")
else:
    print("Chegirma yo‘q")


#13-masala:
k_turi = input("Kitob turini kiriting (ilmiy, badiiy): ")
kun = int(input("Kunlar sonini kiriting: "))
if k_turi == "ilmiy":
    kun_narxi = 2000
else:
    kun_narxi = 1000
umumiy_narx = kun_narxi * kun
if kun > 14:
    umumiy_narx *= 0.7
elif kun > 7:
    umumiy_narx *= 0.8
print(f"Yakuniy narx: {umumiy_narx:.0f} so‘m")


#14-masala:
m_turi = input("Mashq turini kiriting ( kardio, ogirlik... ")
t_yili = int(input("Tajriba yilini kiriting: "))
if m_turi == "kardio" and t_yili < 1:
    print("20 daqiqa yengil")
elif m_turi == "ogir" and t_yili > 2:
    print("60 daqiqa intensiv")
else:
    print("30 daqiqa ortacha")


#15-masala:
d_nomi = input("Dastur nomii kiriting (yangilik serial...: ")
soat = int(input("Soatni kiriting: "))
if d_nomi == "yangilik" and 18 <= soat <= 20:
    print("Tomosha qiling")
elif d_nomi == "serial" and 20 <= soat <= 22:
    print("Qayta ko'ring")
else:
    print("Boshqa ko'rsatuv tanlang")



















