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
m_korinish = input("Meva ko‘rinishini kiriting (“yaxshi”/“yomon”): ")
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


#16-masala:
tur = input("Skuter turi (elektr/oddiy): ")
masofa = float(input("Masofani kiriting (km): "))
if tur == "elektr":
    km_narx = 2000
else:
    narx_km = 1000
umumiy_narx = km_narx * masofa
if masofa > 10:
    umumiy_narx *= 0.85
print("Yakuniy narx:", umumiy_narx, "so'm")


#17-masala:
m_turi = input("Muommo turini kiriting(dasturiy, uskunaviy ")
if m_turi == "dasturiy":
    print("50000")
else:
    q_narx = float(input("Qisim narxini kiriting "))
    if q_narx >= 100000:
        print("150000")
    else:
        print("To'lov: 80000")


#18-masala:
i_darajasi = int(input("Ifloslanish darajasini kiriting(%): "))
sh_tezligi = int(input("Shamol tezligini kiriting(km/soat: "))
if i_darajasi > 50 and sh_tezligi < 5:
    print("Maska kiying")
elif i_darajasi <= 50 and sh_tezligi >= 10:
    print("Sof havo")
else:
    print("Oddiy holat")


#19-masala:
k_turi = input("Kurs turini kiriting(akvarel, yog'li): ")
oy_davomliligi = int(input("Davomliligini kiriting(oy): "))
if k_turi == "akvarel":
    oy_narx = 200000
else:
    narx_oy = 300000
umumiy_narx = oy_narx * oy_davomliligi
if  oy_davomliligi >= 3:
    umumiy_narx *= 0.9
print("Yakuniy narx:")


#20-masala:
q_turi = input("Qulf turini kiriting(elektron, mexanik): ")
yosh = int(input("Yoshini kiriting(yil): "))
if q_turi == "elektron" and yosh < 2:
    print("Yuqori xavfsizlik")
elif q_turi == "mexanik" and yosh < 5:
    print("O'rtacha xavfsizlik")
else:
    print("Past xavfsizlik")


#21-masala:
hudud = input("Hudud turini kiriting(shahar markazi, shahar cheti...): ")
x_soni = int(input("Xonar sonini kiriting: "))
if hudud == "shahar markazi" and x_soni == 3:
    print("5000000")
elif hudud == "shahar cheti" and x_soni == 2:
    print("3000000")
else:
    print("2000000")


#22-masala:
quvvat = int(input("Quvvat foizini kiriting(%): "))
masofa = float(input("Masofani kiriting(km): "))
if quvvat < 20 and masofa > 5:
    print("Zaryadlang")
elif quvvat < 50 and masofa < 3:
    print("Extiyot bo'ling")
else:
    print("Yaxshi holat")


#23-masala:
ruxsat = int(input("Kamera ruxsatini kiriting(MP): "))
y_darajasi = input("Yorug'lik darajasini kiriting(yaxshi,o'rtacha,yomon): ")
if ruxsat >= 12 and y_darajasi == "yaxshi":
    print("Yuqori sifat")
elif ruxsat >= 8 and y_darajasi == "O'rtacha":
    print("O'rtacha sifat")
else:
    print("Past sifat")


#24-masala:
masofa = int(input("Masofani kiriting(km): "))
havo = input("Ob-havo darajasini kiriting(yaxshi,o'rtacha,yomon): ")
if masofa < 5 and havo == "yaxshi":
    print("Piyoda")
elif masofa < 20 and havo == "o'rtacha":
    print("Velosiped")
else:
    print("Avtobus")


#25-masala:
email = input("Email manzilingizni kiriting: ")
if len(email) >= 10 and email.endswith("@gmail.com"):
    print("Qabul qilindi")
elif len(email) < 10 and email.endswith("@yahoo.com"):
    print("Qisqa email")
else:
    print("Noto'g'ri email")


#26-masala:
ovqat = input("Ovqat turini kiriting(salat,go'sht): ")
porsiya = float(input("Porsiya turini kiriting(g): "))
if ovqat == "salat":
    asosiy_kkal = (porsiya/100) * 50
    if porsiya >= 300:
        print(f"Umumiy kkal:{asosiy_kkal * 1.1}")
elif ovqat == "go'sht":
    asosiy_kkal = (porsiya/100)* 200
    if porsiya >= 300:
        print(f"Umumiy kkal: {asosiy_kkal}")
else:
    print("Qiymatni to'g'ri kiriting ")


#27-masala:
summa = int(input("Kredit summasini kiriting(mln so'm): "))
muddat = int(input("Muddatni kiriting(yil): "))
if summa < 10 and muddat == 1:
    print("12%")
