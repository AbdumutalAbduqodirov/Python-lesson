# Sikil operatorlari || looplar
# For loop
# Salom Avazbek sizni ko'rganimdan xursandman..!
# mehmonlar = ["Avazbek", "Abdullajon", "Sanjarbek", "Otabek"]
# # print(f"Salom {mehmonlar[0]} sizni ko'rganimdan xursandman..!")

# for mehmon in mehmonlar:
#     print(f"Salom {mehmon} sizni ko'rganimdan xursandman..!")
# print("Salom sizni ko'rish bu baht ",mehmon)

# int
# sonlar = list(range(1,11))
# #print(sonlar)
# son_kvadrat = []
# for son in sonlar:
#     son_kvadrat.append(son**2)

# print(sonlar)
# print(son_kvadrat)

# futbol = []
# print("Eng yaxshi 4 ta futbolchini kriting")
# for n in range(4):  # kiritishimiz mumkin bo'lgan futbolchilar soni 
#     futbol.append(input(f"{n + 1} - ta eng yaxshi futbolchilar ismini kriting:  "))

# print(futbol)

# TARMOQLANISH 

mehmonlar = ["Avazbek", "Abdullajon", "Sanjarbek", "Otabek"]

# for mehmon in mehmonlar:
#     if mehmon == "Abdullajon":
#         print(mehmon.upper())
#     else: 
#         print(mehmon.title())

# ism = input("Ismingizni kriting..?\n>> ")
# if ism.lower() == "avazbek":
#     print(f"Sizni kutayotgan edik {ism.title()}")
# else:
#     print(f"Uzur {ism.title()} biz Avazbekni kutayotgan edik... ")

# Parol 8 ta belgidan kam bo'lmasin
# login = input("Login kriting: ")
# if len(login) >= 8:
#     print("Siz to'g'ri login kritdingiz")
# elif len(login) < 8:
#      print("Belgilar soni 8 tadan kam: qayta kriting ")

kun = input("Bugungi xafta kunini kriting: ")
harorat = int(input("Havo haroratini kriting: "))
if kun.lower() == "yakshanba" and harorat >= 30:
    print("Bugun dam olish kuningiz....\n Bemalol cho'milishga borishingiz mumkin...")
elif kun.lower() != "yakshanba" or harorat < 30:  
    if kun.lower() != "yakshanba":
        print("Harorat a'lo darajada ammo bugun ish kuningiz cho'milaolmaysiz...")
    else:
        print("Bugun dam olish kuningiz ammo havo harorati past(sovuq)")  
