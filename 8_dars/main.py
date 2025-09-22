# *****input*******
# ism = input("Ismingizni kriting:\n")
# savol = f"Salom , {ism.title()} tug'ilgan yilingizni kriting ? \n >>"
# yosh = int(input(savol))
# res = 2025 - yosh
# boyi = float(input("Bo'yingiz necha metir ?\n >>"))

# print(f"{ism.title()}ning ma'lumotlari: \n",
#       f"Yoshi: {res}\n",
#      f"Bo'yi: {boyi}\n" )

# ******** While  ******
# son = 1
# while son <= 5:
#     print(son)
#     son +=1
# print("\nDastur tugadi")
#
# print("Kiritilgan sonlarning kvadrati qaytaruvchi dastur tuzilsin.")
# savol = "Istalgan sonni kriting "
# savol += "dasturni yakunlash uchun 'stop' deb yozing: \n>"
# qiymat = ' '
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(float(qiymat)**2)
# print("Dastur tugadi")

# boolen
# print("Kiritilgan sonlarning kvadrati qaytaruvchi dastur tuzilsin.")
# savol = "Istalgan sonni kriting "
# savol += "dasturni yakunlash uchun 'stop' deb yozing: \n>"
# qiymat = True
# while qiymat:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         qiymat= False
#     else:    
#         print(float(qiymat)**2)
# print("Dastur tugadi")

# break
# print("Kiritilgan sonlarning kvadrati qaytaruvchi dastur tuzilsin.")
# savol = "Istalgan sonni kriting "
# savol += "dasturni yakunlash uchun 'stop' deb yozing: \n>"
# while True:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#        break
#     else:    
#         print(float(qiymat)**2)
# print("Dastur tugadi")

# break for
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 11:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng.")

# continue
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng.")

# son = 0
# while son <= 10:
#     son +=1
#     if son % 2 != 0:
#         continue
#     print(son)

# ***** ro'yhatlar ****
print("Siz yaxshi ko'rgan dasturchilar ro'yxatini tiuzamiz: ")
ismlar = []
n = 1 # isimlarni sanash uchun
while True:
    savol = f"{n} - dasturchini ismini kiriting."
    ism = input(savol)
    ismlar.append(ism)
    takror = input("Yana isim qo'shasizmi ? (ha/yo'q)")
    n+=1
    if takror != 'ha':
        break
print("dastur to'xtadi")    
print("Sizning dasturchilaringiz ro'yxati:")
for ism in ismlar:    
    print(ism.title())