elif summa >= 10 and muddat == 2:
    print("10%")
else:
    print("15%")


#28-masala:
sinf = input("Sinfni kiriting(biznes/ekonom): ")
masofa = float(input("Masofani kiriting(km): "))
if sinf == "biznes" and masofa < 1000:
    asosiy = 1000000
    if masofa >= 1000:
        print(f"Yakuniy narx:{asosiy * 1.2}")
    else:
        print("C")
elif sinf == "ekanom" and masofa < 1000:
    asosiy = 5000000
    if masofa >= 1000:
        print(f"Yakuniy narx:{asosiy * 1.2}")
    else:
        print("Yakuniy narx:{asosiy}")
elif sinf == "biznes":
    asosiy = 1000000
    if masofa >= 1000:
        print(f"Yakuniy narx:{asosiy}")
elif sinf == "ekonom":
    asosiy = 5000000
    if masofa >= 1000:
        print(f"Yakuniy narx:{asosiy * 1.2}")
    else:
        print("Yakuniy narx:{asosiy}")
else:
    print("Qiymatda xatolik")


#29-masala:
m_turi = input("Mahsulot turini kiriting(lo'shon/krem): ")
oy = int(input("Oylar sonini kiriting: "))
if m_turi == "lo'shon" and oy >= 6:
    print("Ishlatish mumkun emas")
elif m_turi == "krem" and oy >= 12:
    print("Ishlatish mumkun emas")
else:
    print("Xavfsiz ishatishingiz mumkun")


#30-masala:
k_turi = input("Kiyim turini kiriting(bolalar/kattalar): ")
if k_turi == "bolalar":
    print("2 kun")
else:
    olcham = input("O'lcham turini kiriting:(S,M,L,XL): ")
    if olcham == "s" or olcham == "M":
        print("4 kun")
    else:
        print("6 kun")


#31-masala
qavatlar = int(input("Tort nechta qavatli bo‘lsin? (kamida 1): "))
meva = input("Meva qo‘shilsinmi? (ha/yo‘q): ")
shokolad = input("Shokolad qo‘shilsinmi? (ha/yo‘q): ")
Asosiy = 100000 + (qavatlar - 1) * 50000
if meva == "ha":
    asosiy += 20000
    if shokolad == "ha":
        asosiy += 30000
        print("Tortning yakuniy narxi:", asosiy)


#32-masala:
mato = input("Mato turini kiriting(paxta/sintetik/..): ")
i_darajasi = input("Ifloslanish darajasini kiriting(yengil/og'ir..): ")
if mato == "paxta" and i_darajasi == "yengil":
    print("Rejim 1")
elif mato == "sintetik" and i_darajasi == "og'ir":
    print("Rejim 3")
else:
    print("Rejim 2")


#33-masala:
k_turi == input("Kitob turini kiriting(sir/jinoyat/sevgi/romantik/kosmos/kelajak): ")
if k_turi == "sir" or "jinoyat":
    print("Detektiv")
elif k_turi == "sevgi" or "romantika":
    print("Romantik")
elif k_turi == "kosmos" or "kelajak":
    print("Fantastik")
else:
    print("Boshqa")


#34-masala:
ch_turi = input("Chipta turini kiriting(VIP/oddiy): ")
yosh = int(input("Yoshingizni kiriting: "))
if ch_turi == "VIP" and yosh > 60:
    print("50000")
elif ch_turi == "oddiy" and yosh < 18:
    print("20000")
else:
    print("30000")


#35-masala:
kun = input("Bugun qaysi kun? (dushanba, seshanba, ... , yakshanba): ")
soat = int(input("Soat nechchi? (0–23): "))
ish_kunlari = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma"]
dam_kunlari = ["shanba", "yakshanba"]
if kun in ish_kunlari and 9 <= soat <= 18:
    print("Ochiq")
elif kun in dam_kunlari and 10 <= soat <= 16:
    print("Ochiq")
else:
    print("Yopiq")


#36-masala:
o_turi = input("O'simlik turini kiriting(gul/daraxt): ")
fasl = input("Fasilni kiriting(bahor/yoz/kuz/qish): ")
if o_turi == "gul" and fasl == "bahor":
    print("Haftada 3 marta sug'oring")
elif o_turi == "darxt" and fasl == "yoz":
    print("Har kuni sug'oring")
elif o_turi == "gul" and fasl == "qish":
    print("Haftada 1 marta sug'oring")
else:
    print("Haftada 2 marta sug'oring")


