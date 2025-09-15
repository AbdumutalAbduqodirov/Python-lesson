# sonlar (int)
# a = 5
# b = 5.5
# aholi_soni = 3_986_759_899

# print(type(a))
# print(type(b))
# print(type(aholi_soni))

# O'zgarmas son kotta xarflarda nomlanadi
# P = 3.14
# print(P)
# print(type(P))

# x, y, z = 55, "hello", 3.6
# print(x)
# print(y)
# print(z)

# a = 55
# a = str(a)
# a = float(a)
# a = int(a)

# print(a)
# print(type(a))

# yil = input("Tug'ilgan yilingizni kriting \n>>:")
# yosh = 2025 - int(yil)
# print("Sizning yoshingiz  " + str(yosh)+" da.")  

# List  ~ arry (massiv)
# mehmon1 = "Abdullajon"
# mehmon2 = "Sanjarbek"
# mehmon3 = "Kamoliddin"
# print(mehmon1)
# print(mehmon2)
# print(mehmon3)
#                0              1             2
# menhmonlar = ["Abdullajon", "Sanjarbek", "Kamoliddin"]
# sonlar = [1,2,3,4,5,7,-9,-8,-6,-4,5]
# aralash = [1, 5.6, "Kamola", True]
# pustoy = []
# pustoy.append("olma")
# pustoy.append("Anor")
# print(pustoy)
# menhmonlar[0] = "Ahmadjon"
# print(menhmonlar[0].upper())
# print(sonlar[0] + sonlar[-1])
# print(aralash)
# print(menhmonlar)
# .append - massivga oxiridan qiymat qo'shish
# menhmonlar.append("Ahmadjon")
# print(menhmonlar)
# print(len(menhmonlar))
# .insert - massivga qiymat qo'shadi istagan joyidan
# menhmonlar.insert(3,"Mushtariy")
# print(menhmonlar)
# del - metod rmas || .remove()
menhmonlar = ["Abdullajon", "Sanjarbek", "Kamoliddin","Mushtariy","Ahmadjon"]
# del menhmonlar[0]
# print(menhmonlar)
# menhmonlar.remove("Sanjarbek")
print(menhmonlar)
menhmon = menhmonlar.pop(0)
print(menhmon)
print(menhmonlar)
