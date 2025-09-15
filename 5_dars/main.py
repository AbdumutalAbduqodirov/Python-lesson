
# text = "Hello"
# a = text.swapcase() # Kichik xarfni kottaga kotani kichik
# b = text.isalpha() # Kiritilayotgan matin faqat xarifdan iborat bo'lsa true aks xolda false
# print(b)
# print(text.find("o")) # Tekshirilayotgan matin ichda aynan o'sha xarf bor yoki yo'qligini tekshiradi index kalitini chiqarib beradi agar xato bo'lsa qiymat -1 ga teng bo'ladi
# print(text.find("i")) # Tekshirilayotgan matin ichda aynan o'sha xarf bor yoki yo'qligini tekshiradi
# print(text.index("h")) # Tekshirilayotgan matin ichda aynan o'sha xarf bor yoki yo'qligini tekshiradi index kalitini chiqarib beradi agar xato bo'lsa qiymat qaytarmaydi

# menu = ["osh", "bishtekis", "lag'mon", "kuksi", "somsa"]
# # print("sho'rva" in menu)
# # taom = input("Qanday taom buyurasiz:\n >>")
# taom = ["osh",'kola','pitsa','lipton']
# for mijoz in taom:
#     if mijoz.lower() in menu:
#         print(f"Buyurtmangiz {mijoz} bor.")
#     else:
#         print(f"Kechirasiz {mijoz} bizda mavjud emas.")

#*********** Xatoliklar ********************
#SyntaxError
# print("Hello world")

# IndentationError
#  print("Hello world")
# for n in range(10):
# print(n)

# TypeError: - ma'lumot turida xatolik
# num = input("Son krit \n>>")
# print(num + 2)

# NameError - o'zgaruvchi yozilishida xatolik
# mevalar = ['olma', 'banana', 'kivi']
# for meva in mevaler:
#     print(meva)

# ValueError: - qiymat xatoligi
# num = int(input("Son krit \n>>"))
# if num > 0:    
#     print("Musbat")
# else:
#     print("Manfiy")

# IndexError: - kiritilayotgan index xatoligi
# mevalar = ['olma', 'banana', 'kivi']
# print(mevalar[3])

# ZeroDivisionError: - sonni 0 ga bo'lish mumkin emas
# x, y = 50, 50
# z = 250/(x-y)
# print(z)

# Mantiqiy xatoliklar
# rad = 5
# p = 4.14 # 3.14
# ayl_yuzi = p*rad*2
# print(ayl_yuzi)

# son = float(input("Istalgan son kriting:\n>>"))
# ildiz = son**0.5
# print(f"{son} ning ildizi {ildiz} ga teng.")