#37-masala:
budjet = int(input("Budjetni kiriting(so‘mda): "))
vip = input("VIP kerakmi?(ha/yo‘q): ")
yaxshi_korish = input("Yaxshi ko‘rish kerakmi?(ha/yo‘q): ")
if budjet > 100000 and vip == "ha":
    print("Birinchi qator VIP")
elif budjet > 100000 and vip == "yo‘q":
    print("Birinchi qator oddiy")
elif budjet <= 100000 and yaxshi_korish == "ha":
    print("O'rta qatorlar")
else:
    print("Orqa qatorlar")


#38-masala:
foiz = int(input("Xotira bandligi foizini kiriting(%): "))
if foiz > 95:
    print("Xotira to'la! Tozalash kerak")
elif foiz > 80:
    print("Xotira kam qoldi")
elif foiz > 50:
    print("Xotira yetarli")
else:
    print("Xotira bo'sh")


#39-masala:
ball = int(input("Umumiy ballni kiriting: "))
if ball > 90:
    print("Ustoz")
elif ball > 70:
    print("Malakali")
elif ball > 50:
    print("O'rta")
else:
    print("Boshlang'ich")


#40-masala:
ball = int(input("Umumiy ballingizni kiriting(0-100): "))
if ball > 90:
    print("5 baxo")
elif ball > 70:
    print("4 baxo")
elif ball > 60:
    print("3 baxo")
else:
    print("Ball yetarli emas")


#41-masala:
yosh = int(input("Yoshingizni kiriting: "))
talaba_h = input("Talabamisiz(ha/yo'q): ")
if yosh < 7:
    print("Bepul")
elif talaba_h == "ha":
    print("5000")
elif yosh > 60:
    print("Chegirma: 3000")
else:
    print("7000")


#42-masala:
oy = int(input("Oy raqamini kiriting(1-12): "))
if oy == 12 or oy == 1 or oy == 2:
    print("Qish")
elif oy == 3 or oy == 4 or oy == 5:
    print("Bahor")
elif oy == 6 or oy == 7 or oy == 7:
    print("Yoz")
else:
    print("Kuz")


#43-masala:
model = input("Telefon modelini kiriting(iPhone/Samsung): ")
holat = input("Telefon holatini kiriting(yaxshi/ishlatilgan): ")
if model == "iPhone" and holat == "yangi":
    print("1200")
elif model == "iPhone" and holat == "ishlatilgan":
    print("800")
elif model == "Samsung" and holat == "yangi":
    print("900")
else:
    print("600")


#44-masala:
yosh = int(input("Yoshingizni kiriting: "))
ball = int(input("Test ballingizni kiriting: "))
if yosh > 6 and ball > 70:
    print("Qabul qilindi")
else:
    print("Qabul qilinmadi")


#45-masala:
tezlik = (input("Internet tezligini kiriting(Mbps): "))
if tezlik < 5:
    print("Juda sekin")
elif tezlik < 20:
    print("O'rtacha")
elif tezlik <= 100:
    print("Tez")
else:
    print("Juda tez")


#46-masala:
vaqt = input("Vaqtni kiriting(kam/ko'p/o'rtacha): ")
joy = input("Joy mavjudligini kiriting(kam/ko'p): ")
sabr = input("Sabr borligini kiriting(bor/yo'q): ")
if vaqt == "kam" and joy == "kam":
    print("Baliq")
elif vaqt == "ko'p" and sabr == "bor":
    print("it")
else:
    print("Mushuk")


#47-masala:
yosh = int(input("Yoshingizni kiriting: "))
tajriba = input("Tajriba muddatingizni kiriting(yil): ")
daraja = input("Ingliz tili bo'yicha darajangizni kiriting(o'rta/yaxshi): ")
if yosh >= 20 and tajriba >= 2 and daraja == "o'rta" or daraja == "yaxshi":
    print("Qabul qilindi")
else:
    print("Qabul qilinmadi")


#48-masala:
yil = int(input("Yilni kiriting(butun son): "))
if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print("Kabisa yili")
else:
    print("Kabisa yili emas")


#49-masala:
daromad = float(input("Oylik daromadingizni kiriting (mln so‘mda): "))
if daromad <= 1:
    print("0%")
elif daromad <= 3:
    print("10%")
else:
    print("20%")


#50-masala:
yosh = int(input("Yoshingizni kiriting: "))
mahsulot = input("Mahsulot turini kiriting (Oziq-ovqat/kiyim/texnika...): ")
if mahsulot == "oziq-ovqat":
    print("Chegirma yo‘q")
elif yosh < 12:
    print("20% chegirma")
elif yosh > 60:
    print("15% chegirma")
else:
    print("Chegirma mavjud emas")






















