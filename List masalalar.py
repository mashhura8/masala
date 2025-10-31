# Python List Masalalari
#1-masala:
fruits = ['olma','banan','uzum']
fruits.append('nok')
uzunlik = len(fruits)
olma = 'olma' in fruits
banan_index = fruits.index('banan')
print("Ro'yhat",fruits)
print("Ro'yhat uzunligi",uzunlik)
print("Ro'hatda olma bormi",olma)
print("Index",banan_index)


#2-masala:
colors = ['qizil','yashil','kok']
colors.append('sariq')
colors.sort()
uzunlik = len(colors)
yashil = 'yashil' in colors
print("Ro'yhat",colors)
print("Alifbo tartibida",colors)
print("Ro'yhat uzunligi",uzunlik)
print("Ro'yhatda yashil bormi",yashil)


#3-masala:
cities = ['Toshkent','Samarqand','Buxoro']
cities.append('Xiva')
samarqand_index = cities.index('Samarqand')
uzunlik = len(cities)
cities.sort()
print("Ro'yhat",cities)
print("Index",samarqand_index)
print("Ro'yhat uzunligi",uzunlik)
print("Alifbo tartibida",cities)


#4-masala
numbers = [5,2,8,1]
numbers.append(10)
numbers.sort()
uzunlik = len(numbers)
mavjud = 8 in numbers
print("Ro'yhat",numbers)
print("O'sish tartibida",numbers)
print("Ro'yhat uzunligi",uzunlik)
print("Ro'yhatda 8 bormi",mavjud)


#5-masala:
animals = ['mushuk','it','qush']
animals.append('baliq')
animals.sort()
index = animals.index('it')
uzunlik = len(animals)
print("Ro'yhat",animals)
print("Alifbo tartibida",animals)
print("Index",index)
print("Ro'yhat uzunligi",uzunlik)


#6-masala:
fruits = ['olma', 'banan', 'uzum', 'nok']
fruits.append('kivi')
fruits.remove('banan')
fruits.insert(3,'shaftoli')
fruits.sort()
uzunlik = len(fruits)
olma_index = fruits.index('olma')
m_kivi = 'kivi' in fruits
fruits.sort(reverse=True)
copy_fruits = fruits.copy()
copy_fruits.append('ananas')
print("Asil ro'yhat",fruits)
print("Nusxa",copy_fruits)
print(f"Teskari tartibda: {fruits}")
print("Alifbo tartibida",fruits)
print("Ro'yhat uzunligi",uzunlik)
print("Index",index)


#7-masala:
menu = ['osh', "lag'mon", 'shashlik', 'somsa']
menu.extend(['manti','norin'])
menu.sort()
menu.pop()
uzunlik = len(menu)
o_index = menu.index('osh')
soni = menu.count('somsa')
m_index = menu.index('manti')
copy_menu = menu.copy()
copy_menu.append('qozon kabob')
print("Asil ro'yhat",menu)
print("Nusxa",copy_menu)
print("Alifbo tartibida",menu)
print("O'chirilgan taom", menu)
print("Ro'yhat uzunligi",uzunlik)
print("Index",o_index)
print("Somsa nechta borligi", soni)
print("index",m_index)


#8-masala:
cities = ['Toshkent', 'Samarqand', 'Buxoro', 'Xiva']
cities.insert(0,'Andijon')
cities.remove('Xiva')
s_index = cities.index('Samarqand')
cities.sort()
uzunlik = len(cities)
b_mavjud = "Buxoro" in cities
cities.pop()
cities.sort(reverse=True)
copy_cities = cities.copy()
copy_cities.append('Fargona')
print("Asil ro'yhat",cities)
print("Nusxa",copy_cities)
print("Index",s_index)
print("Alifbo tartibida",cities)
print("Ro'yhatda Buxora mavjudmi",b_mavjud)
print("O'chirilgan shahar", cities)
print(f"Teskari tartibda: {cities}")


#9-masala:
students = ['Ali', 'Vali', 'Sardor', 'Aziz']
students.append('Jamshid')
students.remove('Sardor')
students.insert(1,'Diyor')
students.sort()
a_index = students.index('Aziz')
mavjud = 'Diyor' in students
students.pop()
uzunlik = len(students)
copy_students = students.copy()
copy_students.append('Nodir')
print("Asil ro'yhat",students)
print("Nusxa", students)
print("Alifbo tartibida",students)
print("Index",a_index)
print("Ro'yhatda Diyor mavjudmi",mavjud)
print("O'chirilgan talaba", students)


#10-masala:
favorites = ['telefon', 'noutbuk', 'naushnik']
favorites.append('planshet')
favorites.append('soat')
favorites.sort()
uzunlik = len(favorites)
index = favorites.index('noutbuk')
t_mavjud = 'telfon' in favorites
favorites.remove('naushnik')
favorites.pop()
copy_favorites = favorites.copy()
copy_favorites.append('televizor')
favorites.sort(reverse=True)
print("Asil ro'yhat",favorites)
print("Nusxa",favorites )
print("Alifbo tartibida",favorites)
uzunlik = len(favorites)
print("Index",index)
print("Ro'yhatda telfon mavjudmi",t_mavjud)
print("O'chirilgan mahsulot",favorites)
































